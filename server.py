from fastapi import FastAPI, HTTPException      #core FastAPI
from pydantic import BaseModel, Field       #valida JSON

app = FastAPI(title="Todo List APP")

tasks: list[dict] = []

class TaskSchema(BaseModel):
    text: str = Field(..., example="Estudiar Python")     #los ... quiere decir que el nombre de la tarea es requerido
    done: bool = False

@app.get("/tasks")
def list_task():
    return tasks

#TODO: agregar base de datos real
#sqilite

@app.post("/tasks")
def add_tasks(item: TaskSchema):
    """Crea tarea con ID secuencial"""
    new_tasks = {"id": len(tasks) + 1, **item.dict()} #se coloca el nuevo elemento con la proxima posicion o numero
    tasks.append(new_tasks)
    return new_tasks

@app.get("/tasks/pending")
def pending():
    return[t for t in tasks if not t["done"]]

#Marca la tarea como completada

@app.put("/tasks/{id}/done")
def mark_as_done(id:int):
    for t in tasks:
        if t["id"] == id:
            t["done"] = True
            return t
    raise HTTPException(404, "ID not found")

@app.delete("/tasks/{tid}")
def delete_single_task(tid: int):
    for i, t in enumerate(tasks): #for element, indice in enumerate(tasks)
        if t["id"] == tid:
            tasks.pop(i)
            return{"tarea eliminada": tid}
    raise HTTPException(404, "ID not found") #raise es un return para errores