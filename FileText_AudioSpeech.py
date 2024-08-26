import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilenames(
        title="Sélectionnez un ou plusieurs fichiers",
        filetypes=[("Fichiers PDF", "*.pdf"), ("Fichiers texte", "*.txt")]
    )

def lire_fichier(path):
    text = ""
    if path.lower().endswith('.pdf'):
        with open(path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
    elif path.lower().endswith('.txt'):
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()

    if text.strip():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        print(f"Le fichier {path} est vide ou ne contient pas de texte extractible.")

paths = open_file_dialog()
if paths:
    for path in paths:
        lire_fichier(path)
else:
    print("Aucun fichier sélectionné.")
