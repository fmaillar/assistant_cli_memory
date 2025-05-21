
sync_drive:
	python3 -c "from drive_sync import upload_file; upload_file('IA_Florian_2025-05-21.zip', 'VOTRE_FOLDER_ID_DRIVE')"

archive_sync:
	python3 archive_and_sync.py

log:
	@echo "📘 Historique des sauvegardes :"
	@cat log_sauvegardes.md

rotate:
	python3 rotation_archives.py

archive_sync_rotate:
	python3 archive_and_sync.py
	python3 rotation_archives.py

clean_local:
	python3 nettoyage_local.py

routine_hebdo:
	python3 archive_and_sync.py
	python3 rotation_archives.py
	python3 nettoyage_local.py
