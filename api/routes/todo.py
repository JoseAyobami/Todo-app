from fastapi import APIRouter

todo_router = APIRouter()


@todo_router.get("/")
def all_todos():
    return " Hold"

@todo_router.get("/{key}")
def get_by_id(key: int):
    return " Hold"

@todo_router.post("/")
def create_todo():
    return " Hold"

@todo_router.put("/{key}")
def update_todo():
    return " Hold"

@todo_router.delete("/{key}")
def delete_todo(key: int):
    return " Hold"

