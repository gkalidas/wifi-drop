from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

from config import UPLOAD_DIR
from utils import get_local_ip
from stats import load_stats, upload_stats, print_stats
from upload_handler import check_existing_files, handle_file_upload
from middleware import TimerMiddleware  # ✅ NEW

app = FastAPI()
app.add_middleware(TimerMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use exact IP in production
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")


class FileMetadata(BaseModel):
    filename: str
    size: int

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("static/index.html") as f:
        return f.read()

@app.post("/check-existing")
async def check_existing(files: list[FileMetadata]):
    to_upload, skipped = check_existing_files(files)
    return {"to_upload": to_upload, "skipped": skipped}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return await handle_file_upload(file)

if __name__ == "__main__":
    import uvicorn

    load_stats()
    print_stats()
    local_ip = get_local_ip()
    url = f"http://{local_ip}:8000"

    # total_mb = upload_stats["total_bytes"] / 1024 / 1024
    # total_time = upload_stats["total_time"]
    # avg_speed = total_mb / total_time if total_time > 0 else 0

    border = "*" * 80
    print(border)
    print(f"🚀 Server running at: {url}")
    print(f"📁 Uploads saved to: {UPLOAD_DIR}")
    # print(f"📊 Uploaded {upload_stats['total_files']} file(s)")
    # print(f"📦 {total_mb:.2f} MB in {total_time:.2f} sec")
    # print(f"⚡ Avg Speed: {avg_speed:.2f} MB/s")
    print(border)

    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
