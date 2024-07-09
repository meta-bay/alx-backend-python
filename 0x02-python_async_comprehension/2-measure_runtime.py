#!/usr/bin/env python3
"""
 2. Run time for four parallel comprehensions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure execution time of of async funtion
    """
    asyncs = [async_comprehension() for _ in range(4)]
    start = time.time()
    await asyncio.gather(*asyncs)
    end = time.time()

    return (end - start)
