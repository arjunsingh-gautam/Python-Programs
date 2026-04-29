# Using ThreadPoolExecutor to run multiple threads concurrently
import concurrent.futures
import time
time_start=time.perf_counter()
def do_something(name):
    print(f"Thread-{name} is sleeping for 1 second...")
    time.sleep(1)
    print(f"Thread-{name} Done Sleeping!")

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for i in range(10):
        executor.submit(do_something,i)
time_finish=time.perf_counter()
print(f"Finished in {time_finish-time_start} second(s)")