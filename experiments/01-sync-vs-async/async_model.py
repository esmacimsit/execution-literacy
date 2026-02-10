import time
import asyncio

async def fake_io():
    await asyncio.sleep(0.1) # Simulate an asynchronous I/O operation by sleeping for 0.1 seconds

async def run(): # special async function that can use await
    start = time.perf_counter()
    tasks = [fake_io() for _ in range(50)] # not running yet
    await asyncio.gather(*tasks) # works like join, event loop keeps running
    end = time.perf_counter()
    print(f"ASYNC total time: {end - start:.2f}s")

if __name__ == "__main__":
    asyncio.run(run()) # event loop

# result is 0.1s