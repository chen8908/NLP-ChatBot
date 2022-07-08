
from fastapi import Header, HTTPException
from security import secret_token

async def access(x_token: str = Header(...)):
    if x_token != secret_token:
        raise HTTPException(status_code=400, detail='Invalid x-token')
    return 200
