from fastapi import FastAPI
from models import Task

app = FastAPI()

@app.get("/")
def home():
    return {"message": "?? Task Tracker API is running"}

@app.post("/tasks")
def create_task(task: Task):
    return task
