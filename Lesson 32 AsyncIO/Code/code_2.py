# Writing 2 co-routines and running them using only awain in main co-routine
import asyncio
import time
async def coroutine1():
    print("Coroutine 1 started")
    await asyncio.sleep(1)
    print("Coroutine 1 completed")
async def coroutine2():
    print("Coroutine 2 started")
    await asyncio.sleep(2)
    print("Coroutine 2 completed")
    
async def main():
    print("Main function started")
    await coroutine1()
    await coroutine2()
    print("Main function completed")
    
if __name__ == "__main__":
    start_time=time.perf_counter()
    asyncio.run(main())
    finish_time=time.perf_counter()
    print(f"Finished in {round(finish_time-start_time,2)} second(s)")
    
# Output:
# Main function started
# Coroutine 1 started   
# Coroutine 1 completed
# Coroutine 2 started
# Coroutine 2 completed
# Main function completed
# Finished in 3.01 second(s)


# No concurrency benefit as we are scheduling the co-routine and running the co-routinne and there is no other scheduled co-routine to run while the first co-routine is sleeping. 
# Because it act same as if we are running the co-routines sequentially. So we need to schedule the co-routines and then run them using await. We will see that in the next code snippet.