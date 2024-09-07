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

    # Run wait_n asynchronously and wait for it to finish
    asyncio.run(wait_n(n, max_delay))

    # Stop measuring time
    end_time = time.perf_counter()

    # Calculate the total elapsed time
    total_time = end_time - start_time

    # Return the average time per coroutine
    return total_time / n
