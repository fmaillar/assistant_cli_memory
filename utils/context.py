# utils/context.py
import os
import json
from pathlib import Path

# Les contextes sont stockés à la racine du projet dans le dossier
# `contextes`. L'ancien chemin "IA_Florian/contextes" n'existait pas et
# entraînait la création involontaire d'un dossier inutile.
CONTEXT_DIR = Path("contextes")
CONTEXT_DIR.mkdir(parents=True, exist_ok=True)

def context_path(nom_session: str) -> Path:
    return CONTEXT_DIR / f"{nom_session}.json"

def load_context(nom_session: str) -> list:
    path = context_path(nom_session)
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return []

def save_context(nom_session: str, messages: list):
    with open(context_path(nom_session), "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)

def list_contexts() -> list:
    return [p.stem for p in CONTEXT_DIR.glob("*.json")]

