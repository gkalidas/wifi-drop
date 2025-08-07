from fastapi import UploadFile
import os
from config import UPLOAD_DIR, CHUNK_THRESHOLD_MB
from rich.progress import Progress
import time
from context import get_request_id
import asyncio


# For metadata check
def check_existing_files(file_list):
    to_upload = []
    skipped = []
    for file in file_list:
        path = os.path.join(UPLOAD_DIR, file.filename)
        if os.path.exists(path) and os.path.getsize(path) == file.size:
            skipped.append(file.filename)
        else:
            to_upload.append(file.filename)
    return to_upload, skipped

import os
import asyncio
from datetime import datetime

from fastapi import UploadFile

from config import UPLOAD_DIR
# from utils import get_request_id

# Global counter (for debug)
active_uploads = 0

# Optional: threshold in MB to chunk large files
CHUNK_THRESHOLD_MB = 5


async def handle_file_upload(file: UploadFile):
    global active_uploads
    save_path = os.path.join(UPLOAD_DIR, file.filename)
    file_size = file.size or 0
    mb_size = file_size / (1024 * 1024)

    request_id = get_request_id()
    start_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    task_id = id(asyncio.current_task())
    
    active_uploads += 1
    print(f"\n🔴 [{request_id}] START upload at {start_time} | {file.filename} ({mb_size:.2f} MB)")
    print(f"    └─ Task ID: {task_id} | Active uploads: {active_uploads}")

    # Optional: simulate delay to visualize concurrency (uncomment to test)
    # await asyncio.sleep(3)

    if mb_size > CHUNK_THRESHOLD_MB:
        chunk_size = 1024 * 500  # 500 KB
        with open(save_path, "wb") as f:
            while True:
                chunk = await file.read(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
    else:
        content = await file.read()
        with open(save_path, "wb") as f:
            f.write(content)

    active_uploads -= 1
    end_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"✅ [{request_id}] DONE upload at {end_time} | {file.filename}")
    print(f"    └─ Task ID: {task_id} | Remaining uploads: {active_uploads}\n")

    return {"status": "uploaded", "filename": file.filename}

