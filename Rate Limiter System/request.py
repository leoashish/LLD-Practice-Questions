from datetime import datetime


class request:
    def __init__(self, ip):
        self.time = datetime.now()
        self.ip = ip
