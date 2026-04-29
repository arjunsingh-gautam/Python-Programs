# Demonstrating a code without using multithreading
import time

start_time=time.perf_counter()

def do_something():
    print("Sleeping for 1 second...")
    time.sleep(1)
    print("Done Sleeping!")

do_something()
do_something()

finish_time=time.perf_counter()
print(f"Finished in {round(finish_time-start_time,2)} second(s)")