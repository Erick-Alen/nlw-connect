from typing import Dict


class HttpResponse:
    def __init__(
        self, status_code: int, body: Dict = None, headers: Dict[str, str] = None
    ):
        self.status_code = status_code
        self.headers = headers
        self.body = body
