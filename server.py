from fastapi import FastAPI, Path
from fastapi.responses import RedirectResponse

app = FastAPI()

redirections = {
    "123": "https://google.com",
    "345": "https://metu.edu.tr",
    "cclub": "https://cclub.metu.edu.tr"
}


@app.get("/{path}")
async def redirect_endpoint(path = Path(None)):
    if path in redirections:
        return RedirectResponse(redirections[path])

    return "Not Found"
