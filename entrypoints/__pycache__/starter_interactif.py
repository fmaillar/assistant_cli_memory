import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
from openai import OpenAI
from utils.contexte_ia_florian import ContexteIAFlorian

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

contexte = ContexteIAFlorian(session_name="florian_auto")
contexte.initialiser_prompt_systeme()
print("🧠 Session IA_Florian interactive – Tape 'exit' pour quitter.\n")

while True:
    try:
        prompt = input("🧠 Vous > ").strip()
        if prompt.lower() in {"exit", "quit"}:
            contexte.sauvegarder()
            print("💾 Session sauvegardée.")
            break

        contexte.ajouter_user(prompt)
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=contexte.exporter(max_messages=8),
                temperature=0.4
            )
            reply = response.choices[0].message.content.strip()
        except openai.RateLimitError as e:
            print("⚠️ API GPT-4o : trop de tokens envoyés. Réduction nécessaire.")
            continue
        except Exception as e:
            reply = f"❌ Erreur lors de l'appel API : {e}"
            print(f"\n{reply}\n")
            continue
        
        print(f"\n🤖 IA > {reply}\n")
        contexte.ajouter_ia(reply)
        contexte.sauvegarder()

    except KeyboardInterrupt:
        print("\n⏹ Interruption. Sauvegarde en cours...")
        contexte.sauvegarder()
        break
