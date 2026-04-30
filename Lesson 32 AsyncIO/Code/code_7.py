# In this module we will understand  asyncio.gather() method and how it can be used to run multiple coroutines concurrently and wait for them to complete.
import asyncio
import time

async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1, result2 = await asyncio.gather(task1, task2)
    print("Task 1 fully completed")
    print("Task 2 fully completed")
    return [result1, result2]

if __name__ == "__main__":
    t1 = time.perf_counter()

    results = asyncio.run(main())
    print(results)

    t2 = time.perf_counter()
    print(f"Finished in {t2 - t1:.2f} seconds")