import datetime
import os

# Liste der Wochentage von Montag (Index 0) bis Samstag (Index 5)
DAYS = ["montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag"]

# Pfad zum Ordner in Google Colab
FOLDER_PATH = "newscheck"

def get_day_order():
    # Aktuellen Wochentag ermitteln (0 = Montag, 6 = Sonntag)
    today_num = datetime.datetime.now().weekday()
    
    # Falls heute Sonntag ist (Index 6), starten wir mit Samstag (Index 5)
    if today_num > 5:
        start_index = 5
    else:
        start_index = today_num

    # Wochentage rückwärts ab heute zusammenstellen
    ordered_days = []
    for i in range(len(DAYS)):
        day_idx = (start_index - i) % len(DAYS)
        ordered_days.append(DAYS[day_idx])
        
    return ordered_days

def combine_files(output_filename="gesamt.txt"):
    ordered_days = get_day_order()
    print("Lese-Reihenfolge der Tage:", " -> ".join(ordered_days))
    
    # Ausgabedatei direkt im Ordner newscheck speichern (oder nach Wunsch im Hauptverzeichnis)
    output_path = os.path.join(FOLDER_PATH, output_filename)
    
    with open(output_path, "w", encoding="utf-8") as outfile:
        for day in ordered_days:
            filename = f"{day}.txt"
            file_path = os.path.join(FOLDER_PATH, filename)
            
            if os.path.exists(file_path):
                outfile.write(f"=== {day.upper()} ===\n")
                with open(file_path, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
                outfile.write("\n\n" + "="*30 + "\n\n")
                print(f"Datei '{filename}' hinzugefügt.")
            else:
                print(f"Warnung: Datei '{file_path}' wurde nicht gefunden.")

    print(f"\nGesamtausgabe erfolgreich erstellt unter: {output_path}")

if __name__ == "__main__":
    combine_files()
