# understanding co-routine and event loop
import asyncio

async def coroutine_function():
    print("Coroutine function started")
    await asyncio.sleep(2)
    print("Coroutine function completed")
    
async def main():
    print("Main function started")
    await coroutine_function()
    print("Main function completed")
    
if __name__ == "__main__":
    asyncio.run(main())