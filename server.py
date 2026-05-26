from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

from config import UPLOAD_DIR, CERT_FILE, KEY_FILE
from utils import get_local_ip, generate_self_signed_cert
from stats import load_stats, upload_stats, print_stats
from upload_handler import check_existing_files, handle_file_upload
from middleware import TimerMiddleware

app = FastAPI()
app.add_middleware(TimerMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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

# Served from root so the Service Worker's scope covers the entire origin
@app.get("/sw.js")
async def serve_sw():
    with open("static/sw.js", "rb") as f:
        return Response(f.read(), media_type="application/javascript")

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
    generate_self_signed_cert(local_ip, CERT_FILE, KEY_FILE)

    url = f"https://{local_ip}:8000"

    border = "*" * 80
    print(border)
    print(f"🚀 Server running at: {url}")
    print(f"📁 Uploads saved to: {UPLOAD_DIR}")
    print(f"⚠️  First visit: tap 'Advanced' → 'Proceed' to accept the self-signed cert")
    print(border)

    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        ssl_keyfile=KEY_FILE,
        ssl_certfile=CERT_FILE,
    )
