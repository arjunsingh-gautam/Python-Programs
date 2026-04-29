# Returning the result in the order they were submitted
import concurrent.futures
import time
time_start=time.perf_counter()
def do_something(name):
    print(f"Thread-{name} is sleeping for 1 second...")
    time.sleep(1)
    return f"Thread-{name} Done Sleeping!"
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures=[executor.submit(do_something,i) for i in range(10)]
    for future in futures:
        print(future.result())
        
        