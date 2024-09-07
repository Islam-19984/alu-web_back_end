#!/usr/bin/env python3
import time
import asyncio
from concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns the average time per coroutine.
    :param n: Number of times to call wait_n.
    :param max_delay: The maximum delay for each call.
    :return: Average time per coroutine.
    """
    # Start measuring time
    start_time = time.perf_counter()

    # Run wa
