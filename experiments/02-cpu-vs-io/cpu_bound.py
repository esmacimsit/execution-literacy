import time
import asyncio

def cpu_work(n: int): # cpu simulation
    x = 0
    for i in range(n):
        x += i * i
    return x


def cpu_sync(): # sync
    start = time.perf_counter()
    for _ in range(4):
        cpu_work(20_000_000)
    print("CPU SYNC:", time.perf_counter() - start)


async def cpu_async(): # async
    async def task(): 
        cpu_work(20_000_000)

    start = time.perf_counter()
    await asyncio.gather(*(task() for _ in range(4)))
    print("CPU ASYNC:", time.perf_counter() - start)


if __name__ == "__main__":
    cpu_sync()
    asyncio.run(cpu_async())

# results:
# CPU SYNC: ~2.3s
# CPU ASYNC: ~2.1s