import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import os
from openai import OpenAI
from utils.contexte_ia_florian import ContexteIAFlorian

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
contexte = ContexteIAFlorian(session_name="florian_auto")

contexte.ajouter_user("Montre-moi les projets actifs liés à la paroisse.")
response = client.chat.completions.create(
    model="gpt-4o",
    messages=contexte.exporter(),
    temperature=0.4
)
print(response.choices[0].message.content)
contexte.sauvegarder()

