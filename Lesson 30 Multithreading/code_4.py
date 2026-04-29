# Running multiple threads
import threading
import time

start=time.perf_counter()

def do_something(name,seconds):
    print(f"Thread-{name} is sleeping for {seconds} seconds...")
    time.sleep(seconds)
    print(f"Thread-{name} Done Sleeping!")

threads=[]
for i in range(10):
    t=threading.Thread(target=do_something,args=(i,1.5))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish=time.perf_counter()

print(f"Finished in {finish-start} second(s)")





