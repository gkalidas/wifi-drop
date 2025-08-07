# context.py (create a new file if needed)
from contextvars import ContextVar

request_id_var: ContextVar[str] = ContextVar("request_id", default=None)

def get_request_id():
    return request_id_var.get()
