# Now scheduling tasks using asyncio and see how much time it takes to download the images using asyncio.
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
    task1=asyncio.create_task(coroutine1())
    task2=asyncio.create_task(coroutine2())
    await task1
    await task2
    print("Main function started")
    
if __name__ == "__main__":
    start_time=time.perf_counter()
    asyncio.run(main())
    finish_time=time.perf_counter()
    print(f"Finished in {round(finish_time-start_time,2)} second(s)")
    
# Output:
# Coroutine 1 started   
# Coroutine 2 started
# Coroutine 1 completed
# Coroutine 2 completed
# Main function started
# Finished in 2.01 second(s)