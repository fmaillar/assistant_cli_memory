import os
import re
import unicodedata
import openai
from pathlib import Path
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def slugify(titre):
    slug = unicodedata.normalize('NFKD', titre)
    slug = slug.encode('ascii', 'ignore').decode('ascii')
    slug = re.sub(r'[^a-zA-Z0-9]+', '_', slug)
    return slug.strip('_').lower()

def charger_prompts_disponibles():
    index = Path("IA_Florian/01_prompts/index.md")
    if not index.exists():
        return []
    prompts = []
    with index.open(encoding="utf-8") as f:
        for line in f:
            if line.startswith("|") and "Titre" not in line:
                parts = line.strip().split("|")
                if len(parts) >= 3:
                    titre = parts[1].strip()
                    objectif = parts[2].strip()
                    prompts.append((titre, objectif))
    return prompts

def mode_prompt_interactif():
    prompts = charger_prompts_disponibles()
    if not prompts:
        print("❌ Aucun prompt disponible.")
        return
    print("\n📚 Prompts disponibles :")
    for i, (titre, objectif) in enumerate(prompts, 1):
        print(f"[{i}] {titre:<35} — {objectif}")
    choix = input("\n➡️ Choisis un prompt à utiliser : ").strip()
    if not choix.isdigit() or not (1 <= int(choix) <= len(prompts)):
        print("❌ Numéro invalide.")
        return
    titre = prompts[int(choix)-1][0]
    chemin = Path(f"IA_Florian/01_prompts/{slugify(titre)}.md")
    if not chemin.exists():
        print(f"❌ Fichier introuvable : {chemin}")
        return
    consigne = chemin.read_text(encoding="utf-8").strip()
    print(f"🧠 Prompt sélectionné : {titre}\n\n{consigne}")
    while True:
        texte = input("\nVotre input ('exit' pour quitter) > ").strip()
        if texte.lower() == "exit":
            break
        try:
            res = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": consigne},
                    {"role": "user", "content": texte}
                ]
            )
            print(f"🤖 Résultat :\n{res.choices[0].message.content.strip()}")
        except Exception as e:
            print(f"❌ Erreur : {e}")


def charger_profil_ia(base: str = "IA_Florian") -> str:
    fichiers = [
        "00_profil/fiche_fonctionnement_fusionnee.md",
        "00_profil/profil_fonctionnel_florian.md",
        "00_profil/regles_automatiques.md",
        "00_profil/reinjection_memorielle.md",
        "00_profil/audit_fichiers.md",
        "02_vie_interieure/registre_detections_sensibles.md",
        "05_cas_concrets/tableau_casuistica_multiscenario.md"
    ]
    contenu = []
    for f in fichiers:
        try:
            texte = Path(base, f).read_text(encoding="utf-8")
            contenu.append(f"\n\n==== {f} ====\n\n{texte}")
        except FileNotFoundError:
            continue
    return "\n".join(contenu)

def afficher_prompts():
    index = Path("IA_Florian/01_prompts/index.md")
    if not index.exists():
        return
    print("\n📚 Prompts disponibles :")
    print("-" * 100)
    print(f"{'N°':<4} | {'Titre':<40} | Objectif")
    print("-" * 100)
    with index.open(encoding="utf-8") as f:
        compteur = 1
        for line in f:
            if line.startswith("|") and "Titre" not in line:
                parts = line.strip().split("|")
                if len(parts) >= 3:
                    titre = parts[1].strip()
                    objectif = parts[2].strip()
                    print(f"{compteur:<4} | {titre:<40} | {objectif}")
                    compteur += 1
    print("-" * 100)
    print("💡 Détails : IA_Florian/01_prompts/index.md\n")

def mode_classique():
    print("\n🧠 Mode classique – tape 'exit' pour quitter.")
    historique = []
    while True:
        prompt = input("Vous > ").strip()
        if prompt.lower() in {"exit", "quit"}:
            break
        historique.append({"role": "user", "content": prompt})
        try:
            res = openai.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": "Tu es un assistant structuré, efficace, rigoureux."}] + historique,
                temperature=0.4
            )
            output = res.choices[0].message.content.strip()
            print(f"\n🤖 {output}\n")
            historique.append({"role": "assistant", "content": output})
        except Exception as e:
            print(f"❌ Erreur : {e}")

def mode_starter():
    print("\n🧠 Mode starter IA_Florian – tape 'exit' pour quitter.")
    historique = []
    profil = charger_profil_ia()
    while True:
        prompt = input("Florian > ").strip()
        if prompt.lower() in {"exit", "quit"}:
            break
        historique.append({"role": "user", "content": prompt})
        try:
            res = openai.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": profil}] + historique[-8:],
                temperature=0.4
            )
            output = res.choices[0].message.content.strip()
            print(f"\n🧠 IA_Florian > {output}\n")
            historique.append({"role": "assistant", "content": output})
        except Exception as e:
            print(f"❌ Erreur : {e}")

def mode_documents():
    path_docs = Path("documents")
    fichiers = list(path_docs.glob("*.md")) + list(path_docs.glob("*.txt")) + list(path_docs.glob("*.csv"))
    if not fichiers:
        print("❌ Aucun fichier trouvé dans ./documents/")
        return
    while True:
        print("\n📂 Fichiers disponibles :")
        for i, f in enumerate(fichiers, 1):
            print(f"[{i}] {f.name}")
        print("[0] Retour")
        choix = input("➡️ Choix du fichier : ").strip()
        if choix == "0":
            return
        try:
            idx = int(choix) - 1
            texte = fichiers[idx].read_text(encoding="utf-8")
            res = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Tu es un assistant qui résume précisément les documents fournis."},
                    {"role": "user", "content": f"Voici le contenu :\n{texte}\n\nDonne un résumé structuré en bullet points."}
                ],
                temperature=0.4
            )
            print("\n🧾 Résumé :\n" + res.choices[0].message.content.strip())
        except Exception as e:
            print(f"❌ Erreur : {e}")

def mode_rapport_ia():
    print("\n📄 Génération du rapport IA global...")
    profil = charger_profil_ia()
    try:
        res = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": profil},
                {"role": "user", "content": "Établis un rapport synthétique IA_Florian en 5 sections : Résumé, Vigilances, Avancées, Tensions, Recos stratégiques 30 jours."}
            ],
            temperature=0.3
        )
        print("\n📋 Rapport IA :\n" + res.choices[0].message.content.strip())
    except Exception as e:
        print(f"❌ Erreur : {e}")

def menu():
    while True:
        print("\n🎛 MENU IA – Choisissez un mode")
        print("[1] Classique")
        print("[2] Starter IA_Florian")
        print("[3] Résumé de documents")
        print("[4] Rapport IA complet")
        print("[5] Utiliser un prompt")
        print("[0] Quitter")
        choix = input("➡️ Choix : ").strip()
        if choix == "1":
            mode_classique()
        elif choix == "2":
            mode_starter()
        elif choix == "3":
            mode_documents()
        elif choix == "4":
            mode_rapport_ia()
        elif choix == "5":
            mode_prompt_interactif()
        elif choix == "0":
            print("👋 Fin de session.")
            break
        else:
            print("❌ Choix invalide.")

if __name__ == "__main__":
    menu()


