# Automatisation Outlook – IA_Florian

## 📥 Règles de tri automatique (mod_TriRegexComplet.bas)
- Déplacement des mails [CAF IT], [INCxxxx], easyvista vers `IT/`
- Adresse CSE Reichshoffen → `COMM/CSE`
- Mails SEGULA → `SEGULA/`
- Suppression automatique des mails Teams, Oracle et Planner
- Identification des projets : OXYGENE, REGIOLIS_H2, LEX, etc.
- Classification basée sur le premier tag `[xxx]` dans l'objet

## 📤 Scripts associés
- `CorrigerCaracteresAccentues` pour encoder proprement les accents depuis VBA
- `EvaluerRèglesMail` = moteur de classification des projets par objet

## 🔁 Synchronisation avec `log_sauvegardes.md` automatique à chaque routine