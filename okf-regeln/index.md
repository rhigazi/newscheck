---
okf_version: "0.2"
title: "OKF-Wissensbasis: Verhaltensökonomische Regeln & DJIA-Marktdynamik"
description: "Wissensbasis gemäß Open Knowledge Format (OKF) v0.2 zur Identifikation, Klassifikation und Handlungssynthese menschlicher Verhaltensnarrative am Aktienmarkt anhand des DJIA (DIA-Proxy)."
---

# OKF-Wissensbasis: Verhaltensnarrative und DJIA-Dynamik (Herbst 2026)

Diese Wissensbasis synthetisiert die Wechselwirkungen zwischen menschlichen Verhaltensnarrativen (z. B. Ungewissheit, Panik, Zinsangst, Erwartungshaltungen) in den Finanznachrichten und den empirischen Kursdaten des Dow Jones Industrial Average (DJIA), abgebildet über den Leit-ETF **SPDR Dow Jones Industrial Average ETF Trust (DIA)**.

Die Struktur folgt den Vorgaben des [Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md).

---

## Inhaltsverzeichnis und Kernkonzepte

### 1. Empirische Marktdatenbasis
* [`marktdaten-analyse-dia`](marktdaten-analyse-dia.md): Detaillierte quantitative Analyse der 10 Handelstage vom 26.10.2026 bis 06.11.2026 (OHLCV, Volatilitätsregime, Gaps, Volumen-Z-Scores und Reversal-Metriken).

### 2. Synthetisierte Verhaltensregeln
* [`regel-pre-event-paralyse`](regel-pre-event-paralyse.md): **Regel 1** – Ungewissheits-Paralyse und Volatilitätskompression vor binären Großereignissen (US-Midterms / Notenbanktage).
* [`regel-relief-rally-gridlock`](regel-relief-rally-gridlock.md): **Regel 2** – Post-Event Relief Rally und Gridlock-Illusion (De-Hedging und falsche Sicherheit politischer Lähmung).
* [`regel-bull-trap-realitaetsschock`](regel-bull-trap-realitaetsschock.md): **Regel 3** – Bull Trap, kaskadierender Realitätsschock und Panik-Liquidation (Guidance-Senkungen und KI-Regulierungsangst unter Rekordvolumen).
* [`regel-zinsangst-good-news-bad-news`](regel-zinsangst-good-news-bad-news.md): **Regel 4** – Zinsangst und das „Good News is Bad News“-Dilemma (Hawkish Fed unter angebotsseitigem Inflationsdruck).
* [`regel-sektordivergenz-bodenbildung`](regel-sektordivergenz-bodenbildung.md): **Regel 5** – Asymmetrische Panik-Absorption und selektives Dip-Buying (Tech-Rebound versus Industrie-Trägheit).

### 3. Übergreifende Synthese & Entscheidungsmodell
* [`synthese-verhaltensregeln`](synthese-verhaltensregeln.md): Ganzheitlicher Verhaltenszyklus, Phasenmodell, vergleichende Regel-Matrix und algorithmische Handlungsanweisungen für Marktteilnehmer.

---

## Verhaltensmatrix im Überblick

| Datum | Verhaltensnarrativ in den Nachrichten | DJIA / DIA Kursreaktion | Dominantes psychologisches Phänomen | Zugehörige OKF-Regel |
| :--- | :--- | :--- | :--- | :--- |
| **02.11. - 03.11.** | Institutionelles Abwarten, Vorsicht vor US-Midterms, Anthropic-Ramsch-Rating-Befürchtung | Stagnation bei 517–519 Punkten, Spanne schrumpft auf 0,62 %, Volumen sinkt | Risikoaversion, Entscheidungsaufschub, Ungewissheits-Paralyse | [`regel-pre-event-paralyse`](regel-pre-event-paralyse.md) |
| **04.11.** | Wahlsieg der Demokraten, "klare Verhältnisse", Hoffnung auf politischen Gridlock, fallende Ölpreise | Gap-Up (+2,08 %), Tagesgewinn +3,10 % (533,11), Volumen verdoppelt (6,6 Mio.) | Relief Rally, De-Hedging-Kaskade, kognitive Dissonanz (Gridlock-Illusion) | [`regel-relief-rally-gridlock`](regel-relief-rally-gridlock.md) |
| **05.11.** | Panik vor KI-Regulierung (Rechenzentren), Rheinmetall- & BMW-Gewinnwarnungen, Halbleiter-Ausverkauf | Eröffnungshoch 536,60, Intraday-Crash um 22,47 Pkt. auf 514,27, Rekordvolumen 11,45 Mio. | Bull Trap, Schock-Ernüchterung, Panik-Liquidation (Capitulation) | [`regel-bull-trap-realitaetsschock`](regel-bull-trap-realitaetsschock.md) |
| **06.11.** | Starker US-Arbeitsmarkt (+59k) schürt Fed-Zinsangst für Dezember (Warsh-Hawkishness), Iran-Kriegs-Ölpreis | Eröffnungs-Gap Down (508,72), Schluss 512,22 (-0,40 %), Dow bleibt unter Druck | "Good News is Bad News", Diskontierungs-Angst, Makro-Dominanz | [`regel-zinsangst-good-news-bad-news`](regel-zinsangst-good-news-bad-news.md) |
| **06.11. Schluss** | Schnäppchenjagd im Halbleitersektor (AMD +10 %, Lam +8 %, Nvidia +3 %), KI-Zyklus intakt | Tech erholt (+1,35 %), Dow Jones verharrt im Minus (-0,46 %) | Asymmetrisches Dip-Buying, Sektordivergenz, selektive Gier | [`regel-sektordivergenz-bodenbildung`](regel-sektordivergenz-bodenbildung.md) |

---

## Revisionshistorie

* Siehe [`log.md`](log.md) für die chronologische Dokumentation aller Änderungen und Syntheseschritte.
