---
okf_version: "0.2"
typ: erwartung
datum: 2026-11-07
bezugsregel: regel-pre-event-paralyse
richtung: neutral
spanne_untere: 508.00
spanne_obere: 516.00
volumen: normal
konfidenz: 0.85
---

# Tagesaktuelle Marktprognose (Soll-Vorgabe) für den Handelstag 09.11.2026

Diese Prognose synthetisiert die Verhaltensnarrative der jüngsten Nachrichtenberichte mit den quantitativen Marktdaten des Dow Jones Industrial Average (abgebildet über den **SPDR Dow Jones Industrial Average ETF Trust / DIA**) gemäß dem Open Knowledge Format (OKF) v0.2.

---

## 1. Übersicht & Soll-Parameter

| Parameter | Soll-Wert | Erläuterung |
| :--- | :--- | :--- |
| **Gültigkeitsdatum** | `2026-11-07` / Vorbereitung für Handelstag `2026-11-09` | Erstellt am Wochenende nach Handelsschluss vom 06.11.2026 |
| **Tragende OKF-Regel** | [`regel-pre-event-paralyse`](okf-regeln/regel-pre-event-paralyse.md) | Ungewissheits-Paralyse vor US-Verbraucherpreisdaten (CPI) |
| **Erwartete Richtung** | `neutral` | Seitwärtskonsolidierung / Stagnation um den Pivot 512,22 USD |
| **Kurskorridor (DIA)** | `508.00` bis `516.00` | Untergrenze: Freitagstief (508,66); Obergrenze: Freitagshoch (515,98) |
| **Erwartetes Volumen** | `normal` | Gedämpftes institutionelles Handelsvolumen (3,0 bis 4,3 Mio. Anteile) |
| **Modell-Konfidenz** | `0.85` | Hohe statistische Wahrscheinlichkeit von Paralyse vor binärem Makro-Event |

---

## 2. Ausgangslage & Marktrecap (06.11.2026)

Am letzten Handelstag der Vorwoche zeigte der DJIA/DIA nach dem schweren Ausverkauf vom Donnerstag (Bull Trap mit 11,45 Mio. Rekordvolumen) ein zweigeteiltes Bild:

1. **Kursentwicklung DIA**:
   * Eröffnung bei **508,72** (Abwärts-Gap von -1,08 % ggü. Vortagsschluss 514,27).
   * Tagestief bei **508,66** bildete eine solide Intraday-Unterstützung.
   * Zwischenerholung bis auf ein Tageshoch von **515,98**.
   * Tagesschlusskurs bei **512,22** (-0,40 %; der Dow Jones Industrial Index verlor -0,46 % auf 51.285 Punkte).
   * Handelsvolumen: **4.010.171 Anteile** (entspricht exakt 0,94x des 10-Tages-Durchschnitts von ca. 4,24 Mio.).
2. **Dominierende Verhaltensnarrative**:
   * **Zinsangst („Good News is Bad News“)**: Die robusten US-Arbeitsmarktdaten (+59.000 Stellen im Oktober, Arbeitslosenquote stabil bei 4,2 %) und das solide Verbrauchervertrauen der Uni Michigan wurden nicht positiv aufgenommen. In Kombination mit den kriegsbedingt hohen Ölpreisen (Iran-Krieg) stärkten sie die Falken um Fed-Chef Kevin Warsh, der eine weitere Leitzinserhöhung im Dezember in Aussicht gestellt hat (siehe [`regel-zinsangst-good-news-bad-news`](okf-regeln/regel-zinsangst-good-news-bad-news.md)).
   * **Sektordivergenz**: Während abgestrafte Technologie- und Halbleiterwerte von gezielten Dip-Käufen profitierten (AMD +10,4 %, Lam +8,3 %, Intel +7,2 %, Nvidia +3,2 %, Nasdaq 100 +1,35 %), blieb der traditionelle Industrie- und Dividendenindex Dow Jones im Minus gefangen (siehe [`regel-sektordivergenz-bodenbildung`](okf-regeln/regel-sektordivergenz-bodenbildung.md)).

---

## 3. Auswertung der anstehenden Termine (termine.md)

Die Analyse der Wochenvorschau für die Woche vom 09. bis 13. November 2026 liefert folgende Schlüsselimpulse:

### A. Montag, 09. November 2026 (Unmittelbarer Prognosehorizont)
* **Konjunkturdaten**:
  * 02:30 MEZ: China Erzeuger- und Verbraucherpreise (10/26) – Relevanz für globale Rohstoff- und Exportdynamik.
  * 08:00 MEZ: Deutschland Außenhandelsdaten (Im-/Exporte 9/26), Lkw-Maut-Fahrleistungsindex.
  * 10:30 MEZ: Eurozone Sentix-Investorvertrauen (11/26).
  * *Bewertung*: Es stehen **keine marktbewegenden US-Makrodaten** an, die die US-Zinsdebatte am Montag vorab entscheiden könnten.
* **Unternehmensdaten**:
  * USA: KKR & Co (Q3).
  * Europa/Asien: Unicredit, Hannover Rück, Hypoport, Gea Group, Patrizia, Mazda Motor.
  * *Bewertung*: Primär Finanz- und Industrie-Mittelgewichte; keine DJIA-Schwergewichte, die eine breite Indexbewegung entfachen könnten.
* **Politik & Sondertermine**:
  * PK der Deutschen Telekom zur europäischen KI-Infrastruktur (München, mit Siemens-Chef Busch und Ministern).
  * Treffen der EU-Finanzminister und der Euro-Gruppe in Brüssel; G7-Außenministertreffen in Marseille.
  * 16:00 MEZ: Supreme Court der USA tagt in Washington.
  * Feiertag in Singapur (Börse geschlossen).

### B. Dienstag, 10. November 2026 (Das dominierende Makro-Großereignis)
* **14:15 MEZ USA**: ADP Arbeitslosenzahlen (Woche).
* **14:30 MEZ USA: Verbraucherpreise (CPI) 10/26 & Realeinkommen 10/26**.
* *Kritische Einordnung*:
  * Dies ist der **entscheidende Datenpunkt für die Zinsentscheidung der Federal Reserve im Dezember**.
  * Fällt der CPI inflationsbedingt heiß aus (getrieben durch Energie- und Importkosten), festigt sich die Zinserhöhungserwartung unter Kevin Warsh, was Standardaktien im DJIA weiter belasten dürfte.
  * Fällt der CPI überraschend moderat aus, könnte eine Entlastungsbewegung einsetzen.
* *Unternehmensberichte*: Infineon (Jahreszahlen), Henkel, Porsche Automobil Holding, Softbank, Adtran, Alcon.

---

## 4. Verhaltensökonomische Begründung & Regeldokumentation

### Warum greift die Bezugsregel [`regel-pre-event-paralyse`](okf-regeln/regel-pre-event-paralyse.md)?
1. **Entscheidungsaufschub unter Mehrdeutigkeit (Ambiguity Aversion)**:
   Vor einem binären Makroereignis ersten Ranges – wie dem US-Verbraucherpreisbericht am Dienstag um 14:30 MEZ – meiden institutionelle Portfolio-Manager und Market Maker neues Richtungsrisiko. Da am Montag keine richtungsweisenden US-Zahlen vorliegen, frieren Fonds ihre Allokationen weitgehend ein.
2. **Volatilitätskompression im Pivot-Band [508.00, 516.00]**:
   * Die Untergrenze bei **508.00** repräsentiert die erfolgreiche Testzone vom Freitag (Open 508,72 / Low 508,66). Unterhalb dieses Niveaus schlug die Dip-Buying-Nachfrage an. Ohne neue Schocknachrichten am Montag besteht kein Grund für einen Durchbruch nach unten.
   * Die Obergrenze bei **516.00** deckelt das Aufwärtspotenzial am Erholungshoch vom Freitag (High 515,98). Zinsängste und die drohende CPI-Zahl verhindern prozyklische Käufe über diese Hürde hinaus.
   * Der Kursverlauf dürfte daher um den Freitagsschluss bei **512,22** oszillieren.
3. **Volumenprofil**:
   * Institutionelle Orderbücher dünnen vor dem CPI-Event aus. Das Handelsvolumen wird voraussichtlich im moderat-gedämpften Bereich verbleiben (**normal**, typischerweise zwischen 3,0 und 4,2 Mio. Anteile, analog zum Vor-Wahltag am 03.11. mit 3,18 Mio. Anteilen).

---

## 5. Handlungsanweisung für automatisierte Handels- und Analysesysteme

* **Kein Breakout-Trading**: Scheinbare Ausbrüche über 516.00 oder unter 508.00 am Montag sind mit hoher Wahrscheinlichkeit Fehlausbrüche (Fakeouts), solange das Handelsvolumen unter 4,5 Mio. Anteilen verharrt.
* **Absicherungen intakt halten**: Bestehende Hedges gegen Zinsrisiken nicht vor Veröffentlichung des US-CPI am Dienstag auflösen.
* **Vorbereitung auf Volatilitätsexpansion am Dienstag**: Die verengte Handelsspanne am Montag bereitet das Feld für ein signifikantes Eröffnungs- oder Nachmittags-Gap am Dienstag ab 14:30 MEZ.
