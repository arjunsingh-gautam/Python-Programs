# using map to run multiple threads
import concurrent.futures
import time
time_start=time.perf_counter()
def do_something(name):
    print(f"Thread-{name} is sleeping for 1 second...")
    time.sleep(1)
    return f"Thread-{name} Done Sleeping!"
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results=executor.map(do_something,range(10))
for result in results:
    print(result)