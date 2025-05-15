import os
import re

def index_prompts(prompts_dir="IA_Florian/01_prompts", output_file="IA_Florian/01_prompts/index.md"):
    index = []
    for fname in sorted(os.listdir(prompts_dir)):
        if not fname.endswith(".md") or fname.startswith("README"):
            continue

        path = os.path.join(prompts_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        prompts = re.findall(r"## 🔹 (.+?)\n+### 🎯 Objectif\n+(.+?)\n", content)
        for title, objective in prompts:
            index.append((title.strip(), objective.strip(), fname))

    # Création de l'index markdown
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("# 📇 Index des Prompts – IA_Florian\n\n")
        out.write("## Prompts disponibles\n\n")
        out.write("| Titre | Objectif | Fichier source |\n")
        out.write("|-------|----------|----------------|\n")
        for title, obj, file in index:
            out.write(f"| {title} | {obj} | [{file}]({file}) |\n")

    print(f"✅ Index généré avec {len(index)} prompts dans {output_file}")

if __name__ == "__main__":
    index_prompts()