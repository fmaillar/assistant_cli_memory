# 🤖 Règles d’automatisation implicite – Assistant IA Florian

Ce fichier documente les comportements IA activés automatiquement, sans validation systématique.  
Ces règles visent à prolonger la logique de pilotage par objectif sans surcharge cognitive.

---

## ✅ Règles actives

### 🎯 1. Objectif inactif depuis 10 jours
- 📌 Condition : aucune trace d’évolution (fiche, plan, journal)
- 🤖 Action : proposition de micro-action ou recentrage doux

### 📘 2. Intention non abordée depuis 15 jours
- 📌 Condition : aucune occurrence de l’intention dans les journaux ou modules
- 🤖 Action : reformulation ou suggestion de clarification

### 🧾 3. Absence de bilan ou journal depuis 20 jours
- 📌 Condition : pas d’entrée dans `bilans_mensuels.md`, `journal_*`
- 🤖 Action : génération d’un bloc `bilan_rapide.md` à insérer manuellement

### 🗃 4. Surcharge structurelle
- 📌 Condition : plus de 10 fichiers non classés ou redondants dans un même dossier
- 🤖 Action : suggestion de fusion, renommage ou simplification

### ❓ 5. Module orphelin
- 📌 Condition : module créé sans contenu ni lien actif depuis plus de 30 jours
- 🤖 Action : suggestion de suppression ou reformulation d’usage

### ⚙️ 6. Exécution sans validation
- 📌 Condition : Sous-tâches évidentes ou déjà validées dans la stratégie de Florian
- 🤖 Action : Exécution automatique sans demander de validation pour les sous-étapes simples ou récurrentes

---

## 🧠 Note

Aucune action destructive ou irréversible n’est exécutée.  
Vous pouvez désactiver, suspendre ou compléter ces règles à tout moment.

<!-- 🟡 Contenu fusionné depuis ./ doublon -->

[...]