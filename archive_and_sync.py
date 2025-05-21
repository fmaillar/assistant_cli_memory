
import os
import zipfile
import datetime
from drive_sync import upload_file

# Paramètres
SOURCE_DIR = "IA_Florian"
DESTINATION_ZIP = f"IA_Florian_{datetime.datetime.now().strftime('%Y-%m-%d')}.zip"
DRIVE_FOLDER_ID = "1bLROt0vI6YLPKcQ4lJ2YT0SaDtc070jW"  # ID fourni par l'utilisateur

def zip_directory(source_dir, zip_path):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, source_dir)
                zipf.write(full_path, rel_path)

def main():
    print(f"🗜 Archivage de {SOURCE_DIR} en {DESTINATION_ZIP}...")
    zip_directory(SOURCE_DIR, DESTINATION_ZIP)
    print(f"✅ Archive créée : {DESTINATION_ZIP}")

    print("🚀 Envoi de l'archive vers Google Drive...")
    upload_file(DESTINATION_ZIP, DRIVE_FOLDER_ID)

if __name__ == "__main__":
    main()
