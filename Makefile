# Makefile – Assistant IA unifié via launcher

PYTHON=python

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
	$(PYTHON) utils/prompts_indexer.py

help:
	@echo "📘 Commandes disponibles :"
	@echo "  make run         → Lancer le menu IA_Florian via launcher"
	@echo "  make setup       → Installer les dépendances"
	@echo "  make reset       → Réinitialiser les contextes"
	@echo "  make bilan       → Ajouter un bloc de bilan mensuel"
	@echo "  make archive     → Créer une archive .zip du profil IA"