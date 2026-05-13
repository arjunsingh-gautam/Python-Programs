from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

accounts = {
    1: 5000,
    2: 7000,
    3: 1823
}

@app.get("/")
@app.get("/api/accounts")
def get_accounts():
    return accounts


@app.get("/api/account/{id}")
def get_account(id: int):

    if id not in accounts:
        raise HTTPException(
            status_code=404,
            detail="Resource Not Found!"
        )

    return {
        "id": id,
        "balance": accounts[id]
    }


# Custom Exception
class InsufficientBalance(Exception):
    pass


@app.get("/withdraw/account/{id}/{amount}")
def withdraw(id: int, amount: int):

    if id not in accounts:
        raise HTTPException(
            status_code=404,
            detail="Account Not Found!"
        )

    if amount > accounts[id]:
        raise InsufficientBalance()

    accounts[id] -= amount

    return {
        "account_id": id,
        "current_balance": accounts[id],
        "amount_withdrawn": amount
    }


@app.exception_handler(InsufficientBalance)
def withdraw_exception(
    request: Request,
    exc: InsufficientBalance
):

    return JSONResponse(
        status_code=400,
        content={
            "message": "Insufficient Balance for Withdrawal!"
        }
    )
