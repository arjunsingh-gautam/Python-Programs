# Demonstrationg multiprocessing in Python using the multiprocessing library
import multiprocessing
import time

def do_something(name):
    print(f"Process-{name} is sleeping for 1 second...")
    time.sleep(1)
    print(f"Process-{name} Done Sleeping!")
    
if __name__=="__main__":
    t1=time.perf_counter()
    processes=[]
    for i in range(10):
        p=multiprocessing.Process(target=do_something,args=(i,))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    t2=time.perf_counter()
    print(f"Finished in {t2-t1} second(s)")
        
