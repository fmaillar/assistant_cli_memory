# Makefile – Assistant IA + Profil IA unifié

PYTHON=python

# === Assistant CLI ===

run:
	@echo "💡 Usage : make run_classique | run_documents | run_auto"

run_classique:
	@echo "🚀 Mode classique (conversation GPT)"
	$(PYTHON) entrypoints/main.py classique

run_documents:
	@echo "📂 Mode documents (upload + analyse fichiers)"
	$(PYTHON) entrypoints/main.py documents

run_auto:
	@echo "🔁 Lancement selon IA_FLORIAN_MODE ($$IA_FLORIAN_MODE)"
	$(PYTHON) entrypoints/main.py

setup:
	@echo "🔧 Installation des dépendances..."
	pip install -r requirements.txt

reset:
	@echo "🧹 Réinitialisation du contexte..."
	rm -f context/*.json
	@echo "✔ Contextes supprimés."

# === Gestion du profil IA (IA_Florian) ===

bilan:
	@echo "📝 Génération d’un bloc de bilan..."
	@mkdir -p IA_Florian/02_usages
	@echo "## 📆 Bilan – $(shell date +%B\ %Y)\n- ✅ Réalisations clés : \n- 🧠 Prises de conscience : \n- 🧭 Priorités mois prochain : \n- ⏳ Points de vigilance : \n" >> IA_Florian/02_usages/bilans_mensuels.md
	@echo "✔ Bloc ajouté à IA_Florian/02_usages/bilans_mensuels.md"

archive:
	@echo "📦 Création de l’archive IA_Florian.zip..."
	@zip -r IA_Florian_$(shell date +%Y-%m-%d).zip IA_Florian >/dev/null
	@echo "✔ Archive générée : IA_Florian_$(shell date +%Y-%m-%d).zip"

init_git:
	@echo "🔧 Initialisation Git dans IA_Florian/..."
	cd IA_Florian && git init && git add . && git commit -m "Initialisation du dépôt IA_Florian" || true
	@echo "✔ Dépôt Git initialisé."

status_git:
	@cd IA_Florian && git status || echo "❌ Dépôt non initialisé."

index_prompts:
	$(PYTHON) utils/prompts_indexer.py

# === Aide ===

help:
	@echo "📘 Commandes disponibles :"
	@echo "  make run         → Lancer l’assistant IA local"
	@echo "  make setup       → Installer les dépendances"
	@echo "  make reset       → Réinitialiser les contextes"
	@echo "  make bilan       → Ajouter un bloc de bilan mensuel"
	@echo "  make archive     → Créer une archive .zip du profil IA"
	@echo "  make init_git    → Initialiser Git dans IA_Florian/"
	@echo "  make status_git  → Voir l’état Git du profil"
