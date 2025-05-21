
import os
import re
from datetime import datetime, timedelta

ARCHIVE_PATTERN = re.compile(r"IA_Florian_(\d{4}-\d{2}-\d{2})\.zip")

def nettoyage_archives_locales(max_age_days=7):
    now = datetime.now()
    for filename in os.listdir("."):
        match = ARCHIVE_PATTERN.match(filename)
        if match:
            date_str = match.group(1)
            try:
                file_date = datetime.strptime(date_str, "%Y-%m-%d")
                if (now - file_date).days > max_age_days:
                    os.remove(filename)
                    print(f"🧹 Supprimé : {filename}")
            except ValueError:
                continue

if __name__ == "__main__":
    nettoyage_archives_locales()
