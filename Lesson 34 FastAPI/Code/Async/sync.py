from fastapi import FastAPI

import time

app = FastAPI()


@app.get("/sync")
def sync_api():

    print("Request started")

    time.sleep(5)

    print("Request completed")

    return {
        "message": "sync done"
    }