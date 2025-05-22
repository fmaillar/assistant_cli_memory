# 🔐 Sécurité & durcissement


---

## Créer un mot de passe sécurisé en ligne de commande
📅 2025-05-22

```bash
openssl rand -base64 32
```

---

## Configurer fail2ban pour SSH
📅 2025-05-22

```ini
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 5
```
