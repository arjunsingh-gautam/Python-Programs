# Using blocking statement inside async code: Result breaks event loop

import asyncio
import time

async def couroutine_with_block_statement(name,seconds):
    print(f"Coroutine-{name} started and will be sleeping for {seconds} seconds(s)")
    time.sleep(seconds) # Blocking statement: uses the seconds parameter
    print(f"Coroutine-{name} resumed")
    
async def main():
    task1=asyncio.create_task(couroutine_with_block_statement("A",2))
    task2=asyncio.create_task(couroutine_with_block_statement("B",3))
    await task1
    print("Task-1 finished")
    await task2
    print("Task-2 finished")
    
if __name__=="__main__":
    start_time=time.perf_counter()
    asyncio.run(main())
    finish_time=time.perf_counter()
    print(f"Module finished after:{finish_time-start_time} second(s)")
    