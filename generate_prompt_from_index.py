import yaml
from pathlib import Path
import argparse

# === CONFIGURATION ===
CACHE_PATH = Path("IA_Florian/cache/conversations_index_clean.yaml")
OUTPUT_PROMPT = Path("IA_Florian/cache/prompt_system_conversations.txt")

# === ARGUMENTS CLI ===
parser = argparse.ArgumentParser(description="Générer un prompt system à partir du cache des conversations")
parser.add_argument("--theme", type=str, help="Filtrer les extraits contenant ce mot-clé (ex: paroisse)")
parser.add_argument("--all", action="store_true", help="Injecter tous les extraits")
args = parser.parse_args()

# === CHARGEMENT DU CACHE ===
if not CACHE_PATH.exists():
    print(f"❌ Cache introuvable : {CACHE_PATH}")
    exit(1)

with open(CACHE_PATH, "r", encoding="utf-8") as f:
    index = yaml.safe_load(f)

# === FILTRAGE ===
selected = []

if args.all:
    selected = [item["extrait"] for item in index if item.get("extrait", "").strip()]
elif args.theme:
    mot = args.theme.lower()
    selected = [
        item["extrait"] for item in index
        if mot in item.get("extrait", "").lower()
    ]
else:
    print("❌ Spécifie --all ou --theme 'mot-clé'")
    exit(1)

# === FORMAT DU PROMPT ===
if not selected:
    print("❗ Aucun extrait trouvé.")
    exit(0)

header = f"## 🔁 Extraits de conversations passées injectés automatiquement ({len(selected)} items)\n\n"
body = "\n\n".join(f"- {extrait.strip()}" for extrait in selected)

# === SAUVEGARDE DU PROMPT SYSTEM ===
OUTPUT_PROMPT.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_PROMPT, "w", encoding="utf-8") as f:
    f.write(header + body)

print(f"✅ Prompt généré → {OUTPUT_PROMPT}")

