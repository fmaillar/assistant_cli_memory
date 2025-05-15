def lancer_session_classique():
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    import os
    from datetime import datetime
    from pathlib import Path
    from openai import OpenAI
    from utils.context import load_context, save_context, list_contexts
    from utils.prompts import load_prompts
    from utils.init_session_IA_Florian import choix_gpt
    from utils.tools import print_colored

    # === Affichage de l’index des prompts disponibles ===
    index_path = Path("IA_Florian/01_prompts/index.md")
    if index_path.exists():
        print("\n📚 Prompts disponibles :")
        print("-" * 100)
        print(f"{'N°':<4} | {'Titre':<40} | Objectif")
        print("-" * 100)
        with open(index_path, encoding="utf-8") as index_file:
            compteur = 1
            for line in index_file:
                if line.startswith("|") and "Titre" not in line:
                    parts = line.strip().split("|")
                    if len(parts) >= 3:
                        titre = parts[1].strip()
                        objectif = parts[2].strip()
                        print(f"{compteur:<4} | {titre:<40} | {objectif}")
                        compteur += 1
        print("-" * 100)
        print("💡 Détails complets dans : IA_Florian/01_prompts/index.md\n")

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

    # === Choix du GPT et du mode de session ===
    prompts = load_prompts()
    session_info = choix_gpt()

    # === Chargement du profil IA et composition du prompt système ===
    profil_systeme = charger_profil_ia()
    prompt_selectionne = session_info if session_info else "Tu es un assistant IA"
    prompt_systeme = f"""
    # 🔐 PROFIL IA FLORIAN ACTIVÉ
    # Version : Consolidée + Prompt

    ## 🧠 Contexte utilisateur
    {profil_systeme.strip()}

    ## 🎯 Rôle attendu
    {prompt_selectionne.strip()}
    """.strip()

    # === Choix du contexte de session ===
    print("\n📂 Contextes disponibles :")
    for i, ctx in enumerate(list_contexts(), 1):
        print(f"  {i}. {ctx}")

    choix = input("\n➡️  Choisis un nom de session (existant ou nouveau) : ").strip()
    # Protection : si nom trop court ou numérique, générer automatiquement un nom valide
    if not choix or len(choix) < 3 or choix.isdigit():
        choix = "session_" + datetime.now().strftime("%Y%m%d_%H%M")
        print(f"⚠️  Nom de session invalide ou trop court. Session renommée : {choix}")
    session_name = choix

    messages = load_context(session_name)
    print(f"[DEBUG] Contexte chargé ({session_name}) : {len(messages)} messages")

    # Ajout du prompt système si absent
    if not any(msg["role"] == "system" for msg in messages):
        messages.insert(0, {
            "role": "system",
            "content": [{"type": "text", "text": prompt_systeme}]
        })

    print(f"\n🧠 Assistant IA prêt pour la session : {session_name}. Tape 'exit' pour quitter.\n")

    while True:
        try:
            prompt = input("🧠 Vous > ").strip()
            if prompt.lower() in {"exit", "quit", "bye"}:
                save_context(session_name, messages)
                print_colored("💾 Session sauvegardée. À bientôt.", "yellow")
                break

            messages.append({
                "role": "user",
                "content": [{"type": "text", "text": prompt}]
            })

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.4
            )

            reply = response.choices[0].message.content.strip()
            print_colored(f"\n🤖 IA > {reply}\n", "cyan")

            messages.append({
                "role": "assistant",
                "content": [{"type": "text", "text": reply}]
            })
            save_context(session_name, messages)

        except KeyboardInterrupt:
            save_context(session_name, messages)
            print("\n💾 Session interrompue et sauvegardée.")
            break
        except Exception as e:
            print(f"\n[ERREUR] {e}\n")
