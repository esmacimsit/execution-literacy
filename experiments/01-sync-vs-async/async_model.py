import time
import asyncio

async def fake_io():
    await asyncio.sleep(0.1)

async def run():
    start = time.perf_counter()
    tasks = [fake_io() for _ in range(50)]
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    print(f"ASYNC total time: {end - start:.2f}s")

if __name__ == "__main__":
    asyncio.run(run())
