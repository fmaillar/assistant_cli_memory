# 📦 Makefile — Assistant IA Florian (structure complète)

# === VARIABLES ===
PYTHON      := python
SCRIPT_GD   := drive_sync.py
PROFILE     := IA_Florian
ARCHIVE_DIR := ./$(PROFILE)
DATE        := $(shell date +%Y-%m-%d)
TS          := $(shell date +%Y-%m-%d_%H%M)

DOSSIER_LOCAL = IA_Florian
DOSSIER_DRIVE = IA_Florian

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
	@printf "## 📆 Bilan – $(shell date +%B\ %Y)\n\n### ✅ Réalisations clés\n\n- \n\n### 🧠 Prises de conscience\n\n- \n\n### 🧭 Priorités mois prochain\n\n- \n\n### ⏳ Points de vigilance\n\n- \n\n### 🧠 Cognitif / Structuration IA\n\n- \n\n### 💻 Professionnel\n\n- \n\n### 🧬 Personnel / Santé\n\n- \n\n### 💒 Spirituel / Intérieur\n\n- \n\n### 👨 👩 👧 Vie familiale\n\n- \n" >> $(ARCHIVE_DIR)/02_usages/bilans_mensuels.md
	@echo "✔ Bloc ajouté."

log:
	@echo "📘 Historique des sauvegardes :"
	@cat log_sauvegardes.md || echo "Aucun log trouvé."

# === SYNC AVEC GDRIVE ===
# === ATTENTION AUX VARIABLES ===
# Exemples d'utilisation
#	make upload_file FICHIER_LOCAL=rapport.txt DOSSIER_DRIVE=Archives
#	make download_file FICHIER_DRIVE=old.txt DEST_LOCAL=./truc.txt
#upload_file:
#	$(PYTHON) $(SCRIPT_GD) upload_file $(FICHIER_LOCAL) $(DOSSIER_DRIVE)
#
#upload_folder:
#	$(PYTHON) $(SCRIPT_GD) upload_folder $(DOSSIER_LOCAL) $(DOSSIER_DRIVE)
#
#download_file:
#	$(PYTHON) $(SCRIPT_GD) download_file $(FICHIER_DRIVE) $(DEST_LOCAL)
#
#download_folder:
#	$(PYTHON) $(SCRIPT_GD) download_folder $(DOSSIER_DRIVE) $(DOSSIER_LOCAL)_download
#
#list_folder:
#	$(PYTHON) $(SCRIPT_GD) list_folder $(DOSSIER_DRIVE)

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
	@echo "  make run                 → Lancer le menu principal"
	@echo "  make setup               → Installer les dépendances"
	@echo "  make reset               → Réinitialiser les contextes"
	@echo "  make bilan               → Ajouter un bloc de bilan"
	@echo "  make archive             → Archiver IA_Florian"
#	@echo "  make archive_sync        → Archive + sync vers Drive"
#	@echo "  make archive_sync_rotate → Archive + sync + rotation"
	@echo "  make routine_hebdo       → Pipeline complet hebdo"
#	@echo "  make rotate              → Supprimer vieilles archives Drive"
#	@echo "  make clean_local         → Supprimer vieilles archives locales"
	@echo "  make log                 → Voir les sauvegardes"
#	@echo "  make sync_drive          → Uploader archive manuelle"
#	@echo "  make upload_file         → Upload un fichier simple"
#	@echo "  make upload_folder       → Upload récursif d'un dossier"
#	@echo "  make download_file       → Télécharge un fichier Drive"
#	@echo "  make download_folder     → Télécharge récursivement un dossier Drive"
#	@echo "  make list_folder         → Liste les fichiers dans un dossier Drive"

