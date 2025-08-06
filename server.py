from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

UPLOAD_DIR = os.path.expanduser("~/Uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


# 🧠 File metadata sent by client
class FileMetadata(BaseModel):
    filename: str
    size: int


@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("static/index.html") as f:
        return f.read()


# ✅ Check if files already exist
@app.post("/check-existing")
async def check_existing(files: list[FileMetadata]):
    to_upload = []
    skipped = []

    for file in files:
        path = os.path.join(UPLOAD_DIR, file.filename)
        print(f"🔍 Checking: {file.filename} ({file.size} bytes)")
        if os.path.exists(path) and os.path.getsize(path) == file.size:
            skipped.append(file.filename)
        else:
            to_upload.append(file.filename)

    return {"to_upload": to_upload, "skipped": skipped}


# ✅ Upload the actual file
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    save_path = os.path.join(UPLOAD_DIR, file.filename)
    print(f"🔍 Uploading: {file.filename} ({file.size} bytes)")

    with open(save_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return {"status": "uploaded", "filename": file.filename}
