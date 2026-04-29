# Using ProcessPoolExecutor to run multiple processes concurrently
import concurrent.futures
import time

def do_something(name):
    print(f"Process-{name} is sleeping for 1 second...")
    time.sleep(1)
    print(f"Process-{name} Done Sleeping!")

if __name__ == "__main__":
    time_start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(10):
            executor.submit(do_something,i)
    time_finish=time.perf_counter()
    print(f"Finished in {time_finish-time_start} second(s)")