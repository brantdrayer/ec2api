import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/joke")
def get_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "text/plain"}

    response = httpx.get(url, headers=headers)
    joke = response.text.strip()

    return {"joke": joke}

