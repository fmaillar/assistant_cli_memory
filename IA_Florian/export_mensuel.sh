#!/bin/bash
# Compilation d'un rapport PDF mensuel (nécessite Pandoc et latexmk)

mkdir -p exports
pandoc \
  00_profil/fiche_fonctionnement_fusionnee.md \
  02_usages/bilans_mensuels.md \
  03_projets/*.md \
  -o exports/rapport_$(date +%Y-%m).pdf \
  --from markdown --pdf-engine=latexmk --metadata title="Rapport IA Florian"
echo "✔ Rapport mensuel compilé dans exports/"
