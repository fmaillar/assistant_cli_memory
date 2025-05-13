# Makefile – Assistant personnel CLI IA_Florian

.PHONY: install run lint format clean freeze

# Installation des dépendances (sans venv)
install:
	pip install -U openai pyyaml tqdm

# Lancer l'assistant CLI (script principal)
run:
	python main.py

# Linter simple (optionnel)
lint:
	flake8 *.py

# Formatage de code (optionnel)
format:
	black *.py

# Nettoyage (logs, fichiers temporaires)
clean:
	rm -rf __pycache__ logs/*

# Gèle les dépendances dans un fichier requirements.txt
freeze:
	pip freeze > requirements.txt

