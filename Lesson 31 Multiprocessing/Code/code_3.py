# Using a seconds iterator where we pass diferent seconds to the function and see how much time it takes to run the function using multiprocessing.
import concurrent.futures
import time
def do_something(seconds):
    print(f"Sleeping for {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done Sleeping for {seconds} second(s)!"
if __name__ == "__main__":
    time_start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs=[5,4,3,2,1]
        results=executor.map(do_something,secs)
    for result in results:
        print(result)
    time_finish=time.perf_counter()
    print(f"Finished in {time_finish-time_start} second(s)")