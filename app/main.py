from fastapi import FastAPI
from api.routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI(title="Todo App")
app.include_router(todo_router)
# register_tortoise(
#     app
# )

@app.get("/")
def index():
    return {"status": "Todo app is running"}