#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay
beteen 0 and a specified maximum delay and returns the delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay (inclusive)seconds and returns it.
    :param max_delay: Maximum number of seconds to wait.
    :return: The random delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
