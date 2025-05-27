
import os
import openai
from pathlib import Path

openai.api_key = os.getenv("OPENAI_API_KEY")

def lire_fichier(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        return f.read()

def afficher_fichiers(dossier):
    fichiers = list(Path(dossier).glob("*.md")) + list(Path(dossier).glob("*.txt")) + list(Path(dossier).glob("*.csv"))
    return fichiers

def lancer_session_documents_light():
    print("📂 Chargement des fichiers depuis ./documents/")
    while True:
        fichiers = afficher_fichiers("documents")
        if not fichiers:
            print("❌ Aucun fichier trouvé dans ./documents/")
            return

        for i, f in enumerate(fichiers, 1):
            print(f"[{i}] {f.name}")
        print("[0] Quitter")

        choix = input("➡️  Choisis un fichier à traiter : ").strip()
        if choix == "0":
            print("👋 Session terminée.")
            break

        try:
            index = int(choix) - 1
            chemin_fichier = fichiers[index]
        except:
            print("❌ Choix invalide.")
            continue

        contenu = lire_fichier(chemin_fichier)
        print(f"📄 Fichier sélectionné : {chemin_fichier.name}")
        print("✉️ Envoi au modèle pour résumé... ")

        try:
            completion = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Tu es un assistant chargé d'analyser des documents texte (.md, .csv, .txt) et d'en extraire les points clés."},
                    {"role": "user", "content": f"Voici le contenu du fichier :\n{contenu}\n Merci d’en faire un résumé structuré avec bullet points."}
                ],
                temperature=0.4
            )
            print(" 🤖 Résumé IA : ")
            print(completion.choices[0].message.content.strip())
        except Exception as e:
            print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    lancer_session_documents_light()
