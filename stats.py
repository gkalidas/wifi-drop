import json
import os
from config import STATS_FILE

upload_stats = {
    "total_files": 0,
    "total_bytes": 0,
    "total_time": 0.0
}

def load_stats():
    global upload_stats
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as f:
            upload_stats = json.load(f)

def save_stats():
    with open(STATS_FILE, "w") as f:
        json.dump(upload_stats, f, indent=2)

def update_stats(file_size, upload_time):
    upload_stats["total_files"] += 1
    upload_stats["total_bytes"] += file_size
    upload_stats["total_time"] += upload_time
    save_stats()

def print_stats():
    files = upload_stats["total_files"]
    mb = upload_stats["total_bytes"] / (1024 * 1024)
    seconds = upload_stats["total_time"]
    speed = mb / seconds if seconds > 0 else 0
    print(f"📊 Uploaded {files} file(s)")
    print(f"📦 {mb:.2f} MB in {seconds:.2f} sec")
    print(f"⚡ Avg Speed: {speed:.2f} MB/s")
