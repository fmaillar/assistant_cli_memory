
import os
import time
from pathlib import Path
from utils.charger_profil_complet import charger_profil_complet
from utils.prompts import load_prompts

def initialiser_session_ia(dossier_profil: str = "IA_Florian") -> list:
    texte_profil = charger_profil_complet(dossier_profil)

    horodatage = time.strftime("%Y-%m-%d_%H-%M-%S")
    archive_path = Path(dossier_profil) / "00_profil" / "_archives"
    archive_path.mkdir(parents=True, exist_ok=True)
    archive_file = archive_path / f"profil_consolide_{horodatage}.md"
    archive_file.write_text(texte_profil, encoding="utf-8")

    message = {
        "role": "system",
        "content": f"[Profil IA Florian consolidé, horodaté {horodatage}]\n\n{texte_profil}"
    }

    return [message]

def choix_gpt():
    prompts = load_prompts()
    print("\n📋 Choisissez un prompt parmi la liste :\n")
    for i, p in enumerate(prompts):
        print(f"[{i+1}] {p['titre']}")
    print("[0] Aucun prompt\n")
    try:
        choix = int(input("Votre choix : ").strip() or 0)
        if 1 <= choix <= len(prompts):
            return prompts[choix - 1]["prompt"]
    except:
        pass
    return "Tu es un assistant IA."
