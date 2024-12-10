import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta


class ArbeitszeitRechner:
    def __init__(self, root):
        self.root = root
        self.root.title("Arbeitszeitrechner")

        # Liste für Tage
        self.tage = []

        # Überschrift
        tk.Label(root, text="Arbeitszeitrechner", font=("Arial", 16)).grid(row=0, column=0, columnspan=7, pady=10)

        # Hinzufügen eines Tages
        self.hinzufuegen_tag()

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.grid(row=99, column=0, columnspan=7, pady=10)

        tk.Button(button_frame, text="Weiteren Tag hinzufügen", command=self.hinzufuegen_tag).pack(side="left", padx=10)
        tk.Button(button_frame, text="Gesamtsumme berechnen", command=self.berechne_gesamtzeit).pack(side="left",
                                                                                                     padx=10)

    def hinzufuegen_tag(self):
        row = len(self.tage) + 1
        tag_frame = {}

        # Label für den Tag
        tk.Label(self.root, text=f"Tag {len(self.tage) + 1}:", font=("Arial", 12)).grid(row=row, column=0, padx=5,
                                                                                        pady=5, sticky="w")

        # Dropdown-Menüs für Startzeit (Stunden und Minuten)
        tk.Label(self.root, text="Startzeit (HH:MM):").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        tag_frame["start_stunden"] = ttk.Combobox(self.root, values=[f"{i:02}" for i in range(24)], width=3,
                                                  state="readonly")
        tag_frame["start_stunden"].grid(row=row, column=2, padx=2, pady=5)
        tag_frame["start_stunden"].set("00")

        tag_frame["start_minuten"] = ttk.Combobox(self.root, values=[f"{i:02}" for i in range(60)], width=3,
                                                  state="readonly")
        tag_frame["start_minuten"].grid(row=row, column=3, padx=2, pady=5)
        tag_frame["start_minuten"].set("00")

        # Dropdown-Menüs für Endzeit (Stunden und Minuten)
        tk.Label(self.root, text="Endzeit (HH:MM):").grid(row=row, column=4, padx=5, pady=5, sticky="w")
        tag_frame["end_stunden"] = ttk.Combobox(self.root, values=[f"{i:02}" for i in range(24)], width=3,
                                                state="readonly")
        tag_frame["end_stunden"].grid(row=row, column=5, padx=2, pady=5)
        tag_frame["end_stunden"].set("00")

        tag_frame["end_minuten"] = ttk.Combobox(self.root, values=[f"{i:02}" for i in range(60)], width=3,
                                                state="readonly")
        tag_frame["end_minuten"].grid(row=row, column=6, padx=2, pady=5)
        tag_frame["end_minuten"].set("00")

        # Ergebnisfeld
        tag_frame["ergebnis"] = tk.Label(self.root, text="00:00", font=("Arial", 12))
        tag_frame["ergebnis"].grid(row=row, column=7, padx=5, pady=5)

        # Hinzufügen zur Liste
        self.tage.append(tag_frame)

    def berechne_gesamtzeit(self):
        gesamtzeit = timedelta()

        for tag in self.tage:
            try:
                # Hole die Zeitwerte aus den Dropdowns
                start_stunden = int(tag["start_stunden"].get())
                start_minuten = int(tag["start_minuten"].get())
                end_stunden = int(tag["end_stunden"].get())
                end_minuten = int(tag["end_minuten"].get())

                # Erstelle datetime-Objekte
                start = datetime.strptime(f"{start_stunden:02}:{start_minuten:02}", "%H:%M")
                end = datetime.strptime(f"{end_stunden:02}:{end_minuten:02}", "%H:%M")

                # Berechne Arbeitszeit
                arbeitszeit = end - start
                if arbeitszeit.total_seconds() < 0:
                    arbeitszeit += timedelta(days=1)  # Für Übernachtungszeiten

                # Pausenregel: Ab 6 Stunden nur die Zeit über 6 Stunden abziehen (maximal 30 Minuten)
                if arbeitszeit > timedelta(hours=6):
                    ueberschuss = arbeitszeit - timedelta(hours=6)
                    pause = min(ueberschuss, timedelta(minutes=30))
                    arbeitszeit -= pause

                # Update der Tagesanzeige
                tag["ergebnis"].config(text=str(arbeitszeit)[:-3])  # Kürzt Sekunden ab

                # Hinzufügen zur Gesamtsumme
                gesamtzeit += arbeitszeit

            except ValueError:
                # Fehlerbehandlung bei fehlerhaften Eingaben
                messagebox.showerror("Fehler", f"Ungültige Eingabe bei Tag {self.tage.index(tag) + 1}.")
                return

        # Anzeige der Gesamtsumme
        gesamtstunden = int(gesamtzeit.total_seconds() // 3600)
        gesamtminuten = int((gesamtzeit.total_seconds() % 3600) // 60)

        messagebox.showinfo("Gesamtzeit", f"Gesamte Arbeitszeit: {gesamtstunden} Stunden {gesamtminuten} Minuten")


# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    app = ArbeitszeitRechner(root)
    root.mainloop()
