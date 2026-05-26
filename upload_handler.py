import os
import asyncio
import aiofiles
from datetime import datetime

from fastapi import UploadFile

from config import UPLOAD_DIR, CHUNK_THRESHOLD_MB, UPLOAD_CHUNK_BYTES
from context import get_request_id

active_uploads = 0


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

    if mb_size > CHUNK_THRESHOLD_MB:
        async with aiofiles.open(save_path, "wb") as f:
            while True:
                chunk = await file.read(UPLOAD_CHUNK_BYTES)
                if not chunk:
                    break
                await f.write(chunk)
    else:
        content = await file.read()
        async with aiofiles.open(save_path, "wb") as f:
            await f.write(content)

    active_uploads -= 1
    end_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"✅ [{request_id}] DONE upload at {end_time} | {file.filename}")
    print(f"    └─ Task ID: {task_id} | Remaining uploads: {active_uploads}\n")

    return {"status": "uploaded", "filename": file.filename}
