import os
import redis

from fastapi import FastAPI, Path
from fastapi.responses import RedirectResponse

from pydantic import BaseModel

app = FastAPI()
r = redis.Redis(
  host= os.environ.get('REDIS_HOST'),
  port= os.environ.get('REDIS_PORT'),
  password= os.environ.get('REDIS_PASS'),
)

class Item(BaseModel):
    path: str
    url: str

@app.post("/save")
async def save_endpoint(item: Item):
    r.set(item.path, item.url)

    return "Saved"

@app.get("/{path}")
async def redirect_endpoint(path = Path(None)):
    url = r.get(path)
    if url is not None:
        return RedirectResponse(url.decode("utf-8"))

    return "Not Found"
