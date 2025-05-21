
import subprocess

def sauvegarde_complete():
    print("📦 Lancement de la sauvegarde complète IA_Florian...")
    result = subprocess.run(["make", "archive_sync_rotate"], capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Sauvegarde complète effectuée avec succès.")
    else:
        print("❌ Erreur lors de la sauvegarde complète :")
        print(result.stderr)

def afficher_log():
    try:
        with open("log_sauvegardes.md", "r", encoding="utf-8") as log_file:
            print("📘 Historique des sauvegardes :\n")
            print(log_file.read())
    except FileNotFoundError:
        print("❌ Aucun historique trouvé.")
