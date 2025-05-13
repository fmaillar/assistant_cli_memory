import os
from datetime import datetime
from pathlib import Path

def start_session():
    session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = Path("sessions")
    session_dir.mkdir(exist_ok=True)
    with open(session_dir / f"{session_id}.log", "w") as f:
        f.write(f"Session started: {datetime.now().isoformat()}")
    return session_id
