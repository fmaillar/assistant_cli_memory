import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
from openai import OpenAI
from utils.contexte_ia_florian import ContexteIAFlorian

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

contexte = ContexteIAFlorian(session_name="florian_auto")
contexte.charger_extraits_conversations("IA_Florian/05_archives/conversations/conversations_2025-05-15.json")

print("🧠 Session IA_Florian interactive – Tape 'exit' pour quitter.\n")

while True:
    try:
        prompt = input("🧠 Vous > ").strip()
        if prompt.lower() in {"exit", "quit"}:
            contexte.sauvegarder()
            print("💾 Session sauvegardée.")
            break

        contexte.ajouter_user(prompt)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=contexte.exporter(),
            temperature=0.4
        )
        reply = response.choices[0].message.content.strip()
        print(f"\n🤖 IA > {reply}\n")
        contexte.ajouter_ia(reply)
        contexte.sauvegarder()

    except KeyboardInterrupt:
        print("\n⏹ Interruption. Sauvegarde en cours...")
        contexte.sauvegarder()
        break