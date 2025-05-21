import json
import hashlib
import yaml
from pathlib import Path

# === CONFIGURATION ===
INPUT_JSON = Path("IA_Florian/05_archives/conversations/conversations_2025-05-15.json")
OUTPUT_YAML = Path("IA_Florian/cache/conversations_index.yaml")
MAX_CONV = 300  # Limite du nombre de conversations à indexer
MAX_EXTRACT = 2  # Nombre de messages à conserver par conversation
MAX_CHARS = 300  # Longueur maximale par extrait

# === CHARGEMENT DU FICHIER JSON ===
if not INPUT_JSON.exists():
    print(f"❌ Fichier introuvable : {INPUT_JSON}")
    exit(1)

with open(INPUT_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

# === CONSTRUCTION DE L'INDEX ===
index_conversations = []
for i, conv in enumerate(data[:MAX_CONV]):
    messages = conv.get("mapping", {})
    extraits = []
    for msg in messages.values():
        if not isinstance(msg, dict):  # ← évite les None
            continue

        message = msg.get("message")
        if not isinstance(message, dict):
            continue

        contenu = msg.get("message", {}).get("content", {}).get("parts", [])
        if contenu and isinstance(contenu[0], str):
            extrait = contenu[0].replace("\n", " ").strip()
            extraits.append(extrait[:MAX_CHARS])
    if extraits:
        concat = " ".join(extraits[:MAX_EXTRACT])[:800]
        hash_id = hashlib.md5(concat.encode("utf-8")).hexdigest()[:8]
        index_conversations.append({
            "id": f"conv_{hash_id}",
            "extraits": extraits[:MAX_EXTRACT]
        })

# === SAUVEGARDE DU FICHIER YAML ===
OUTPUT_YAML.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_YAML, "w", encoding="utf-8") as f:
    yaml.dump(index_conversations, f, allow_unicode=True, sort_keys=False)

print(f"✅ Index généré avec {len(index_conversations)} entrées → {OUTPUT_YAML}")

