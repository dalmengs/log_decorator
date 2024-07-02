class CustomException(Exception):
    status_code: int = 400
    msg: str

    def __init__(self, msg):
        self.msg = msg