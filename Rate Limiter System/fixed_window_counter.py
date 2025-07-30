from collections import defaultdict
from rate_limiting_strategy import rate_limiting_strategy
from typing import override
from datetime import datetime, timedelta
from request import request


class fixed_window_counter_strategy(rate_limiting_strategy):
    def __init__(self, limit: int, time_period: int):
        self.limit = limit
        self.time_period = timedelta(seconds=time_period)
        self.start_time = datetime.now()
        self.ip_map = defaultdict(int)

    @override
    def rate_limit(self, request: request) -> bool:
        req_time = request.time
        req_ip = request.ip
        time_diff = req_time - self.start_time

        if req_ip not in self.ip_map:
            self.ip_map[req_ip] = self.limit

        if self.time_period < time_diff:
            self.ip_map[req_ip] = self.limit
            self.start_time = datetime.now()

        if self.ip_map[req_ip] > 0:
            self.ip_map[req_ip] -= 1
            return True
        else:
            return False
