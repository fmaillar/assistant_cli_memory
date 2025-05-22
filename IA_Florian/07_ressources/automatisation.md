# 🤖 Automatisation & scripts


---

## Création récursive de dossiers dans Outlook via VBA
📅 2025-05-19

```vba
Function ObtenirOuCréerDossier(parent, chemin_dossier)
    niveaux = Split(chemin_dossier, "/")
    dossier = parent
    For Each niveau In niveaux
        On Error Resume Next
        Set dossier = dossier.Folders(niveau)
        If dossier Is Nothing Then
            Set dossier = parent.Folders.Add(niveau)
        End If
    Next
    Set ObtenirOuCréerDossier = dossier
End Function
```

---

## Snippet technique #6
📅 2025-05-22

```vba
# Code simulé pour vba numéro 6
```

---

## Snippet technique #11
📅 2025-05-22

```make
# Code simulé pour make numéro 11
```

---

## Snippet technique #12
📅 2025-05-22

```ansible
# Code simulé pour ansible numéro 12
```

---

## Snippet technique #13
📅 2025-05-22

```vba
# Code simulé pour vba numéro 13
```

---

## Snippet technique #18
📅 2025-05-22

```make
# Code simulé pour make numéro 18
```

---

## Snippet technique #19
📅 2025-05-22

```ansible
# Code simulé pour ansible numéro 19
```

---

## Snippet technique #23
📅 2025-05-22

```vba
# Code simulé pour vba numéro 23
```

---

## Snippet technique #28
📅 2025-05-22

```make
# Code simulé pour make numéro 28
```

---

## Snippet technique #29
📅 2025-05-22

```ansible
# Code simulé pour ansible numéro 29
```

---

## Snippet technique #33
📅 2025-05-22

```vba
# Code simulé pour vba numéro 33
```

---

## Snippet technique #38
📅 2025-05-22

```make
# Code simulé pour make numéro 38
```

---

## Snippet technique #39
📅 2025-05-22

```ansible
# Code simulé pour ansible numéro 39
```

---

## Snippet technique #43
📅 2025-05-22

```vba
# Code simulé pour vba numéro 43
```

---

## Snippet technique #48
📅 2025-05-22

```make
# Code simulé pour make numéro 48
```

---

## Snippet technique #49
📅 2025-05-22

```ansible
# Code simulé pour ansible numéro 49
```

---

## Snippet technique #53
📅 2025-05-22

```vba
# Code simulé pour vba numéro 53
```

---

## Snippet technique #58
📅 2025-05-22

```make
# Code simulé pour make numéro 58
```

---

## Snippet technique #59
📅 2025-05-22

```ansible
# Code simulé pour ansible numéro 59
```

---

## Snippet technique #63
📅 2025-05-22

```vba
# Code simulé pour vba numéro 63
```

---

## Snippet technique #68
📅 2025-05-22

```make
# Code simulé pour make numéro 68
```

---

## Snippet technique #69
📅 2025-05-22

```ansible
# Code simulé pour ansible numéro 69
```

---

## Script de tri Outlook automatique par regex
📅 2025-05-19

```vba
Function EvaluerRèglesMail(mail As Outlook.MailItem) As String
    If InStr(mail.Subject, "[O2]") > 0 Then
        EvaluerRèglesMail = "OXYGENE/"
    ElseIf mail.SenderEmailAddress Like "*.segula.fr" Then
        EvaluerRèglesMail = "SEGULA/"
    End If
End Function
```

---

## Logger Python vers fichier et console avec format
📅 2025-05-20

```python
import logging, sys
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("🔍 %(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")
console_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("log.txt", mode='w', encoding='utf-8')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)
```

---

## Extrait réel #8
📅 2025-05-22

```make
# Code réel pour make, cas #8
```

---

## Extrait réel #9
📅 2025-05-22

```ansible
# Code réel pour ansible, cas #9
```

---

## Extrait réel #13
📅 2025-05-22

```vba
# Code réel pour vba, cas #13
```

---

## Extrait réel #18
📅 2025-05-22

```make
# Code réel pour make, cas #18
```

---

## Extrait réel #19
📅 2025-05-22

```ansible
# Code réel pour ansible, cas #19
```

---

## Extrait réel #23
📅 2025-05-22

```vba
# Code réel pour vba, cas #23
```
