# 🔄 Règle fonctionnelle – Flexibilité contrôlée par mémoire temporaire

## Titre
**Autorisation conditionnelle de mémoire temporaire pour traitement fluide**

## Statut
✅ Active  
📅 Mise en place : 2025-05-22  
🔐 Complément à la règle fondamentale “Zéro mémoire implicite”

## Objectif
Permettre une souplesse d’analyse et une réactivité accrue, **sans enfreindre la règle de persistance obligatoire**.

---

## 🔁 Mécanisme autorisé

1. **Chargement ciblé temporaire**
   - Lecture et stockage temporaire d’un sous-ensemble de fichiers (ex. : `profil_strategique_florian.md`, `fusion/*.merge.md`, etc.)
   - Utilisation pour raisonnement, comparaison, fusion, analyse vectorielle…

2. **Traitement interne non persistant**
   - Le moteur IA travaille en RAM, sans écrire dans la mémoire modèle ChatGPT
   - Aucune déduction n’est considérée comme acquise à ce stade

3. **Archivage obligatoire**
   - Toute production (contenu, décision, synthèse, log, nouveau fichier) est :
     - enregistrée dans `IA_Florian/`,
     - datée et structurée,
     - et marquée comme **résultat final** de la session

4. **Nettoyage explicite**
   - La mémoire temporaire est vidée à la fin du cycle
   - Aucun reliquat logique ne subsiste après sauvegarde

---

## Portée
- Cette règle s’applique à tout usage nécessitant :
  - Itération rapide
  - Fusion entre versions
  - Traitement vectoriel ou heuristique avancé
- Elle n’est jamais utilisée pour contourner la règle de persistance

## Suivi
- 🔁 Chaque usage de la mémoire temporaire est loggué
- 📝 Chaque résultat est écrit sous forme de fichier dans la bonne arborescence

