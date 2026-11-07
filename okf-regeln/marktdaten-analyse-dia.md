---
type: "Empirical Analysis"
title: "Empirische Marktdaten-Analyse: SPDR Dow Jones Industrial Average ETF (DIA)"
description: "Quantitative Analyse der 10-Tages-Handelsdaten des DIA-ETF (2026-10-26 bis 2026-11-06) als Proxy für den DJIA zur Korrelation mit menschlichen Verhaltensnarrativen."
generated:
  by: "process:antigravity"
  at: "2026-11-07T06:05:00Z"
sources:
  - id: "dia-market-data"
    description: "DJIA / DIA ETF 10-Tages-OHLCV-Marktdaten (2026-10-26 bis 2026-11-06)"
  - id: "news-briefings-2026-11"
    description: "Börsen-Nachrichten Börse Stuttgart / Dow Jones Newswires (2026-11-02 bis 2026-11-06)"
tags:
  - marktdaten
  - djia
  - dia-etf
  - volatilitaet
  - liquiditaet
  - verhaltensanalyse
---

# Empirische Marktdaten-Analyse: DJIA / DIA ETF (26.10. – 06.11.2026)

Zur Fundierung der verhaltensökonomischen Regeln werden die 10 Handelstage des **SPDR Dow Jones Industrial Average ETF Trust (DIA)** als Proxy für den Leitindex Dow Jones Industrial Average (DJIA) quantitativ ausgewertet [^dia-market-data].

---

## 1. Rohdaten & Statistische Kennzahlen

| Datum | Open | High | Low | Close | Close-to-Close (%) | Open-to-Close (%) | Handelsspanne (Pkt / %) | Gap (%) | Handelsvolumen | Rel. Volumen (vs. Ø) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2026-10-26** | 523,89 | 525,61 | 521,94 | 522,97 | — | -0,18 % | 3,67 (0,70 %) | — | 2.338.671 | 0,55x |
| **2026-10-27** | 523,14 | 524,26 | 521,72 | 523,28 | +0,06 % | +0,03 % | 2,54 (0,49 %) | +0,03 % | 2.716.227 | 0,64x |
| **2026-10-28** | 522,98 | 525,77 | 522,80 | 524,68 | +0,27 % | +0,33 % | 2,97 (0,57 %) | -0,06 % | 2.823.905 | 0,66x |
| **2026-10-29** | 522,96 | 523,46 | 520,80 | 522,73 | -0,37 % | -0,04 % | 2,66 (0,51 %) | -0,33 % | 2.973.848 | 0,70x |
| **2026-10-30** | 521,85 | 522,02 | 515,01 | 517,13 | -1,07 % | -0,90 % | 7,01 (1,34 %) | -0,17 % | 4.871.953 | 1,14x |
| **2026-11-02** | 520,89 | 523,68 | 519,19 | 519,34 | +0,43 % | -0,30 % | 4,49 (0,86 %) | +0,73 % | 3.406.370 | 0,80x |
| **2026-11-03** | 517,06 | 518,38 | 515,19 | 517,06 | -0,44 % | 0,00 % | 3,19 (0,62 %) | -0,44 % | 3.177.824 | 0,75x |
| **2026-11-04** | 527,81 | 534,28 | 527,02 | 533,11 | +3,10 % | +1,00 % | 7,26 (1,38 %) | +2,08 % | 6.599.418 | 1,55x |
| **2026-11-05** | 535,95 | 536,60 | 514,13 | 514,27 | -3,53 % | -4,05 % | 22,47 (4,19 %) | +0,53 % | 11.448.063 | 2,69x |
| **2026-11-06** | 508,72 | 515,98 | 508,66 | 512,22 | -0,40 % | +0,69 % | 7,32 (1,44 %) | -1,08 % | 4.010.171 | 0,94x |

*Hinweis: Der 10-Tages-Durchschnitt des Handelsvolumens liegt bei rund 4.236.645 Anteilen [^dia-market-data].*

---

## 2. Marktphasen & Regimewechsel

### Phase 1: Vor-Ereignis-Kompression & Risikoaversion (26.10. – 03.11.)
* **Charakteristik**: Äußerst enge Tagesspannen von durchschnittlich 0,5 % bis 0,8 % und unterdurchschnittliches Volumen (2,3 bis 3,4 Mio. Anteile).
* **Verhaltenskorrelat**: Institutionelle Anleger drosseln Aktivitäten im Vorfeld der US-Zwischenwahlen (Midterms) drastisch [^news-briefings-2026-11]. Am Wahltag (03.11.) ist der Kursverlauf wie eingefroren: Eröffnung und Schlusskurs liegen exakt bei 517,06.
* **Konzepte**: Siehe [`regel-pre-event-paralyse`](regel-pre-event-paralyse.md).

### Phase 2: Die Entlastungsrallye (04.11.)
* **Charakteristik**: Eröffnungs-Gap von +2,08 % (von 517,06 auf 527,81), gefolgt von einem dynamischen Intraday-Anstieg auf 533,11 (+3,10 % Schluss-zu-Schluss). Das Handelsvolumen steigt sprunghaft auf das 1,55-fache des Schnitts an.
* **Verhaltenskorrelat**: Der Sieg der Demokraten im Kongress wird als "Befreiungsschlag" und Beginn eines stabilisierenden politischen Patts ("Gridlock") gefeiert [^news-briefings-2026-11].
* **Konzepte**: Siehe [`regel-relief-rally-gridlock`](regel-relief-rally-gridlock.md).

### Phase 3: Der Kapitulations-Reversal-Tag / Bull Trap (05.11.)
* **Charakteristik**: Neuer Höchststand bei 536,60 im frühen Handel, gefolgt von einem beispiellosen Intraday-Crash um 22,47 Punkte (-4,19 % Open-to-Close).
* **Volumen-Anomalie**: 11.448.063 Kontrakte — das 2,69-fache des 10-Tage-Durchschnitts und das 4,9-fache der Ruhigphase.
* **Verhaltenskorrelat**: Kaskade aus Gewinnwarnungen (Rheinmetall, BMW, Chipentwickler) und jähes Erwachen hinsichtlich demokratischer Regulierungspläne für KI-Infrastruktur und Rechenzentren [^news-briefings-2026-11].
* **Konzepte**: Siehe [`regel-bull-trap-realitaetsschock`](regel-bull-trap-realitaetsschock.md).

### Phase 4: Zinsangst & sektorale Aufspaltung (06.11.)
* **Charakteristik**: Starkes Abwärts-Gap auf 508,72 (-1,08 %). Während Technologiewerte im Tagesverlauf akkumuliert werden (Nasdaq +1,35 %), bleibt der DIA mit 512,22 im Minus (-0,40 %).
* **Verhaltenskorrelat**: Solide US-Arbeitsmarktdaten schüren Zinsfurcht vor der Dezember-Sitzung der Fed unter Kevin Warsh [^news-briefings-2026-11].
* **Konzepte**: Siehe [`regel-zinsangst-good-news-bad-news`](regel-zinsangst-good-news-bad-news.md) und [`regel-sektordivergenz-bodenbildung`](regel-sektordivergenz-bodenbildung.md).

---

## 3. Provenienz

[^dia-market-data]: Datensatz SPDR Dow Jones Industrial Average ETF Trust (DIA), 10-Tages-Zeitreihe Daily OHLCV vom 26.10.2026 bis 06.11.2026.
[^news-briefings-2026-11]: Morning Briefings und Schlusspanels der Börse Stuttgart / Dow Jones Newswires vom 02.11.2026 bis 06.11.2026.
