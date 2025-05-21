
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io

# Scopes requis pour lire/écrire dans Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate_drive():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('drive', 'v3', credentials=creds)

def upload_file(local_path, folder_id):
    service = authenticate_drive()
    file_metadata = {
        'name': os.path.basename(local_path),
        'parents': [folder_id]
    }
    media = MediaFileUpload(local_path, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"✅ Fichier uploadé avec ID : {file.get('id')}")
    return file.get('id')

def download_file(file_id, destination_path):
    service = authenticate_drive()
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(destination_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"⬇️ Téléchargement {int(status.progress() * 100)}%.")
    print(f"✅ Fichier téléchargé vers : {destination_path}")

def list_files_in_folder(folder_id):
    service = authenticate_drive()
    results = service.files().list(q=f"'{folder_id}' in parents and trashed=false",
                                   spaces='drive',
                                   fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print("📭 Aucun fichier trouvé.")
        return []
    for item in items:
        print(f"📄 {item['name']} (ID: {item['id']})")
    return items
