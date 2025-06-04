# 📁 Dépôt IA_Florian – Configuration personnelle d'assistant IA

Ce répertoire constitue la base de fonctionnement de l'assistant personnel IA_Florian.

## 📦 Structure principale

- `00_profil/` : fichiers de base (santé, règles, fonctionnement)
- `02_usages/` : bilans, journaux, pratiques
- `03_projets/` : fichiers liés aux projets actifs (discernement, STI, paroisse)
- `04_templates/` : template de sortie
- `05_archives/` : anciennes conversations, ...
- `06_graphisme/` : prompts pour dall-e notamment
- `07_diffusion/` : anticipation d'envoi par IA
- `automation/` : scripts shell d’export et de tâches automatisées
- `cache/` : extrait pratique du conversations.json (trop lourd pour être traité en entier)
- `contexte/` : historique des sessions de l'assistant ia local
- `modules/` : modèles à venir piocher pour activer des fonctionnalités

## 🔧 Intégration

- Compatible avec un assistant local en mode terminal
- Repose sur des fichiers `.md`, `.yaml`, `.sh`, versionnés à la main

## 🧠 Dernières modifications

- Ajout du fichier `psychologie_sante.md`
- Réactivation du fichier `profil_strategique_florian.md`
- Restructuration de fichiers critiques vides

## 🧪 Tests

Les tests unitaires s'exécutent avec `pytest`.

```bash
pip install -r requirements.txt
pytest
```
