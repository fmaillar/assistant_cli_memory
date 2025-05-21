# Makefile – Assistant IA unifié via launcher

PYTHON=python

prompt-conversations:
	@echo "🔄 Génération du prompt conversations..."
	@$(PYTHON) generate_prompt_from_index.py --all

run:
	@$(PYTHON) entrypoints/launcher.py

setup:
	@echo "🔧 Installation des dépendances..."
	pip install -r requirements.txt

reset:
	@echo "🧹 Réinitialisation du contexte..."
	rm -f context/*.json
	@echo "✔ Contextes supprimés."

bilan:
	@echo "📝 Génération d’un bloc de bilan..."
	@mkdir -p IA_Florian/02_usages
	@echo "## 📆 Bilan – $(shell date +%B\ %Y)\n- ✅ Réalisations clés : \n- 🧠 Prises de conscience : \n- 🧭 Priorités mois prochain : \n- ⏳ Points de vigilance : \n" >> IA_Florian/02_usages/bilans_mensuels.md
	@echo "✔ Bloc ajouté à IA_Florian/02_usages/bilans_mensuels.md"

archive:
	@echo "📦 Création de l’archive IA_Florian.zip..."
	zip -r IA_Florian_$(shell date +%Y-%m-%d).zip IA_Florian >/dev/null
	@echo "✔ Archive générée : IA_Florian_$(shell date +%Y-%m-%d).zip"

index_prompts:
	@$(PYTHON) utils/prompts_indexer.py

sync_drive:
	@$(PYTHON) -c "from drive_sync import upload_file; upload_file('IA_Florian_2025-05-21.zip', '1bLROt0vI6YLPKcQ4lJ2YT0SaDtc070jW')"

archive_sync:
	@$(PYTHON) archive_and_sync.py

log:
	@echo "📘 Historique des sauvegardes :"
	@cat log_sauvegardes.md

rotate:
	python3 rotation_archives.py

archive_sync_rotate:
	@$(PYTHON) archive_and_sync.py
	@$(PYTHON) rotation_archives.py

clean_local:
	@$(PYTHON) nettoyage_local.py

routine_hebdo:
	@$(PYTHON) archive_and_sync.py
	@$(PYTHON) rotation_archives.py
	@$(PYTHON) nettoyage_local.py

help:
	@echo "📘 Commandes disponibles :"
	@echo "  make run         → Lancer le menu IA_Florian via launcher"
	@echo "  make setup       → Installer les dépendances"
	@echo "  make reset       → Réinitialiser les contextes"
	@echo "  make bilan       → Ajouter un bloc de bilan mensuel"
	@echo "  make archive     → Créer une archive .zip du profil IA"