from typing import Dict


class HttpRequest:
    def __init__(self, body: Dict = None, headers: Dict = None, param: Dict = None):
        self.param = param
        self.headers = headers
        self.body = body
