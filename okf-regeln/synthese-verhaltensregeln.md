---
type: "Synthesis"
title: "Gesamtsynthese: Verhaltensökonomisches Marktmodell und Regelsystem"
description: "Ganzheitliche Synthese der menschlichen Verhaltensnarrative, Marktphasen und abgeleiteten Handlungsregeln auf Basis der DJIA/DIA-Analysen Herbst 2026."
generated:
  by: "process:antigravity"
  at: "2026-11-13T03:50:55Z"
sources:
  - id: "dia-market-data"
    description: "DJIA / DIA ETF 10-Tages-OHLCV-Marktdaten (2026-10-30 bis 2026-11-12)"
  - id: "news-briefings-2026-11"
    description: "Börsen-Nachrichten Börse Stuttgart / Dow Jones Newswires (2026-11-02 bis 2026-11-13)"
  - id: "termine-preview"
    description: "Wochenvorschau Börse Stuttgart Termine bis 20. November 2026 (termine.md)"
tags:
  - behavioral-finance
  - synthese
  - entscheidungsmodell
  - marktzyklen
  - djia
  - okf-v02
---

# Gesamtsynthese: Verhaltensökonomisches Marktmodell und Regelsystem

---

## 1. Einordnung des Verhaltenszyklus (Herbst 2026)

Der untersuchte 10-Tages-Ausschnitt des DJIA (abgebildet über den **DIA-ETF** vom 30.10. bis 12.11.2026) liefert ein vollständiges Bild der marktpsychologischen Phasendynamik [^dia-market-data] [^news-briefings-2026-11]:

```mermaid
flowchart TD
    Phase1["1. Paralyse & Unsicherheit\n(30.10. - 03.11.)\nVolatilitätskompression vor Midterms\nDIA: Stagnation bei 517,06"]
    Phase2["2. Entlastungsrallye & Euphorie\n(04.11.)\nWahlergebnis steht fest, Gridlock-Illusion\nDIA: Gap-Up 527,81 -> Close 533,11 (+3,1 %)"]
    Phase3["3. Bull Trap & Panik-Liquidation\n(05.11.)\nGuidance-Cuts, KI-Regulierungsdrohung\nDIA: High 536,60 -> Low 514,13 (Volumen 11,45 Mio.)"]
    Phase4["4. Zinsangst & 'Good News Bad News'\n(06.11. - 10.11.)\nArbeitsmarkt & heiße CPI-Daten (+0,4 % MoM)\nFed-Zinserhöhungsfurcht deckelt DIA bei 522 USD"]
    Phase5["5. Asymmetrische Erholung & Zinsresilienz\n(09.11. - 11.11.)\nDesensibilisierung, starke Bilanzen (Siemens, Allianz)\nDIA klettert auf 524,44"]
    Phase6["6. Idiosynkratischer Schock & Binnen-Rotation\n(12.11.)\nHuang-Rücktritt bei Nvidia -> Shift in AMD/Broadcom\nDIA-Volumen fällt auf 1,70 Mio. (0,38x)"]

    Phase1 --> Phase2
    Phase2 --> Phase3
    Phase3 --> Phase4
    Phase4 --> Phase5
    Phase5 --> Phase6
    Phase6 -.->|Pre-Event Paralyse vor PPI & Nvidia-Q3| Phase1
```

---

## 2. Synopse der OKF-Verhaltensregeln

Die folgende Matrix konsolidiert die 6 erarbeiteten OKF-Konzepte in ein anwendbares Regelwerk für Handels- und Allokationsentscheidungen:

| OKF-Regel | Psychologischer Treiber | Empirische Signatur (DIA) | Volumenprofil | Zentrale Handlungsmaxime |
| :--- | :--- | :--- | :--- | :--- |
| [`regel-pre-event-paralyse`](regel-pre-event-paralyse.md) | **Ambiguity Aversion**: Angst vor unkalkulierbaren Richtungsentscheidungen | Handelsspanne < 0,7 %; Eröffnung ≈ Schluss (517,06 bzw. 521,73) | Stark unterdurchschnittlich (< 70 % des Mittels, z. B. 1,70 Mio.) | **Füße stillhalten**: Keine Ausbruchswetten im illiquiden Markt; Hedges nicht verfrüht auflösen. |
| [`regel-relief-rally-gridlock`](regel-relief-rally-gridlock.md) | **Certainty Relief & Gridlock Bias**: Verwechslung von Gewissheit mit Fundamentalkraft | Massives Gap-Up (+2,08 %), dynamischer Tagestrend (+3,10 %) | Sprunghafter Anstieg (> 140 % des Mittels, 6,6 Mio.) | **Gewinne realisieren**: Pre-Event-Hedges schließen, Longs in die Rallye reduzieren; FOMO-Käufe strikt meiden. |
| [`regel-bull-trap-realitaetsschock`](regel-bull-trap-realitaetsschock.md) | **Narrative Reversal & Climax Fear**: Schockartiger Zusammenbruch des Hypes | Neues Hoch am Morgen (536,60), dann vertikaler Absturz um 22,47 Pkt. | Extremer Rekord-Spike (256 % des Mittels, 11,45 Mio.) | **Notbremse ziehen**: Sofortiger Exit bei Fehlausbruch unter Vortageseröffnung; kein Hineingreifen in fallende Messer. |
| [`regel-zinsangst-good-news-bad-news`](regel-zinsangst-good-news-bad-news.md) | **Monetary Hawkishness**: Furcht vor Liquiditätsentzug überlagert Realwirtschaft | Abwärts-Gap (-1,08 %), Verharren unter Widerständen trotz starker Konjunkturdaten | Normal bis gedämpft (3,1 bis 4,2 Mio.) | **Makro-Kontext beachten**: Bei angebotsseitiger Inflation gute Daten nicht unreflektiert als Kaufsignal werten. |
| [`regel-sektordivergenz-bodenbildung`](regel-sektordivergenz-bodenbildung.md) | **Selective Anchoring & Dip-Buying**: Schnäppchenjagd in High-Beta-Wachstumswerten | Dow Jones / DIA verharrt im Minus, Tech schießt nach oben (+1,35 %) | Selektive Volumenbündelung in Chip- und KI-Werten | **Präzise Allokation**: Rebound-Trades nach Crash-Tagen nicht im breiten DIA, sondern gezielt bei abgestraften Leadern fahren. |
| [`regel-idiosynkratischer-schock-rotation`](regel-idiosynkratischer-schock-rotation.md) | **Idiosyncratic Substitution**: Trennung von Personenschock und Branchentrend | Nvidia bricht zweistellig ein, Peers (AMD, Broadcom) steigen um >5 %; DIA -0,38 % | Extremer Einbruch im Gesamtmarkt (1,70 Mio. Anteile, 0,38x) | **Kein Gesamtmarkt-Short**: Bei Governance-Schocks Umschichtung in Peer-Substitute nutzen; Markt-Austrocknung respektieren. |

---

## 3. Algorithmischer Entscheidungsbaum

```mermaid
graph TD
    Start["Eingehende Nachricht & Marktdaten"] --> Q1{"Steht ein Großevent < 24h an?\n(CPI/PPI, Zinsentscheid, Mega-Earnings)"}
    Q1 -- Ja --> Action1["Signal: PARALYSE\nKeine neuen Trendpositionen\nVolatilitätsexpansion antizipieren"]
    Q1 -- Nein --> Q2{"Großevent entschieden & Eröffnungs-Gap > 1,5 %?"}
    
    Q2 -- Ja --> Action2["Signal: RELIEF RALLY\nBestehende Longs hedgen / Gewinne sichern\nZeithorizont: max. 24-36h"]
    Q2 -- Nein --> Q3{"Neuhoch gefolgt von Guidance-Cut & Intraday-Crash?"}
    
    Q3 -- Ja --> Action3["Signal: BULL TRAP / PANIK\nSofortiger Ausstieg aus Long-Positionen\nAbsolutes Kaufverbot an Tag 1"]
    Q3 -- Nein --> Q4{"Personeller Einzelschock bei dominanter Leitaktie?"}
    
    Q4 -- Ja --> Action4["Signal: BINNEN-SEKTORROTATION\nKein Gesamtmarkt-Short\nKapitalzufluss in Peer-Substitute suchen"]
    Q4 -- Nein --> Q5{"Gute Konjunkturdaten bei hoher Inflation & Hawkish Fed?"}
    
    Q5 -- Ja --> Action5["Signal: ZINSANGST\nStandardwerte / Dividendenaktien untergewichten"]
    Q5 -- Nein --> Action6["Signal: SEKTORDIVERGENZ\nSelektive Akkumulation überverkaufter High-Beta-Titel"]
```

---

## 4. Fazit und Systemnutzen

Durch die Synthese in standardkonforme OKF v0.2 Einheiten steht dem System ein robustes, portables Regelwerk zur Verfügung. Statt Kursbewegungen rein isoliert-technisch oder Nachrichten rein qualitativ zu betrachten, verknüpft das vorliegende Modell die **Ursache-Wirkungs-Beziehung zwischen menschlichem Massenverhalten und tatsächlicher Orderbuchliquidität**.

---

## 5. Provenienz

[^dia-market-data]: Vollständige 10-Tages-Reihe DIA ETF (30.10. – 12.11.2026), analysiert in [`marktdaten-analyse-dia`](marktdaten-analyse-dia.md).
[^news-briefings-2026-11]: Archivierte Morning Briefings der Börse Stuttgart / Dow Jones Newswires (02.11. – 13.11.2026).
[^termine-preview]: Wochenvorschau Termine bis 20. November 2026 (`termine.md`).
