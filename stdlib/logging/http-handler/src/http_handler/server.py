from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Sample endpoint that returns a welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI HTTP server!"}


# A POST endpoint that accepts JSON data
class LogRecord(BaseModel):
    asctime: str
    levelno: int
    message: str


@app.post("/log/")
def accept_log(log_record: LogRecord):
    print(log_record)
    return {
        "asctime": log_record.asctime,
        "levelno": log_record.levelno,
        "message": log_record.message,
    }


# A GET endpoint with path parameters
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}
