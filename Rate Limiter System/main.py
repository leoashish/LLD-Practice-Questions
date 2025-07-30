from fixed_window_counter import fixed_window_counter_strategy
from sliding_window_counter import sliding_window_counter_strategy
from request import request
import time


##
"""Design a Rate-Limiting System that restricts the number of API
requests a user can make within a given time window.
The system should support different rate-limiting algorithms,
allowing them to be configured and extended easily."""
# IP based rate limiting
# Implement the fixed counter and sliding window conter algo


def main():
    fixed_window_rate_limiter = fixed_window_counter_strategy(2, 2)
    sliding_window_counter_strategy_1 = sliding_window_counter_strategy(2, 3)
    print(fixed_window_rate_limiter.rate_limit(request(1)))

    print(fixed_window_rate_limiter.rate_limit(request(1)))

    print(fixed_window_rate_limiter.rate_limit(request(1)))

    print(fixed_window_rate_limiter.rate_limit(request(2)))

    print(fixed_window_rate_limiter.rate_limit(request(2)))

    time.sleep(2)
    print(fixed_window_rate_limiter.rate_limit(request(2)))

    print(fixed_window_rate_limiter.rate_limit(request(2)))

    print("Sliding window: ")

    print(sliding_window_counter_strategy_1.rate_limit(request(1)))

    print(sliding_window_counter_strategy_1.rate_limit(request(1)))

    print(sliding_window_counter_strategy_1.rate_limit(request(1)))

    print(sliding_window_counter_strategy_1.rate_limit(request(2)))

    print(sliding_window_counter_strategy_1.rate_limit(request(2)))

    print(sliding_window_counter_strategy_1.rate_limit(request(2)))

    print(sliding_window_counter_strategy_1.rate_limit(request(2)))


if __name__ == "__main__":
    main()
