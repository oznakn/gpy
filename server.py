from fastapi import FastAPI, Path
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()

redirections = {
    "123": "https://google.com",
    "345": "https://metu.edu.tr",
    "cclub": "https://cclub.metu.edu.tr"
}

class Item(BaseModel):
    path: str
    url: str

@app.post("/save")
async def save_endpoint(item: Item):
    redirections[item.path] = item.url

    return "Saved"


@app.get("/{path}")
async def redirect_endpoint(path = Path(None)):
    if path in redirections:
        return RedirectResponse(redirections[path])

    return "Not Found"
