# 1) lanza el backend FastAPI (en otra terminal)
#        uvicorn server:ap --reload
# 2) ejecuta este archivo:
#       windows: py ui.py
#   Gradio abrira automaticamente http://127.0.0.1:7860 con la interfaz.

import gradio as gr #libreria o herramienta para hacer interfaces graficas en python
import requests #libreria para hacer peticiones a un servidor

API = "http://127.0.0.1:8000" #Backend (server)

# ─────────────────────────────────────────────────────────────────────────────
#  FUNCIONES “CLIENTE” QUE HABLAN CON LA API
#  Cada una usa requests para mandar/recibir JSON y devuelve texto
#  que luego se mostrará en la interfaz.
# ─────────────────────────────────────────────────────────────────────────────

def list_tasks():
    try:
        tasks = requests.get(f"{API}/tasks", timeout=5).json() #la ruta tasks se encuentra en server
        return "\n".join(f"{t['id']}: {t['text']}" for t in tasks)
    except Exception as err:
        return f"Ha ocurrido el error: {err}"

def add_task(text: str) -> str:
    """
    POST /tasks con el texto introducido en la caja ‘new_text’.
    Retornamos de nuevo list_tasks() para refrescar el cuadro.
    """
    if not text.strip():                 # evita enviar cadenas vacías
        return "Escribe algo primero"
    try:
        requests.post(
            f"{API}/tasks",
            json={"text": text, "done": False},
            timeout=5
        )
        return list_tasks()              # actualiza la vista
    except Exception as e:
        return f"❌ Error: {e}"


def delete_task(task_id: int | float | None) -> str:
    """
    DELETE /tasks/{id} usando el número que escribe el usuario en ‘del_id’.
    (Gradio pasa Number como float, por eso aceptamos int | float | None)
    """
    if task_id is None:
        return "Ingresa un ID numérico"
    try:
        # Convertimos a int porque el endpoint lo espera así
        requests.delete(f"{API}/tasks/{int(task_id)}", timeout=5)
        return list_tasks()
    except Exception as e:
        return f"❌ Error: {e}"
    
# ─────────────────────────────────────────────────────────────────────────────
#  DEFINICIÓN DE LA INTERFAZ EN BLOQUES GRADIO
#  • gr.Blocks actúa como “contenedor” de componentes.
#  • Cada click se conecta a una función Python.
# ─────────────────────────────────────────────────────────────────────────────

with gr.Blocks(title="To Do GUIDE (Gradio)") as app:
    #titulo estilo Markdown
    gr.Markdown("#To-Do List\nCliente minimal en Gradio")

    # Cuadro de texto multilínea que mostrará las tareas
    tasks_box = gr.Textbox(label="Tareas", lines=10)
    tasks_box.value = list_tasks()    # carga inicial al abrir la página

# ── Fila para AÑADIR tarea ─────────────────────────────────────────────
    with gr.Row():
        new_text = gr.Textbox(label="Nueva tarea")  # entrada de texto
        add_btn = gr.Button("Añadir")              # botón

        # Cuando se hace click en add_btn → llama a add_task()
        #   inputs  = contenido de new_text
        #   outputs = se vuelca la respuesta en tasks_box (refrescado)
        add_btn.click(add_task, inputs=new_text, outputs=tasks_box)

        # ── Fila para ELIMINAR tarea ───────────────────────────────────────────
        with gr.Row():
            del_id = gr.Number(label="ID a borrar", precision=0)  # acepta enteros
            del_btn = gr.Button("Eliminar")

        # Click en eliminar → delete_task(id) → actualiza tasks_box
        del_btn.click(delete_task, inputs=del_id, outputs=tasks_box)

app.launch()