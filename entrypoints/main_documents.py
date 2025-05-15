def lancer_session_documents():
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    from utils.init_session_IA_Florian import initialiser_session_ia
    import openai
    import time
    import os
    from pathlib import Path

    openai.api_key = os.getenv("OPEN_API_KEY")

    def lancer_assistant():
        print("[IA_Florian] Initialisation de la session...")
        system_message = initialiser_session_ia()[0]["content"]

        assistant = openai.beta.assistants.create(
            name="IA_Florian-Terminal",
            instructions=system_message,
            model="gpt-4o",
            tools=[{"type": "file_search"}]
        )
        thread = openai.beta.threads.create()

        print("[IA_Florian] Assistant interactif prêt. Tape 'exit' pour quitter.")

        while True:
            commande = input("ia> ").strip()

            if commande == "exit":
                print("[IA_Florian] Fin de session.")
                break

            elif commande == "liste_fichiers":
                fichiers = openai.files.list()
                print("\n=== Fichiers stockés dans l'API OpenAI ===")
                for f in fichiers.data:
                    print(f"- {f.id}  |  nom: {f.filename}  |  taille: {f.bytes} octets  |  créé: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(f.created_at))}")
                    print(f"  → pour le reprendre : ia> reprend {f.id}")
                    print(f"  → pour le supprimer : ia> supprime {f.id}\n")

            elif commande.startswith("charge "):
                chemin = commande[len("charge "):].strip()
                if not Path(chemin).exists():
                    print("  → Fichier introuvable.")
                    continue

                print(f"  → Upload de '{chemin}'...")
                upload = openai.files.create(
                    file=open(chemin, "rb"),
                    purpose="assistants"
                )
                file_id = upload.id
                print(f"    Fichier ID : {file_id}")

                print("  → Envoi à l'assistant...")
                openai.beta.threads.messages.create(
                    thread_id=thread.id,
                    role="user",
                    content="Voici un fichier à analyser. Résume-le ou extrais les informations clés.",
                    file_ids=[file_id]
                )

            elif commande.startswith("reprend "):
                file_id = commande[len("reprend "):].strip()
                print(f"  → Réutilisation du fichier {file_id}...")
                openai.beta.threads.messages.create(
                    thread_id=thread.id,
                    role="user",
                    content="Voici un fichier précédemment uploadé. Merci de l'analyser ou de compléter l'échange.",
                    file_ids=[file_id]
                )

            elif commande.startswith("supprime "):
                file_id = commande[len("supprime "):].strip()
                try:
                    openai.files.delete(file_id)
                    print(f"  → Fichier {file_id} supprimé avec succès.")
                except Exception as e:
                    print(f"  → Erreur lors de la suppression : {e}")

            else:
                openai.beta.threads.messages.create(
                    thread_id=thread.id,
                    role="user",
                    content=commande
                )

            run = openai.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant.id
            )

            print("  → Attente de la réponse IA...")
            while True:
                run_status = openai.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id
                )
                if run_status.status == "completed":
                    break
                elif run_status.status in ["failed", "cancelled"]:
                    print("  → Erreur d'exécution.")
                    return
                time.sleep(2)

            messages = openai.beta.threads.messages.list(thread_id=thread.id)
            print("\n=== Réponse IA ===")
            print(messages.data[0].content[0].text.value)

    if __name__ == "__main__":
        lancer_assistant()
