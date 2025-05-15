
# entrypoints/launcher.py
import yaml
import subprocess
import os
from pathlib import Path

def charger_config():
    with open("config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def menu_scripts(scripts):
    print("\n📜 Scripts disponibles :\n")
    for nom, info in scripts.items():
        print(f"  ▶ {nom} : {info['description']}")
    print()
    return input("➡️  Choisis un script à lancer : ").strip()

def executer_script(scripts, nom):
    if nom not in scripts:
        print("❌ Script non trouvé.")
        return
    chemin = scripts[nom]["path"]
    print(f"🚀 Lancement de {chemin}...\n")
    subprocess.run(["python", chemin])

def main():
    config_path = Path("config.yaml")
    if not config_path.exists():
        print("❌ Fichier config.yaml introuvable.")
        return

    config = charger_config()
    scripts = config.get("scripts", {})

    if not scripts:
        print("❌ Aucun script défini dans config.yaml")
        return

    choix = menu_scripts(scripts)
    executer_script(scripts, choix)

if __name__ == "__main__":
    main()
