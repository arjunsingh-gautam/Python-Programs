# Demonstrating multithreading
import time
import threading

start=time.perf_counter()
def do_something():
    print("Sleeping for 1 second...")
    time.sleep(1)
    print("Done Sleeping!")
thread1=threading.Thread(target=do_something)
thread2=threading.Thread(target=do_something)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
finish=time.perf_counter()

print(f"Finished in {finish-start} second(s)")