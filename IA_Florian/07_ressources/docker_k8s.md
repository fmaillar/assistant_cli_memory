# 🐳 Docker & Kubernetes


---

## Démarrer un conteneur avec volume monté
📅 2025-05-22

```bash
docker run -v $(pwd)/data:/data --name mon_conteneur -it ubuntu bash
```

---

## Créer un pod simple en YAML
📅 2025-05-22

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mon-pod
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80
```
