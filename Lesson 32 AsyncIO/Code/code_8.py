# In this module we will understand asyncio.io task_group() method and how it can be used to run multiple coroutines concurrently and wait for them to complete.
import asyncio
import time
async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data(1))
        task2 = tg.create_task(fetch_data(2))
    print("Task 1 fully completed")
    print("Task 2 fully completed")
    return [task1.result(), task2.result()]

if __name__ == "__main__":
    t1 = time.perf_counter()

    results = asyncio.run(main())
    print(results)

    t2 = time.perf_counter()
    print(f"Finished in {t2 - t1:.2f} seconds")