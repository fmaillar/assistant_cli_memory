import json
import hashlib
import yaml
from pathlib import Path

# === CONFIGURATION ===
INPUT_JSON = Path("IA_Florian/05_archives/conversations/conversations_2025-05-15.json")
OUTPUT_YAML = Path("IA_Florian/cache/conversations_index_clean.yaml")
MAX_CONV = 40   # conversations maximum à indexer
MAX_EXTRACT = 1 # messages par conversation
MAX_LEN = 250   # longueur maximale de l'extrait
MIN_LEN = 30    # longueur minimale d'un message retenu

# === NOUVELLE LIMITE DE SÉCURITÉ GLOBALE (approximative) ===
MAX_TOTAL_CHARS = 9000  # limite globale (≈ 3000 tokens GPT)
total_chars = 0

# === CHARGEMENT DU JSON ===
if not INPUT_JSON.exists():
    print(f"❌ Fichier introuvable : {INPUT_JSON}")
    exit(1)

with open(INPUT_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

# === EXTRACTION DES EXTRUITS UTILES ===
index_conversations = []
for i, conv in enumerate(data[:MAX_CONV]):
    messages = conv.get("mapping", {})
    extraits = []

    for msg in messages.values():
        if not isinstance(msg, dict):
            continue
        message = msg.get("message")
        if not isinstance(message, dict):
            continue
        contenu = message.get("content", {}).get("parts", [])
        if contenu and isinstance(contenu[0], str):
            texte = contenu[0].replace("\n", " ").strip()
            if len(texte) >= MIN_LEN and not texte.startswith("```"):
                extraits.append(texte)

    if extraits:
        dernier = extraits[-1][:MAX_LEN]
        if total_chars + len(dernier) > MAX_TOTAL_CHARS:
            print(f"🛑 Arrêt à la conversation {i+1} : limite globale atteinte ({total_chars} caractères)")
            break
        
        total_chars += len(dernier)
        hash_id = hashlib.md5(dernier.encode("utf-8")).hexdigest()[:8]
        index_conversations.append({
            "id": f"conv_{hash_id}",
            "extrait": dernier
        })

# === SAUVEGARDE DU CACHE YAML ===
OUTPUT_YAML.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_YAML, "w", encoding="utf-8") as f:
    yaml.dump(index_conversations, f, allow_unicode=True, sort_keys=False)

print(f"✅ Index filtré généré avec {len(index_conversations)} extraits → {OUTPUT_YAML}")

