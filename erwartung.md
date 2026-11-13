---
okf_version: "0.2"
typ: erwartung
datum: 2026-11-13
bezugsregel: regel-pre-event-paralyse
richtung: neutral
spanne_untere: 519.00
spanne_obere: 527.00
volumen: niedrig
konfidenz: 0.85
---

# Tagesaktuelle Marktprognose (Soll-Vorgabe) für den Handelstag 13.11.2026

Diese Prognose synthetisiert die jüngsten menschlichen Verhaltensnarrative aus den Finanznachrichten mit den quantitativen Marktdaten des Dow Jones Industrial Average (abgebildet über den **SPDR Dow Jones Industrial Average ETF Trust / DIA**) gemäß dem Open Knowledge Format (OKF) v0.2.

---

## 1. Übersicht & Soll-Parameter

| Parameter | Soll-Wert | Erläuterung & Begründung |
| :--- | :--- | :--- |
| **Gültigkeitsdatum** | `2026-11-13` | Handelstag Freitag, 13. November 2026 |
| **Tragende OKF-Regel** | [`regel-pre-event-paralyse`](okf-regeln/regel-pre-event-paralyse.md) | Vor-Ereignis-Paralyse und Volatilitätskompression vor den US-Erzeugerpreisen (PPI) und den anstehenden Nvidia-Quartalszahlen |
| **Erwartete Richtung** | `neutral` | Seitwärtskonsolidierung im bestehenden Wochenband um den Pivot 522,50 USD |
| **Kurskorridor (DIA)** | `519.00` bis `527.00` | Untere Begrenzung: Wochentief (519,19); Obere Begrenzung: Wochenhoch / Vortagshoch (527,05) |
| **Erwartetes Volumen** | `niedrig` | Ausdünnung der Orderbücher (< 3,13 Mio. Anteile, d. h. < 0,70x des 10-Tages-Schnitts von 4,48 Mio.) |
| **Modell-Konfidenz** | `0.85` | Hohe statistische Evidenz für Zurückhaltung vor binären Makrodaten am Wochenschluss |

---

## 2. Ausgangslage & Marktrecap (Handelstag 12.11.2026)

Am gestrigen Donnerstag zeigte der Markt eine bemerkenswerte Entkopplung zwischen Einzelschock und Indexstabilität:
1. **Kursentwicklung DIA**:
   * Eröffnung bei **524,38** (knapp unter dem Vortagsschluss von 524,44).
   * Intraday-Anstieg auf ein Wochenhoch von **527,05**.
   * Tagestief bei **522,23** fing den zwischenzeitlichen Rücksetzer zuverlässig ab.
   * Schlusskurs bei **522,47** (-0,38 %; der Dow Jones Industrial Index schloss bei 52.297,09 Punkten mit -0,36 %).
2. **Volumen-Anomalie**:
   * Das Handelsvolumen des DIA brach auf **1.702.339 Anteile** ein. Dies entspricht lediglich **0,38x** des 10-Tages-Durchschnitts von 4,48 Mio. Anteilen und markiert das ausgeprägteste Liquiditätsvakuum des gesamten Monats.
3. **Dominierende Verhaltensnarrative**:
   * **Nvidia-Führungsschock & Binnen-Sektorrotation**: Der überraschende Rücktritt von Nvidia-Chef Jensen Huang führte zu zweistelligen Kursverlusten der Nvidia-Aktie im Frühhandel (< 150 USD, Schluss -4,2 %). Anleger reagierten jedoch nicht mit einer panikartigen Marktflucht, sondern mit einer Umschichtung in Peer-Substitute: AMD legte um +5,9 % zu, Broadcom um +5,5 %, während Tech-Schwergewichte (Alphabet, Amazon, Microsoft) den Gesamtmarkt stützten (siehe [`regel-idiosynkratischer-schock-rotation`](okf-regeln/regel-idiosynkratischer-schock-rotation.md)).
   * **Zinsdiskussion nach US-Verbraucherpreisen (CPI)**: Der am Dienstag vermeldete Anstieg der US-Verbraucherpreise um +0,4 % MoM (Kernrate +0,3 %) schürt an der Wall Street Spekulationen über eine Zinserhöhung um 50 Basispunkte durch die Federal Reserve unter Fed-Chef Kevin Warsh im Dezember (siehe [`regel-zinsangst-good-news-bad-news`](okf-regeln/regel-zinsangst-good-news-bad-news.md)).
   * **Geopolitische Mahnung**: Aussagen von US-Präsident Donald Trump auf Truth Social ("keine Vereinbarung mit dem Iran nötig") dämpften voreilige Friedenshoffnungen und hielten den Ölpreis (Brent bei 97–100 USD) als Inflationsfaktor im Fokus.

---

## 3. Auswertung der anstehenden Termine (termine.md)

Die Analyse der Wochenvorschau liefert für den heutigen Handelstag sowie den Wochenauftakt folgende Schlüsselimpulse:

### A. Freitag, 13. November 2026 (Unmittelbarer Prognosetag)
* **Konjunkturdaten**:
  * **14:30 MEZ USA: Erzeugerpreise (PPI) 10/26**:
    * Dies ist der **entscheidende Datenpunkt des heutigen Tages**. Nach dem über den Erwartungen liegenden Verbraucherpreisindex (CPI) am Dienstag blicken Marktteilnehmer nervös auf die Pipeline-Inflation der Produzenten.
    * Bestätigt der PPI den Inflationsdruck, verfestigt sich die Erwartung eines restriktiven 50-Bp-Zinsschritts im Dezember, was Kursavancen an der oberen Spanne (527.00) im Keim ersticken dürfte.
  * **10:00 MEZ FRA: IEA Monatsbericht Ölmarkt 11/26**:
    * Wichtige Orientierung für die globale Angebotssituation im Kontext des Iran-Kriegs.
  * **11:00 MEZ EUR: BIP Q3/26 (2. Veröffentlichung), Handelsbilanz 9/26, Beschäftigung Q3/26**:
    * Makroökonomische Leitplanken für die europäische Konjunktur; stützt die Zinsdifferenzüberlegungen.
  * *Weitere Daten*: Großhandelspreise Deutschland (08:00 MEZ), Verbraucherpreise Frankreich/Spanien/Polen.
* **Unternehmensberichte**:
  * 07:00 MEZ CHE: Richemont (Halbjahreszahlen – Luxusgüter-Indikator).
  * 07:00 MEZ ITA: Generali Group (Q3-Zahlen – Bestätigung des starken Versicherungstrends nach Allianz/Munich Re).
  * 07:15 MEZ AUT: AMS Osram (Q3-Zahlen – Zulieferer für Halbleiter/Sensorik).
  * 07:30 MEZ DEU: Bechtle (Q3-Zahlen – IT-Dienstleister).

### B. Ausblick auf die Folgewoche (KW 47 ab 16. November 2026)
* **Dienstag, 17. November 2026 (Das globale Schlüsselereignis)**:
  * **22:20 MEZ USA: Nvidia Corporation, Q3-Zahlen**:
    * Nach dem Rücktritt von Jensen Huang am 12.11. wird dieser Quartalsbericht zur Nagelprobe für die Bewertung des gesamten globalen KI-Hardwaresektors.
    * Vor diesem Härtetest ist eine defensive Haltung institutioneller Adressen am heutigen Freitag hochgradig plausibel.
  * 12:00 MEZ USA: Home Depot (Q3) & 12:45 MEZ USA: Walt Disney (Q4) – Relevante Dow-Jones-Indexkomponenten.
* **Montag, 16. November 2026**:
  * 03:00 MEZ CHN: Einzelhandelsumsatz & Industrieproduktion 10/26.
  * 14:30 MEZ USA: Empire State Index 11/26.

---

## 4. Verhaltensökonomische Begründung & Regeldokumentation

### Warum greift die Bezugsregel [`regel-pre-event-paralyse`](okf-regeln/regel-pre-event-paralyse.md)?
1. **Zweifache Ambiguity Aversion (Makro- und Micro-Katalysatoren)**:
   * **Makro**: Vor den US-Erzeugerpreisen (PPI) um 14:30 MEZ meiden Marktteilnehmer Richtungsengagements. Die Kombination aus heißem CPI vom Dienstag und anstehendem PPI erzeugt ein asymmetrisches Risiko: Ein hoher Wert zementiert Zinsängste, ein moderater Wert bringt vor dem Wochenende kaum nachhaltigen Kaufdruck.
   * **Micro**: Der Schock um den Rücktritt von Nvidia-CEO Jensen Huang ist zwar durch Sektorrotation aufgefangen worden (siehe [`regel-idiosynkratischer-schock-rotation`](okf-regeln/regel-idiosynkratischer-schock-rotation.md)), doch vor den offiziellen Quartalszahlen am kommenden Dienstag (17.11.) frieren Portfoliomanager größere Neuallokationen ein.
2. **Volumenkollaps als verlässlicher Indikator**:
   * Das DIA-Volumen von nur 1,70 Mio. Anteilen am Donnerstag belegt empirisch, dass große Adressen ihre Bücher vor dem heutigen Datenpunkt weitgehend geschlossen halten.
   * Am Freitag vor dem Wochenende wird sich dieser Trend fortsetzen; das Volumen wird im Regime **niedrig** (< 3,13 Mio. Anteile) verharren.
3. **Etablierung des Konsolidierungskorridors [519.00, 527.00]**:
   * **Untergrenze (519.00)**: Bei 519,19 fand der DIA bereits am Dienstag nach dem heißen CPI-Wert eine tragfähige Unterstützung. Solide Bilanzen (Siemens Rekord-Auftragseingang, Allianz/Munich Re Gewinnanhebungen) sichern Standardwerte nach unten ab.
   * **Obergrenze (527.00)**: Am gestrigen Donnerstag prallte der DIA exakt bei 527,05 nach unten ab. Die Zinsdebatte (Warsh-Falken-Rhetorik) deckelt das Aufwärtspotenzial verlässlich.
   * Der Markt verbleibt somit **neutral** im Gleichgewicht.

---

## 5. Handlungsanweisung für automatisierte Handels- und Analysesysteme

* **Kein Trendfolgemodus**: Signale für Ausbrüche über 527.00 oder unter 519.00 vor 14:30 MEZ sind mit hoher Wahrscheinlichkeit Fehlsignale (False Breakouts).
* **Orderbuch-Überwachung um 14:30 MEZ**: Bei Bekanntgabe der US-Erzeugerpreise ist mit kurzzeitigen Volatilitäts-Spikes zu rechnen; Positionen im DIA sollten mit Stop-Loss-Marken außerhalb des 519–527-Bandes geführt werden.
* **Fokus auf relative Stärke**: Sektorale Umschichtungen aus Halbleiter-Primärwerten in Peer-Substitute (AMD, Broadcom) oder defensive Qualitätsdividendenwerte weiter bevorzugen.
