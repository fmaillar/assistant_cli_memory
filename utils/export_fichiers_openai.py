
import openai
import time
from pathlib import Path
from datetime import datetime
import csv
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def exporter_liste_fichiers_markdown(path="IA_Florian/02_usages/logs/fichiers_openai.md"):
    fichiers = openai.files.list().data
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    lignes = [
        "# Liste des fichiers stockés via l'API OpenAI",
        f"*Dernière mise à jour :* {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "| ID | Nom | Taille (Ko) | Créé le |",
        "|----|-----|--------------|----------|"
    ]

    for f in fichiers:
        lignes.append(f"| {f.id} | {f.filename} | {round(f.bytes / 1024, 1)} | {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(f.created_at))} |")

    path.write_text("\n".join(lignes), encoding="utf-8")
    print(f"[✓] Export Markdown généré : {path}")

def exporter_liste_fichiers_csv(path="IA_Florian/02_usages/logs/fichiers_openai.csv"):
    fichiers = openai.files.list().data
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Nom", "Taille (octets)", "Créé le"])
        for fichier in fichiers:
            writer.writerow([
                fichier.id,
                fichier.filename,
                fichier.bytes,
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(fichier.created_at))
            ])

    print(f"[✓] Export CSV généré : {path}")
