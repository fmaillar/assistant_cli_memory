
from pathlib import Path

def charger_profil_complet(dossier_profil: str = "IA_Florian") -> str:
    chemin_base = Path(dossier_profil) / "00_profil"
    fichiers = sorted(chemin_base.glob("*.md"))

    corpus = []
    titres = set()
    doublons = []

    for fichier in fichiers:
        titre = fichier.stem
        if titre in titres:
            doublons.append(titre)
        else:
            titres.add(titre)
            texte = fichier.read_text(encoding="utf-8").strip()
            corpus.append(f"\n\n# {titre}\n\n{texte}")

    if doublons:
        print(f"⚠️ Doublons détectés dans le profil : {doublons}")

    return "\n".join(corpus)
