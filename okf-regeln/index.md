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
* [`marktdaten-analyse-dia`](marktdaten-analyse-dia.md): Detaillierte quantitative Analyse der 10 Handelstage vom 30.10.2026 bis 12.11.2026 (OHLCV, Volatilitätsregime, Gaps, Volumenprofile und Reversal-Metriken).

### 2. Synthetisierte Verhaltensregeln
* [`regel-pre-event-paralyse`](regel-pre-event-paralyse.md): **Regel 1** – Ungewissheits-Paralyse und Volatilitätskompression vor binären Großereignissen (Midterms, US-CPI/PPI, Earnings).
* [`regel-relief-rally-gridlock`](regel-relief-rally-gridlock.md): **Regel 2** – Post-Event Relief Rally und Gridlock-Illusion (De-Hedging und Entlastung nach Wahlen).
* [`regel-bull-trap-realitaetsschock`](regel-bull-trap-realitaetsschock.md): **Regel 3** – Bull Trap, kaskadierender Realitätsschock und Panik-Liquidation (Guidance-Cuts und KI-Regulierungsangst).
* [`regel-zinsangst-good-news-bad-news`](regel-zinsangst-good-news-bad-news.md): **Regel 4** – Zinsangst und das „Good News is Bad News“-Dilemma (Hawkish Fed unter anhaltendem Inflationsdruck).
* [`regel-sektordivergenz-bodenbildung`](regel-sektordivergenz-bodenbildung.md): **Regel 5** – Asymmetrische Panik-Absorption und selektives Dip-Buying (Tech-Rebound versus Industrie-Trägheit).
* [`regel-idiosynkratischer-schock-rotation`](regel-idiosynkratischer-schock-rotation.md): **Regel 6** – Idiosynkratischer Key-Person-Schock und Binnen-Sektorrotation (Huang-Rücktritt, Peer-Substitution und Volumenkompression).

### 3. Übergreifende Synthese & Entscheidungsmodell
* [`synthese-verhaltensregeln`](synthese-verhaltensregeln.md): Ganzheitlicher 6-Phasen-Verhaltenszyklus, vergleichende Regel-Matrix und algorithmischer Entscheidungsbaum für Marktteilnehmer.

### 4. Aktive Marktprognose (Soll-Vorgabe)
* [`erwartung`](../erwartung.md): Tagesaktuelle Soll-Prognose für den Handelstag 13.11.2026 vor den US-Erzeugerpreisen (PPI) und im Nachgang des Nvidia-Führungsschocks auf Basis von [`regel-pre-event-paralyse`](regel-pre-event-paralyse.md).

---

## Verhaltensmatrix im Überblick

| Datum | Verhaltensnarrativ in den Nachrichten | DJIA / DIA Kursreaktion | Dominantes psychologisches Phänomen | Zugehörige OKF-Regel |
| :--- | :--- | :--- | :--- | :--- |
| **02.11. - 03.11.** | Institutionelles Abwarten, Vorsicht vor US-Midterms | Stagnation bei 517–519 Punkten, Spanne schrumpft auf 0,62 %, Volumen sinkt | Risikoaversion, Entscheidungsaufschub, Ungewissheits-Paralyse | [`regel-pre-event-paralyse`](regel-pre-event-paralyse.md) |
| **04.11.** | Wahlsieg der Demokraten, "klare Verhältnisse", Hoffnung auf politischen Gridlock | Gap-Up (+2,08 %), Tagesgewinn +3,10 % (533,11), Volumen verdoppelt (6,6 Mio.) | Relief Rally, De-Hedging-Kaskade, kognitive Dissonanz (Gridlock-Illusion) | [`regel-relief-rally-gridlock`](regel-relief-rally-gridlock.md) |
| **05.11.** | Panik vor KI-Regulierung (Rechenzentren), Rheinmetall- & BMW-Gewinnwarnungen | Eröffnungshoch 536,60, Intraday-Crash um 22,47 Pkt. auf 514,27, Rekordvolumen 11,45 Mio. | Bull Trap, Schock-Ernüchterung, Panik-Liquidation (Capitulation) | [`regel-bull-trap-realitaetsschock`](regel-bull-trap-realitaetsschock.md) |
| **06.11.** | Starker US-Arbeitsmarkt (+59k) schürt Fed-Zinsangst für Dezember (Warsh-Hawkishness) | Eröffnungs-Gap Down (508,72), Schluss 512,22 (-0,40 %), Dow bleibt unter Druck | "Good News is Bad News", Diskontierungs-Angst, Makro-Dominanz | [`regel-zinsangst-good-news-bad-news`](regel-zinsangst-good-news-bad-news.md) |
| **09.11.** | Schreckreaktion eingepreist, kein KI-Crash, Erleichterungs-Rebound | Gap-Up (+1,24 %) auf 518,55, Schluss bei 523,33 (+2,17 %), Volumen normal (3,46 Mio.) | Erholungs-Zuversicht, Short-Covering | [`regel-sektordivergenz-bodenbildung`](regel-sektordivergenz-bodenbildung.md) |
| **10.11.** | US-CPI steigt über Erwartung (+0,4 % MoM), Spekulation über 50-Bp-Zinsschritt der Fed | Handelsspanne erstarrt auf 3,41 Pkt. (0,65 %), Schluss 521,73 (-0,31 %) | Zinsangst vs. Markt-Desensibilisierung, Pre-Event-Kompression | [`regel-pre-event-paralyse`](regel-pre-event-paralyse.md) / [`regel-zinsangst-good-news-bad-news`](regel-zinsangst-good-news-bad-news.md) |
| **11.11.** | Märkte stecken Zinssorgen weg, starke Bilanzen (Henkel, Infineon) stützen, Veterans Day | Leichter Anstieg auf 524,44 (+0,52 %), US-Anleihehandel ruht, Volumen gedämpft (2,71 Mio.) | Selektive Stärke, Zins-Resilienz | [`regel-zinsangst-good-news-bad-news`](regel-zinsangst-good-news-bad-news.md) |
| **12.11.** | Jensen Huang tritt als Nvidia-Chef zurück; massiver Shift in AMD (+5,9 %) & Broadcom (+5,5 %) | Hoch bei 527,05, Schluss 522,47 (-0,38 %), Volumen kollabiert auf 1,70 Mio. (0,38x) | Idiosynkratische Binnen-Sektorrotation & institutionelles Abwarten vor US-PPI | [`regel-idiosynkratischer-schock-rotation`](regel-idiosynkratischer-schock-rotation.md) |

---

## Revisionshistorie

* Siehe [`log.md`](log.md) für die chronologische Dokumentation aller Änderungen und Syntheseschritte.
