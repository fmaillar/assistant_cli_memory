
from drive_sync import list_files_in_folder, authenticate_drive
import re

DRIVE_FOLDER_ID = "1bLROt0vI6YLPKcQ4lJ2YT0SaDtc070jW"
ARCHIVE_PATTERN = re.compile(r"IA_Florian_(\d{4}-\d{2}-\d{2})\.zip")

def rotate_archives(max_keep=7):
    service = authenticate_drive()
    files = list_files_in_folder(DRIVE_FOLDER_ID)

    # Filtrer les archives IA_Florian_*.zip
    archives = [(f['name'], f['id']) for f in files if ARCHIVE_PATTERN.match(f['name'])]

    # Trier par date (extrait du nom)
    sorted_archives = sorted(archives, key=lambda x: x[0], reverse=True)

    to_delete = sorted_archives[max_keep:]
    if not to_delete:
        print("📦 Aucun fichier à supprimer. Rotation non nécessaire.")
        return

    for name, file_id in to_delete:
        service.files().delete(fileId=file_id).execute()
        print(f"🗑 Supprimé : {name} (ID: {file_id})")

if __name__ == "__main__":
    rotate_archives()
