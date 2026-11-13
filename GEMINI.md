# Newscheck Guidelines: Kausale Marktregeln & Verhaltensketten

Für alle Analysen, Synthesen, Code-Generierungen und Regeldefinitionen in diesem Repository (`newscheck`) gelten folgende verbindliche Richtlinien:

## 1. Abstraktion & Wiederverwendbarkeit (Keine Einzelfall-Fixierung)
* **Regelkern abstrahieren:** Formuliere niemals Marktregeln, die an spezifische Einzelpersonen (z. B. Vorstandsvorsitzende, Politiker), Firmennamen oder konkrete Datumsstände gebunden sind.
* **Funktionale Rollen:** Übersetze konkrete Meldungen stets in verallgemeinerbare Marktrollen (z. B. *„Sektor-Schwergewicht mit >15 % Indexgewicht“*, *„Zentralbank-Kommunikationsschock“*, *„Geopolitischer Angebotsengpass“*).

## 2. Kausale Ketten (WENN X in Sektor A -> Y; WENN Y und Z -> D1)
* Regeln müssen als modulare Ursache-Wirkungs-Ketten formuliert werden:
  1. **Primär-Impuls $X$** (z. B. Idiosynkratischer Schock, Inflationssprung)
  2. **Zwischenwirkung $Y$** (z. B. Intra-sektorale Substitution / Peer-Rotation, Liquiditätsrückzug)
  3. **Umgebungs-Regime $Z$** (z. B. Binäres Event-Ungewissheitsregime, restriktive Zinsphase)
  4. **Kausale Kettenreaktion $D_1$** (z. B. Index-Absorption bei Volatilitätskompression, Kaskadenausbruch)

## 3. Skill-Referenz
* Bei allen Aufgaben rund um die Erstellung oder Pflege von `okf-regeln/`, `erwartung.md` oder der Validierung in Zelle 4.5 ist der Skill **`market-causal-patterns`** (`.agents/skills/market-causal-patterns/SKILL.md`) maßgeblich.

## 4. Validierungs-Trennung (Zelle 4.5)
* Trenne stets die **empirische Verifikation der Kausalkette** (Volumenprofil, Spannenkompression, Sektor-Absorption) von der **taktischen Punktschätzung** (absolutes Kursniveau).
* Eine veraltete Preisspanne darf niemals eine funktionierende Kausalkette abwerten.
* Halte alle Ergebnisse transparent in `okf-regeln/validierung_historie.csv` fest.
