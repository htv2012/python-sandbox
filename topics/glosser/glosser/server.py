import fastapi

app = fastapi.FastAPI()


@app.get("/")
def all_items():
    return {
        "count": 2,
        items[]
    }