import os

UPLOAD_DIR = os.path.join(os.getcwd(), "Uploads")
STATS_FILE = "upload_stats.json"
CHUNK_THRESHOLD_MB = 500

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
