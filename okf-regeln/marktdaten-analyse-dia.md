---
type: "Empirical Analysis"
title: "Empirische Marktdaten-Analyse: SPDR Dow Jones Industrial Average ETF (DIA)"
description: "Quantitative Analyse der 10-Tages-Handelsdaten des DIA-ETF (2026-10-30 bis 2026-11-12) als Proxy für den DJIA zur Korrelation mit menschlichen Verhaltensnarrativen."
generated:
  by: "process:antigravity"
  at: "2026-11-13T03:50:55Z"
sources:
  - id: "dia-market-data"
    description: "DJIA / DIA ETF 10-Tages-OHLCV-Marktdaten (2026-10-30 bis 2026-11-12)"
  - id: "news-briefings-2026-11"
    description: "Börsen-Nachrichten Börse Stuttgart / Dow Jones Newswires (2026-11-09 bis 2026-11-13)"
  - id: "termine-preview"
    description: "Wochenvorschau Börse Stuttgart Termine bis 20. November 2026 (termine.md)"
tags:
  - marktdaten
  - djia
  - dia-etf
  - volatilitaet
  - liquiditaet
  - verhaltensanalyse
  - sektorrotation
---

# Empirische Marktdaten-Analyse: DJIA / DIA ETF (30.10. – 12.11.2026)

Zur empirischen Fundierung der verhaltensökonomischen Regeln werden die jüngsten 10 Handelstage des **SPDR Dow Jones Industrial Average ETF Trust (DIA)** als Proxy für den Leitindex Dow Jones Industrial Average (DJIA) quantitativ ausgewertet [^dia-market-data].

---

## 1. Rohdaten & Statistische Kennzahlen

| Datum | Open | High | Low | Close | Close-to-Close (%) | Open-to-Close (%) | Handelsspanne (Pkt / %) | Gap (%) | Handelsvolumen | Rel. Volumen (vs. Ø) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2026-10-30** | 521,85 | 522,02 | 515,01 | 517,13 | — | -0,90 % | 7,01 (1,36 %) | — | 4.871.953 | 1,09x |
| **2026-11-02** | 520,89 | 523,68 | 519,19 | 519,34 | +0,43 % | -0,30 % | 4,49 (0,86 %) | +0,73 % | 3.406.370 | 0,76x |
| **2026-11-03** | 517,06 | 518,38 | 515,19 | 517,06 | -0,44 % | 0,00 % | 3,19 (0,62 %) | -0,44 % | 3.177.824 | 0,71x |
| **2026-11-04** | 527,81 | 534,28 | 527,02 | 533,11 | +3,10 % | +1,00 % | 7,26 (1,36 %) | +2,08 % | 6.599.418 | 1,47x |
| **2026-11-05** | 535,95 | 536,60 | 514,13 | 514,27 | -3,53 % | -4,05 % | 22,47 (4,37 %) | +0,53 % | 11.448.063 | 2,56x |
| **2026-11-06** | 508,72 | 515,98 | 508,66 | 512,22 | -0,40 % | +0,69 % | 7,32 (1,43 %) | -1,08 % | 4.284.351 | 0,96x |
| **2026-11-09** | 518,55 | 525,17 | 517,24 | 523,33 | +2,17 % | +0,92 % | 7,93 (1,52 %) | +1,24 % | 3.459.825 | 0,77x |
| **2026-11-10** | 521,51 | 522,60 | 519,19 | 521,73 | -0,31 % | +0,04 % | 3,41 (0,65 %) | -0,35 % | 3.115.419 | 0,70x |
| **2026-11-11** | 522,79 | 524,63 | 520,05 | 524,44 | +0,52 % | +0,32 % | 4,58 (0,87 %) | +0,20 % | 2.714.253 | 0,61x |
| **2026-11-12** | 524,38 | 527,05 | 522,23 | 522,47 | -0,38 % | -0,36 % | 4,82 (0,92 %) | -0,01 % | 1.702.339 | 0,38x |

*Statistischer 10-Tages-Durchschnitt des Handelsvolumens: **4.477.982 Anteile** [^dia-market-data].*

---

## 2. Marktphasen & Regimewechsel

### Phase 1: Vor-Ereignis-Kompression & Risikoaversion (30.10. – 03.11.)
* **Charakteristik**: Handelsspanne schrumpft auf ein Minimum von 3,19 Punkten (0,62 % am Wahltag 03.11.), Volumen sinkt kontinuierlich auf 3,18 Mio. Anteile (0,71x). Eröffnung und Schlusskurs am 03.11. liegen exakt gleichauf bei 517,06.
* **Verhaltenskorrelat**: Ungewissheits-Paralyse vor den US-Zwischenwahlen (Midterms).
* **Konzept**: Siehe [`regel-pre-event-paralyse`](regel-pre-event-paralyse.md).

### Phase 2: Die Entlastungsrallye (04.11.)
* **Charakteristik**: Eröffnungs-Gap von +2,08 % auf 527,81, gefolgt von einer dynamischen Rallye auf 533,11 (+3,10 % Close-to-Close). Volumen expandiert auf 6,60 Mio. (1,47x).
* **Verhaltenskorrelat**: Erleichterung über das Wahlergebnis und die Illusion politischer Handlungsunfähigkeit ("Gridlock-Mythos").
* **Konzept**: Siehe [`regel-relief-rally-gridlock`](regel-relief-rally-gridlock.md).

### Phase 3: Bull Trap & Panik-Liquidation (05.11.)
* **Charakteristik**: Bullenfalle mit Allzeithoch-Test bei 536,60 im Frühhandel, gefolgt von einem brutalen Intraday-Crash um 22,47 Punkte (-4,05 % Open-to-Close) auf 514,27.
* **Volumen-Explosion**: 11.448.063 Anteile — das 2,56-fache des Schnitts.
* **Verhaltenskorrelat**: Schockartige Konfrontation mit KI-Regulierungsdrohungen und Gewinnwarnungen der Realwirtschaft (BMW, Rheinmetall).
* **Konzept**: Siehe [`regel-bull-trap-realitaetsschock`](regel-bull-trap-realitaetsschock.md).

### Phase 4: Zinsangst & asymmetrische Panik-Absorption (06.11.)
* **Charakteristik**: Gap Down auf 508,72 (-1,08 %), gefolgt von einer schwachen Erholung auf 512,22 (-0,40 %).
* **Verhaltenskorrelat**: Solide US-Arbeitsmarktdaten schüren Leitzinserhöhungsfurcht vor Fed-Chef Kevin Warsh ("Good News is Bad News"), während Tech-Werte bereits selektiv akkumuliert werden.
* **Konzepte**: Siehe [`regel-zinsangst-good-news-bad-news`](regel-zinsangst-good-news-bad-news.md) und [`regel-sektordivergenz-bodenbildung`](regel-sektordivergenz-bodenbildung.md).

### Phase 5: Rebound, CPI-Zinsabsorption & Konsolidierung (09.11. – 11.11.)
* **Charakteristik**: Dynamischer Rebound am 09.11. mit Gap-Up auf 518,55 und Schluss bei 523,33 (+2,17 %). Am 10.11. preist der Markt die über den Erwartungen liegenden US-Verbraucherpreise (+0,4 % MoM) in einer engen Spanne von nur 3,41 Punkten (0,65 %) ein (Schluss 521,73). Am 11.11. (US-Feiertag Veterans Day) konsolidiert der DIA bei 524,44 unter fallendem Volumen (2,71 Mio.).
* **Verhaltenskorrelat**: Der Markt gewöhnt sich an die Zinsfalken-Rhetorik ("Desensibilisierung"), gestützt durch exzellente Unternehmensergebnisse (Infineon, Henkel, RWE, Siemens Energy).
* **Konzepte**: Siehe [`regel-pre-event-paralyse`](regel-pre-event-paralyse.md) und [`regel-zinsangst-good-news-bad-news`](regel-zinsangst-good-news-bad-news.md).

### Phase 6: Idiosynkratischer Schock & Binnen-Sektorrotation (12.11.)
* **Charakteristik**: Eröffnung bei 524,38, Hoch bei 527,05, gefolgt von Abgaben auf 522,47 (-0,38 %). Das Handelsvolumen bricht drastisch auf **1.702.339 Anteile (0,38x)** ein — der tiefste Wert des Betrachtungszeitraums.
* **Verhaltenskorrelat**: Der überraschende Rücktritt von Nvidia-CEO Jensen Huang löst zweistellige Verluste bei Nvidia aus (<150 USD). Statt einer Panik-Flucht aus dem Gesamtmarkt schichten institutionelle Anleger massiv in Konkurrenten wie AMD (+5,9 %) und Broadcom (+5,5 %) sowie Mega-Caps um. Gleichzeitig mahnt Trumps Erklärung zum Iran-Krieg zur Vorsicht, was das Gesamtvolumen vor dem US-Erzeugerpreisbericht am Freitag austrocknen lässt.
* **Konzept**: Siehe [`regel-idiosynkratischer-schock-rotation`](regel-idiosynkratischer-schock-rotation.md).

---

## 3. Provenienz

[^dia-market-data]: Datensatz SPDR Dow Jones Industrial Average ETF Trust (DIA), 10-Tages-Zeitreihe Daily OHLCV vom 30.10.2026 bis 12.11.2026.
[^news-briefings-2026-11]: Morning Briefings und Schlusspanels der Börse Stuttgart / Dow Jones Newswires vom 02.11.2026 bis 13.11.2026.
[^termine-preview]: Wochenvorschau Termine bis 20. November 2026 (`termine.md`).
