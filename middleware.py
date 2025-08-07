# middleware.py
from starlette.middleware.base import BaseHTTPMiddleware
from uuid import uuid4
import time
from stats import update_stats

from context import request_id_var

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Set unique request ID in context
        request_id = str(uuid4())
        request_id_var.set(request_id)

        start = time.time()
        response = await call_next(request)
        duration = time.time() - start

        if request.url.path == "/upload":
            content_length = request.headers.get("content-length")
            if content_length and content_length.isdigit():
                received_bytes = int(content_length)
                print(f"[{request_id}] /upload: {received_bytes / (1024*1024):.2f} MB in {duration:.2f} sec")
                update_stats(received_bytes, duration)

        return response
