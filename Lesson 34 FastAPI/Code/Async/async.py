from fastapi import FastAPI

import asyncio

app = FastAPI()


@app.get("/async")
async def async_api():

    print("Request started")

    await asyncio.sleep(5)

    print("Request completed")

    return {
        "message": "async done"
    }