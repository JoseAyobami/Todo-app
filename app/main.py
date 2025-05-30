from fastapi import FastAPI
from api.routes.todo import todo_router


app = FastAPI(title="Todo App")
app.include_router(todo_router)

@app.get("/")
def index():
    return {"status": "Todo app is running"}