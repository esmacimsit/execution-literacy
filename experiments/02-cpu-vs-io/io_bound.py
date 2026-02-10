import time
import asyncio

def fake_io():
    time.sleep(0.1)  # io behavior


def io_sync():
    start = time.perf_counter()
    for _ in range(50):
        fake_io()
    print("IO SYNC:", time.perf_counter() - start)


async def io_async():
    async def task():
        await asyncio.sleep(0.1)

    start = time.perf_counter()
    await asyncio.gather(*(task() for _ in range(50)))
    print("IO ASYNC:", time.perf_counter() - start)


if __name__ == "__main__":
    io_sync()
    asyncio.run(io_async())
