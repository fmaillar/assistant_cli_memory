# 📦 Makefile — Assistant IA Florian (structure complète)

# === VARIABLES ===
PYTHON      := python
PROFILE     := IA_Florian
ARCHIVE_DIR := ./$(PROFILE)
DATE        := $(shell date +%Y-%m-%d)
TS          := $(shell date +%Y-%m-%d_%H%M)

# === COMMANDES DE LANCEMENT ===
run:
	@$(PYTHON) entrypoints/launcher.py

setup:
	@echo "🔧 Installation des dépendances..."
	pip install -r requirements.txt

reset:
	@echo "🧹 Réinitialisation des contextes JSON..."
	@rm -fv contextes/*.json
	@echo "✔ Contexte effacé."

# === BILAN & JOURNALISATION ===
bilan:
	@echo "📝 Ajout d’un bloc de bilan mensuel..."
	@mkdir -p $(ARCHIVE_DIR)/02_usages
	@echo "## 📆 Bilan – $(shell date +%B\ %Y)\n- ✅ Réalisations clés : \n- 🧠 Prises de conscience : \n- 🧭 Priorités mois prochain : \n- ⏳ Points de vigilance : \n" >> $(ARCHIVE_DIR)/02_usages/bilans_mensuels.md
	@echo "✔ Bloc ajouté."

log:
	@echo "📘 Historique des sauvegardes :"
	@cat log_sauvegardes.md || echo "Aucun log trouvé."

# === ARCHIVAGE ===
archive:
	@echo "📦 Archivage de $(ARCHIVE_DIR)/ vers $(PROFILE)_$(DATE).zip"
	@zip -r $(PROFILE)_$(DATE).zip $(ARCHIVE_DIR) >/dev/null
	@echo "✔ Archive créée."

archive_sync:
	@$(PYTHON) archive_and_sync.py

archive_sync_rotate:
	@$(PYTHON) archive_and_sync.py
	@$(PYTHON) rotation_archives.py

routine_hebdo:
	@$(PYTHON) archive_and_sync.py
	@$(PYTHON) rotation_archives.py
	@$(PYTHON) nettoyage_local.py

rotate:
	@$(PYTHON) rotation_archives.py

clean_local:
	@$(PYTHON) nettoyage_local.py

# === SYNC & PROMPTS ===
sync_drive:
	@$(PYTHON) -c "from drive_sync import upload_file; upload_file('$(PROFILE)_$(DATE).zip', '1bLROt0vI6YLPKcQ4lJ2YT0SaDtc070jW')"

prompt-conversations:
	@$(PYTHON) generate_prompt_from_index.py --all

index_prompts:
	@$(PYTHON) utils/prompts_indexer.py

# === AIDE ===
help:
	@echo "🧠 Commandes disponibles :"
	@echo "  make run               → Lancer le menu principal"
	@echo "  make setup             → Installer les dépendances"
	@echo "  make reset             → Réinitialiser les contextes"
	@echo "  make bilan             → Ajouter un bloc de bilan"
	@echo "  make archive           → Archiver IA_Florian"
	@echo "  make archive_sync      → Archive + sync vers Drive"
	@echo "  make archive_sync_rotate → Archive + sync + rotation"
	@echo "  make routine_hebdo     → Pipeline complet hebdo"
	@echo "  make rotate            → Supprimer vieilles archives Drive"
	@echo "  make clean_local       → Supprimer vieilles archives locales"
	@echo "  make log               → Voir les sauvegardes"
	@echo "  make sync_drive        → Uploader archive manuelle"

