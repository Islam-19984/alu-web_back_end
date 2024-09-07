#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine wait_n that spawns multiple
instances of wait_random, waits for their completion, and returns a sorted
list of the delays.

The wait_random function is imported from the 0-basic_async_syntax module.
"""

import asyncio
from typing import List
from _0_basic_async_syntax import wait_random  # Adjust the module name as needed

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    
    This function creates n asynchronous tasks that each call wait_random 
    with max_delay. It waits for all the tasks to complete and collects their 
    results. The function returns a list of these delays in ascending order.

    :param n: Number of times to call wait_random.
    :param max_delay: The maximum delay for each call.
    :return: List of delays in ascending order.
    """
    # List of tasks for each wait_random call
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    # Wait for all tasks to complete and collect their results
    delays = await asyncio.gather(*tasks)
    
    return sorted(delays)
