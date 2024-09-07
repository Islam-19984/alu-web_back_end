#!/usr/bin/env python3
import asyncio
import random

async def async_generator():
    """
    Asynchronous generator that yields 10 random numbers between 0 and 10.
    Each number is yielded after an asynchronous wait of 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronous wait
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
