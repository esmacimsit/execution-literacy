import time

def io_work():
    time.sleep(0.3)

def cpu_work():
    sum(i*i for i in range(5_000_000))

def full_workload():
    io_work()
    cpu_work()