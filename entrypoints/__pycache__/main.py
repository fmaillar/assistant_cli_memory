import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

MODE = os.environ.get("IA_FLORIAN_MODE", "documents")  # "classique" ou "documents"

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ["classique", "documents"]:
        MODE = sys.argv[1]

    print(f"🔁 Mode actif : {MODE}")

    if MODE == "classique":
        from main_classique import lancer_session_classique
        lancer_session_classique()

    elif MODE == "documents":
        from main_documents import lancer_session_documents
        lancer_session_documents()

    else:
        print("❌ Mode inconnu. Utilisez 'classique' ou 'documents'.")

