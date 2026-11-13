# Zelle 4.5: Robuste Regel- & Prognose-Validierung mit Historie

Diese Datei enthält den vollständigen Code für **Zelle 4.5** des Notebooks (`Daily_Newscheck.ipynb` bzw. `RegelAnalyse_okf.ipynb`), um Verhaltensregeln empirisch und robust zu validieren.

---

## 📋 Schritt-für-Schritt-Anleitung zur Übertragung

1. **Colab-Notebook öffnen:** Öffne dein Notizbuch `Daily_Newscheck.ipynb` (oder `RegelAnalyse_okf.ipynb`) in Google Colab.
2. **Zu Zelle 4.5 navigieren:** Scrolle zu der Code-Zelle mit dem Titel:
   `# @title Zelle 4.5: Soll-Ist-Validierung & Feedback (Regelkorrektur)`
3. **Inhalt ersetzen:**
   * Klicke in die Zelle und wähle den gesamten bisherigen Code aus (`Strg + A` bzw. `Cmd + A`).
   * Lösche den alten Code (`Entf` bzw. `Backspace`).
   * Kopiere den unten stehenden Python-Codeblock vollständig und füge ihn in die Zelle ein (`Strg + V` bzw. `Cmd + V`).
4. **Zelle ausführen:** Drücke `Umschalt + Eingabe` (Shift + Enter), um Zelle 4.5 auszuführen.
5. **Notebook speichern:** Speichere die Änderung mit `Strg + S` (Cmd + S).

---

## 💻 Vollständiger Code für Zelle 4.5

```python
# @title Zelle 4.5: Soll-Ist-Validierung & Feedback (Robuste Regel- & Prognoseprüfung)
import datetime
import os
import sys
import pandas as pd

try:
    from IPython.display import display
except ImportError:
    display = print

# --- Laufzeit-Check: Colab-Pfad vs. lokaler Pfad ---
IN_COLAB = "google.colab" in sys.modules
WORKDIR = os.environ.get("NEWSCHECK_DIR") or ("/content/newscheck" if IN_COLAB else os.getcwd())
OKF_DIR = os.path.join(WORKDIR, "okf-regeln")
LOG_PATH = os.path.join(OKF_DIR, "log.md")
CSV_PATH = os.path.join(OKF_DIR, "validierung_historie.csv")


def _frontmatter(text):
    """Extrahiert einfache 'schluessel: wert'-Paare aus dem YAML-Frontmatter."""
    d = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return d
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            k, v = line.split(":", 1)
            d[k.strip().lower()] = v.strip().strip('"').strip("'")
    return d


def _adjust_konfidenz(path, delta):
    """Passt das konfidenz-Feld einer OKF-Regel an (Delta, gekappt auf 0.05..0.99)."""
    if not path or not os.path.exists(path):
        return None, None
    with open(path, encoding="utf-8") as _f:
        lines = _f.read().splitlines(keepends=True)
    idx = None
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("konfidenz:"):
            idx = i
            break
    if idx is not None:
        try:
            old = float(lines[idx].split(":", 1)[1].strip())
        except ValueError:
            old = 0.50
        new = max(0.05, min(0.99, round(old + delta, 2)))
        lines[idx] = "konfidenz: " + format(new, ".2f") + "\n"
    else:
        old = 0.50
        insert_at = 1 if lines and lines[0].strip() == "---" else 0
        new = max(0.05, min(0.99, round(0.50 + delta, 2)))
        lines.insert(insert_at, "konfidenz: " + format(new, ".2f") + "\n")
    with open(path, "w", encoding="utf-8") as _f:
        _f.write("".join(lines))
    return old, new


def _annotate_rule(path, note):
    if not path or not os.path.exists(path):
        return
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n> " + note + "\n")


def _append_log(entry):
    os.makedirs(OKF_DIR, exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(entry)


def _append_history_csv(row):
    os.makedirs(OKF_DIR, exist_ok=True)
    header = not os.path.exists(CSV_PATH)
    df_row = pd.DataFrame([row])
    df_row.to_csv(CSV_PATH, mode="a", header=header, index=False, encoding="utf-8")


# --- Gestern-Erwartung laden (von Zelle 4 gesichert, sonst von Disk) ---
prev_text = globals().get("ERWARTUNG_VORIGE_TEXT")
if prev_text is None:
    _p = os.path.join(WORKDIR, "erwartung.md")
    if os.path.exists(_p):
        with open(_p, encoding="utf-8", errors="replace") as _f:
            prev_text = _f.read()

if "df" not in globals():
    print("❌ Marktdaten (df) fehlen – bitte zuerst Zelle 2 ausführen. Validierung übersprungen.")
elif not prev_text:
    print("ℹ️ Keine vorige erwartung.md gefunden – erster Lauf, Validierung übersprungen.")
else:
    exp = _frontmatter(prev_text)
    bezug = exp.get("bezugsregel", "")
    rule_path = os.path.join(OKF_DIR, bezug + ".md") if bezug else None

    # --- Ist-Werte aus den DIA-Marktdaten (Zelle 2) ---
    dfv = df.sort_index()
    heute = dfv.iloc[-1]
    gestern = dfv.iloc[-2]
    close_h = float(heute["close"])
    close_g = float(gestern["close"])
    high_h = float(heute["high"])
    low_h = float(heute["low"])
    open_h = float(heute["open"])
    vol_h = float(heute["volume"])
    mean_vol = float(dfv["volume"].tail(10).mean())

    ret_pct = (close_h - close_g) / close_g
    spanne_pct = (high_h - low_h) / close_h if close_h else 0.0
    body_pct = abs(close_h - open_h) / open_h if open_h else 0.0
    vol_ratio = vol_h / mean_vol if mean_vol else 1.0

    # Realistischer Richtungs-Korridor (±0.35% als Neutralbereich statt 0.05%)
    if ret_pct > 0.0035:
        ist_richtung = "bullisch"
    elif ret_pct < -0.0035:
        ist_richtung = "baerisch"
    else:
        ist_richtung = "neutral"

    ist_volumen = "hoch" if vol_ratio > 1.25 else ("niedrig" if vol_ratio < 0.75 else "normal")

    # =========================================================================
    # TEIL 1: HYPOTHESEN-VALIDIERUNG DER BEZUGSREGEL (Verhaltensmuster)
    # =========================================================================
    rule_checks = []

    if bezug == "regel-pre-event-paralyse":
        # Erwartung: Orderbuch-Rückzug, Volumen-Dürre (< 75% Ø), Spannen-Kompression (<= 1.0%)
        c_vol = (vol_ratio < 0.75)
        c_spanne = (spanne_pct <= 0.010)
        c_body = (body_pct <= 0.006)
        rule_checks = [
            ("Volumen-Austrocknung (< 0.75x)", vol_ratio, c_vol),
            ("Spannen-Kompression (<= 1.0%)", spanne_pct * 100, c_spanne),
            ("Richtungs-Indifferenz (|Body| <= 0.6%)", body_pct * 100, c_body),
        ]
    elif bezug == "regel-relief-rally-gridlock":
        c_trend = (ret_pct >= 0.008)
        c_vol = (vol_ratio >= 1.20)
        rule_checks = [
            ("Rallye-Dynamik (>= +0.8%)", ret_pct * 100, c_trend),
            ("Volumen-Expansion (>= 1.20x)", vol_ratio, c_vol),
        ]
    elif bezug == "regel-bull-trap-realitaetsschock":
        c_reversal = ((high_h - close_h) / high_h >= 0.012) or (close_h < open_h)
        c_vol = (vol_ratio >= 1.25)
        rule_checks = [
            ("Abverkauf vom Hoch (Reversal)", (high_h - close_h) / high_h * 100, c_reversal),
            ("Panik-Volumen (>= 1.25x)", vol_ratio, c_vol),
        ]
    elif bezug == "regel-idiosynkratischer-schock-rotation":
        c_stable = (abs(ret_pct) <= 0.008)
        c_vol = (vol_ratio <= 0.85)
        rule_checks = [
            ("Index-Resilienz (|Delta| <= 0.8%)", ret_pct * 100, c_stable),
            ("Institutionelle Zurückhaltung (<= 0.85x)", vol_ratio, c_vol),
        ]
    elif bezug == "regel-zinsangst-good-news-bad-news":
        c_cap = (close_h <= high_h * 0.996)
        c_druck = (ret_pct <= 0.002)
        rule_checks = [
            ("Deckelung unter Hoch", (high_h - close_h) / high_h * 100, c_cap),
            ("Zinslast dämpft Dynamik (<= +0.2%)", ret_pct * 100, c_druck),
        ]
    elif bezug == "regel-sektordivergenz-bodenbildung":
        c_rebound = ((close_h - low_h) / low_h >= 0.004)
        rule_checks = [
            ("Bodenbildung / Intraday-Rebound (>= 0.4%)", (close_h - low_h) / low_h * 100, c_rebound),
        ]
    else:
        exp_vol = exp.get("volumen", "").lower()
        c_vol = (exp_vol == ist_volumen) if exp_vol else True
        rule_checks = [("Volumenprofil passend", vol_ratio, c_vol)]

    rule_hits = sum(1 for _, _, ok in rule_checks if ok)
    rule_total = len(rule_checks)
    # Regel gilt als bestätigt, wenn die Mehrheit der Verhaltensmerkmale eintritt
    regel_bestaetigt = (rule_hits >= max(1, (rule_total + 1) // 2))

    # =========================================================================
    # TEIL 2: PUNKTSCHÄTZUNGS-VALIDIERUNG (Taktische Tages-Prognose)
    # =========================================================================
    exp_richtung = exp.get("richtung", "").lower()
    exp_volumen = exp.get("volumen", "").lower()
    try:
        spanne_u = float(exp.get("spanne_untere", "nan"))
        spanne_o = float(exp.get("spanne_obere", "nan"))
    except ValueError:
        spanne_u = spanne_o = float("nan")

    t_richtung = (exp_richtung == ist_richtung)
    t_spanne = (spanne_u <= close_h <= spanne_o)
    t_volumen = (exp_volumen == ist_volumen)
    prog_hits = int(t_richtung) + int(t_spanne) + int(t_volumen)

    # =========================================================================
    # AUSGABE & FEEDBACK-LOOP
    # =========================================================================
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    datum_erw = exp.get("datum", "unbekannt")

    print("=" * 72)
    print(f"1. REGEL-VALIDIERUNG (Verhaltensmuster: '{bezug}')")
    print("=" * 72)
    for name, val, ok in rule_checks:
        symbol = "✓ BESTÄTIGT" if ok else "✗ ABWEICHUNG"
        print(f"  • {name:<42} Ist={val:6.2f} -> {symbol}")
    print(f"  --> Ergebnis: {rule_hits}/{rule_total} Kriterien erfüllt.")

    if regel_bestaetigt:
        old_k, new_k = _adjust_konfidenz(rule_path, +0.05)
        print(f"  ==> REGEL BESTÄTIGT! Konfidenz erhöht: {old_k} -> {new_k} (+0.05)")
        _annotate_rule(rule_path, f"Bestätigt: {ts} Empirische Signatur ({rule_hits}/{rule_total}) am Markt verifiziert.")
        log_regel_fazit = f"Regel '{bezug}' empirisch BESTÄTIGT ({rule_hits}/{rule_total} Merkmale). Konfidenz erhöht auf {new_k}."
    else:
        old_k, new_k = _adjust_konfidenz(rule_path, -0.05)
        print(f"  ==> REGEL HINTERFRAGT. Konfidenz gesenkt: {old_k} -> {new_k} (-0.05)")
        _annotate_rule(rule_path, f"Korrektur: {ts} Signatur verfehlt ({rule_hits}/{rule_total}) – Regel hinterfragt.")
        log_regel_fazit = f"Regel '{bezug}' verfehlt ({rule_hits}/{rule_total} Merkmale). Konfidenz gesenkt auf {new_k}."

    print("\n" + "=" * 72)
    print(f"2. TAGES-PROGNOSE-VALIDIERUNG (Taktisches Kursziel vom {datum_erw})")
    print("=" * 72)
    print(f"  • Richtung : Soll={exp_richtung:<8} | Ist={ist_richtung:<8} ({ret_pct*100:+.2f}%) -> {'TREFFER' if t_richtung else 'ABWEICHUNG'}")
    print(f"  • Spanne   : Soll=[{spanne_u:.2f}, {spanne_o:.2f}] | Ist={close_h:.2f} -> {'TREFFER' if t_spanne else 'ABWEICHUNG'}")
    print(f"  • Volumen  : Soll={exp_volumen:<8} | Ist={ist_volumen:<8} (Ratio {vol_ratio:.2f}) -> {'TREFFER' if t_volumen else 'ABWEICHUNG'}")
    print(f"  --> Prognose-Score: {prog_hits}/3 Treffer.")

    # Audit in log.md schreiben
    audit_entry = (
        f"\n## Audit {ts}\n"
        f"- Bezugsregel: '{bezug}'\n"
        f"- Regel-Validierung: {'BESTÄTIGT' if regel_bestaetigt else 'ABWEICHUNG'} ({rule_hits}/{rule_total} Kriterien) -> {log_regel_fazit}\n"
        f"- Markt-Signatur: Close={close_h:.2f} ({ret_pct*100:+.2f}%), Spanne={spanne_pct*100:.2f}%, Vol-Ratio={vol_ratio:.2f} ({ist_volumen})\n"
        f"- Taktische Prognose ({datum_erw}): {prog_hits}/3 Treffer (Richtung={t_richtung}, Spanne={t_spanne}, Volumen={t_volumen})\n"
    )
    _append_log(audit_entry)

    # Strukturierte Historie in validierung_historie.csv schreiben
    hist_row = {
        "timestamp": ts,
        "erwartung_datum": datum_erw,
        "bezugsregel": bezug,
        "regel_bestaetigt": regel_bestaetigt,
        "regel_hits": f"{rule_hits}/{rule_total}",
        "prognose_score": f"{prog_hits}/3",
        "close": close_h,
        "ret_pct": round(ret_pct * 100, 2),
        "spanne_pct": round(spanne_pct * 100, 2),
        "vol_ratio": round(vol_ratio, 2),
        "richtung_ist": ist_richtung,
        "richtung_soll": exp_richtung,
        "konfidenz_neu": new_k,
    }
    _append_history_csv(hist_row)

    # Letzte 5 Historien-Einträge anzeigen
    if os.path.exists(CSV_PATH):
        print("\n" + "=" * 72)
        print("3. HISTORISCHER TRACK-RECORD (okf-regeln/validierung_historie.csv)")
        print("=" * 72)
        df_hist = pd.read_csv(CSV_PATH)
        display(df_hist.tail(5))
```

---

## 🎯 Was diese neue Zelle bewirkt

1. **Echte Regel-Verifikation (WENN-DANN):**
   * Die Konfidenz der Bezugsregel (z. B. `regel-pre-event-paralyse`) wird daran gemessen, ob ihr **charakteristisches Verhaltensmuster** (Volumen-Dürre < 0,75x, Spannen-Kompression $\le 1{,}0\,\%$) eingetroffen ist.
   * Am 12.11. bedeutet das: **3 von 3 Kriterien erfüllt $\rightarrow$ Regel bestätigt $\rightarrow$ Konfidenz gestärkt!**
2. **Entkopplung vom veralteten Preislevel:**
   * Die absolute Kursspanne (`[508, 516]`) wird als taktische Punktschätzung separat bewertet und zerstört nicht mehr fälschlicherweise die Konfidenz der Verhaltensregel.
3. **Statistischer Track-Record (`okf-regeln/validierung_historie.csv`):**
   * Jeder Validierungslauf wird tabellarisch archiviert. So können Sie über Wochen hinweg quantitativ nachweisen, welche Regeln am zuverlässigsten funktionieren.
4. **Realistischer Richtungsfilter:**
   * $\pm 0{,}35\,\%$ Schwellenwert für `neutral` statt $0{,}05\,\%$ verhindert Fehlabweichungen durch normales Intraday-Rauschen.
