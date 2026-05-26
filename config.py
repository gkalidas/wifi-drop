import os

UPLOAD_DIR = os.path.join(os.getcwd(), "Uploads")
STATS_FILE = "upload_stats.json"
CHUNK_THRESHOLD_MB = 5
UPLOAD_CHUNK_BYTES = 2 * 1024 * 1024  # 2 MB per read() call

CERTS_DIR = os.path.join(os.getcwd(), "certs")
CERT_FILE = os.path.join(CERTS_DIR, "server.crt")
KEY_FILE = os.path.join(CERTS_DIR, "server.key")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(CERTS_DIR, exist_ok=True)
