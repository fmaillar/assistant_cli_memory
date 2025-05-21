#!/bin/bash

# Script de routine hebdomadaire pour IA_Florian
# Exécute : sauvegarde, sync, rotation, log horodaté

set -e

echo "🔁 [$(date '+%Y-%m-%d %H:%M:%S')] Début de la routine IA_Florian"

# Aller dans le dossier contenant le Makefile
cd "$(dirname "$0")"

# Lancer la routine hebdo complète
make routine_hebdo

# Lancer l'archivage + sync + rotation explicite si besoin
# make archive_sync_rotate

# Afficher les logs
echo "📘 Log sauvegarde (log_sauvegardes.md) :"
tail -n 10 log_sauvegardes.md 2>/dev/null || echo "(pas encore de log)"

echo "✅ [$(date '+%Y-%m-%d %H:%M:%S')] Routine IA_Florian terminée"
