import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np
import pandas as pd
import os
import sys

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

model_path = os.path.join(base_path, "model", "model_xg_rf.pkl")
model = joblib.load(model_path)

features = [
    'distance',
    'angle',
    'first_time_shot',
    'body_part_foot',
    'body_part_head',
    'penalty'
]

def calculate_xg():
    try:
        inputs = {}
        for feature in features:
            val = entries[feature].get().strip()
            if val == "":
                raise ValueError(f"Pole '{labels[feature]}' nie może być puste.")
            if feature in ['first_time_shot', 'body_part_foot', 'body_part_head', 'penalty']:
                val = int(val)
                if val not in [0, 1]:
                    raise ValueError(f"Pole '{labels[feature]}' musi mieć wartość 0 lub 1.")
            else:
                val = float(val)
            inputs[feature] = val

        # Walidacja logiczna: tylko noga lub głowa
        if inputs['body_part_foot'] == 1 and inputs['body_part_head'] == 1:
            raise ValueError("Strzał nie może być oddany nogą i głową jednocześnie.")

        # Walidacja fizyczna: maksymalna sensowna odległość i kąt
        if inputs['penalty'] == 1:
            xg = 0.77
            komunikat = "Rzut karny – xG ustawione na 0.77"
        elif inputs['distance'] > 40 or inputs['angle'] > 90:
            xg = 0.01
            komunikat = "Strzał z bardzo trudnej pozycji – xG ≈ 0"
        else:
            data = pd.DataFrame([{
                'distance': inputs['distance'],
                'angle': inputs['angle'],
                'first_time_shot': inputs['first_time_shot'],
                'body_part_foot': inputs['body_part_foot'],
                'body_part_head': inputs['body_part_head']
            }])
            xg = model.predict_proba(data)[0][1]
            komunikat = ""

        wynik = f"xG: {xg:.3f}"
        if komunikat:
            wynik += f"\n({komunikat})"

        result_var.set(wynik)

    except Exception as e:
        messagebox.showerror("Błąd", f"Nieprawidłowe dane wejściowe.\n{e}")

root = tk.Tk()
root.title("xG Kalkulator – Viteckpl & ChatGPT")

frame = tk.Frame(root, padx=20, pady=20, bg="#f0f0f0")
frame.pack()

entries = {}
labels = {
    'distance': "Odległość od bramki (metry, max 40)",
    'angle': "Kąt strzału (stopnie, max 90)",
    'first_time_shot': "Strzał z pierwszej piłki (1 = tak, 0 = nie)",
    'body_part_foot': "Strzał nogą (1 = tak, 0 = nie)",
    'body_part_head': "Strzał głową (1 = tak, 0 = nie)",
    'penalty': "Rzut karny (1 = tak, 0 = nie)"
}

for i, feature in enumerate(features):
    label = tk.Label(frame, text=labels[feature], anchor="w", bg="#f0f0f0")
    label.grid(row=i, column=0, sticky="w", pady=2)
    entry = tk.Entry(frame, width=10)
    entry.grid(row=i, column=1, pady=2)
    entries[feature] = entry

tk.Button(frame, text="Oblicz xG", command=calculate_xg, bg="#444", fg="white", padx=10).grid(row=len(features), column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_var, font=("Arial", 14), bg="#f0f0f0", fg="#333", justify="center")
result_label.grid(row=len(features)+1, column=0, columnspan=2)

footer = tk.Label(frame, text="Autorzy: Viteckpl 🧠 & ChatGPT 🤖\nSilnik: RandomForest (100 drzew) 🌲", font=("Arial", 8), bg="#f0f0f0", fg="#666")
footer.grid(row=len(features)+2, column=0, columnspan=2, pady=(10, 0))

root.mainloop()
