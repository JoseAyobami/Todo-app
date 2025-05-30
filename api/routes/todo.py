from fastapi import APIRouter, HTTPException, status
from api.models.todo import Todo
from api.schemas.todo import GetTodo, PostTodo, PutTodo

todo_router = APIRouter()


@todo_router.get("/")
async def all_todos():
    data = Todo.all()
    return await GetTodo.from_queryset(data)

@todo_router.get("/{key}")
async def get_by_id(key: int):
    exists = await Todo.filter(id=key).exists()
    if not exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await Todo.filter(id=key).get()
    return await GetTodo.from_queryset_single(Todo.get(id=key))

@todo_router.post("/")
async def create_todo(body: PostTodo):
    rows = await Todo.create(**body.model_dump(exclude_unset=True))
    return await GetTodo.from_tortoise_orm(rows)

@todo_router.put("/{key}")
async def update_todo(key: int, body: PutTodo):
    data = body.model_dump(exclude_unset=True)
    exists = Todo.filter(id=key).exists()
    if not exists:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await Todo.filter(id=key).update(**data)
    return await GetTodo.from_queryset_single(Todo.get(id=key))

@todo_router.delete("/{key}")
async def delete_todo(key: int):
    exists = await Todo.filter(id=key).exists()
    if not exists:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await Todo.filter(id=key).delete()
    return "Todo deleted successfully"

