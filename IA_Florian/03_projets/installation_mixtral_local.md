# 🚀 Installation de Mixtral 8x7B quantisé en local avec `llama.cpp`

## 📦 1. Prérequis système

### Sous Linux ou macOS :
```bash
sudo apt update && sudo apt install -y build-essential cmake python3 python3-pip git
```

### Sous macOS avec Homebrew :
```bash
brew install cmake python git
```

---

## 🧰 2. Cloner et compiler `llama.cpp`

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
make LLAMA_CUBLAS=1 # ⚠️ Si GPU NVIDIA CUDA (sinon fais juste `make`)
```

---

## 💾 3. Télécharger Mixtral 8x7B quantisé `.gguf`

Rendez-vous sur : https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF

Téléchargez par exemple :
```
Mixtral-8x7B-Instruct-v0.1.Q4_K_M.gguf
```
Et placez le fichier dans :
```
llama.cpp/models/mixtral/
```

---

## ▶️ 4. Lancer le modèle en ligne de commande

```bash
cd llama.cpp
./main -m models/mixtral/Mixtral-8x7B-Instruct-v0.1.Q4_K_M.gguf -p "Bonjour, que peux-tu faire pour moi ?" -n 300
```

---

## 🔌 5. Utilisation Python via `llama-cpp-python`

```bash
pip install llama-cpp-python
```

### Script minimal :
```python
from llama_cpp import Llama

llm = Llama(model_path="models/mixtral/Mixtral-8x7B-Instruct-v0.1.Q4_K_M.gguf")
res = llm("Explique la souveraineté numérique.", max_tokens=200)
print(res["choices"][0]["text"])
```

---

## 🧠 Intégration avec IA_Florian
- Tu peux appeler ce modèle via un script `src/local_llm_call.py`
- Contextes sélectionnés depuis SQLite ou fichiers `.md`
- Envoi à `llm()` puis récupération des réponses à réinjecter

Souhaites-tu que je t’écrive ce `local_llm_call.py` dans ton repo ?

