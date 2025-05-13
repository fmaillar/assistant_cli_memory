import os
from pathlib import Path
from openai import OpenAI
from utils.context import load_context, save_context, list_contexts
from utils.tools import print_colored

def charger_profil_ia(dossier_profil: str = "IA_Florian") -> str:
    fichiers_cles = [
        "00_profil/fiche_fonctionnement_fusionnee.md",
        "00_profil/profil_fonctionnel_florian.md",
        "reinjection_memorielle.md",
    ]
    prompt_systeme = ""
    for chemin in fichiers_cles:
        try:
            with open(Path(dossier_profil) / chemin, encoding="utf-8") as f:
                prompt_systeme += f"\n\n==== {chemin} ====\n\n" + f.read()
        except FileNotFoundError:
            continue
    return prompt_systeme.strip()

# === Lecture API key ===
api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPEN_API_KEY")
if not api_key:
    raise RuntimeError("Clé API manquante. Définis OPENAI_API_KEY dans ton environnement.")

client = OpenAI(api_key=api_key)
profil_systeme = charger_profil_ia()
print("✅ Profil IA chargé.")

# === Choix du contexte ===
print("\n📂 Contextes disponibles :")
for i, ctx in enumerate(list_contexts(), 1):
    print(f"  {i}. {ctx}")
choix = input("\n➡️  Choisis un nom de session (existant ou nouveau) : ").strip()
session_name = choix if choix else "default"
messages = load_context(session_name)
print(f"[DEBUG] Contexte chargé ({session_name}) : {len(messages)} messages")

# Ajout du prompt système si absent
if not any(msg["role"] == "system" for msg in messages):
    messages.insert(0, {"role": "system", "content": profil_systeme})

print(f"\n🧠 Assistant IA prêt pour la session : {session_name}. Tape 'exit' pour quitter.\n")

while True:
    try:
        prompt = input("🧠 Vous > ").strip()
        if prompt.lower() in {"exit", "quit", "bye"}:
            save_context(session_name, messages)
            print_colored("💾 Session sauvegardée. À bientôt.", "yellow")
            break

        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.4
        )

        reply = response.choices[0].message.content.strip()
        print_colored(f"\n🤖 IA > {reply}\n", "cyan")

        messages.append({"role": "assistant", "content": reply})
        save_context(session_name, messages)

    except KeyboardInterrupt:
        save_context(session_name, messages)
        print("\n💾 Session interrompue et sauvegardée.")
        break
    except Exception as e:
        print(f"\n[ERREUR] {e}\n")

