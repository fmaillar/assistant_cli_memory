
from pathlib import Path
import os
import json

def load_prompts():
    prompts_dir = Path(__file__).resolve().parent.parent / "IA_Florian" / "01_prompts"
    prompts = []

    for fname in os.listdir(prompts_dir):
        if fname.endswith(".md") and not fname.startswith("index"):
            path = prompts_dir / fname
            with open(path, encoding="utf-8") as f:
                titre = fname.replace("GPT_", "").replace(".md", "").replace("_", " ")
                contenu = f.read()
                prompts.append({
                    "titre": titre.strip(),
                    "prompt": contenu.strip()
                })

    return prompts
