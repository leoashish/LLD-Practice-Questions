from collections import defaultdict, deque
from rate_limiting_strategy import rate_limiting_strategy
from typing import override
from datetime import datetime, timedelta
from request import request


class sliding_window_counter_strategy(rate_limiting_strategy):
    def __init__(self, limit: int, time_period: int):
        self.limit = limit
        self.time_period = timedelta(seconds=time_period)
        self.last_request_map: dict[int, deque[datetime]] = {}

    @override
    def rate_limit(self, request: request) -> bool:
        req_time = request.time
        req_ip = request.ip

        last_request_deque = self.last_request_map.get(req_ip, deque([]))

        # print(last_request_deque)
        while last_request_deque and (
            req_time - last_request_deque[0] > self.time_period
        ):
            print(req_time - last_request_deque[0])
            last_request_deque.popleft()

        if len(last_request_deque) < self.limit:
            last_request_deque.append(req_time)
            self.last_request_map[req_ip] = last_request_deque
            return True

        self.last_request_map[req_ip] = last_request_deque

        return False
