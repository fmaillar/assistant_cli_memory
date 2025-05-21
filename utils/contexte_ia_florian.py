from pathlib import Path
import json
from utils.charger_profil_complet import charger_profil_complet
from utils.init_session_IA_Florian import choix_gpt
from utils.context import load_context, save_context
from utils.prompts import load_prompts

class ContexteIAFlorian:
    def __init__(self, session_name="session_auto", profil_path="IA_Florian"):
        self.session_name = session_name
        self.profil_path = Path(profil_path)
        self.prompts = load_prompts()
        self.messages = load_context(self.session_name)
        if not any(m["role"] == "system" for m in self.messages):
            self.initialiser_prompt_systeme()

    def initialiser_prompt_systeme(self):
        profil_systeme = charger_profil_complet(dossier_profil=str(self.profil_path))
        prompt_selectionne = choix_gpt() or "Tu es un assistant IA"

        prompt_systeme = f"""
# 🔐 PROFIL IA FLORIAN ACTIVÉ
# Version : Consolidée + Prompt

## 🧠 Contexte utilisateur
{profil_systeme.strip()}

## 🎯 Rôle attendu
{prompt_selectionne.strip()}
""".strip()

        # === Ajout du prompt conversations, si disponible
        conversations_prompt_path = self.profil_path / "cache/prompt_system_conversations.txt"
        if conversations_prompt_path.exists():
            with open(conversations_prompt_path, "r", encoding="utf-8") as f:
                prompt_conversations = f.read().strip()
            if prompt_conversations:
                prompt_systeme += f"\n\n{prompt_conversations}"
                print("🧠 Prompt conversations injecté dans le système.")
        else:
            print("ℹ️ Aucun prompt conversations trouvé.")

        self.messages.insert(0, {
            "role": "system",
            "content": prompt_systeme
        })

    def ajouter_user(self, texte):
        self.messages.append({"role": "user", "content": texte})

    def ajouter_ia(self, texte):
        self.messages.append({"role": "assistant", "content": texte})

    def sauvegarder(self):
        save_context(self.session_name, self.messages)

    def exporter(self):
        return self.messages
 
