import tkinter as tk
from tkinter import messagebox

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - {self.cantidad} unidades - ${self.precio:.2f}"

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📦 Control de Inventario")
        self.inventario = {}

        # Entradas
        self.nombre_var = tk.StringVar()
        self.cantidad_var = tk.IntVar()
        self.precio_var = tk.DoubleVar()

        tk.Label(root, text="Nombre:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.nombre_var).grid(row=0, column=1)

        tk.Label(root, text="Cantidad:").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.cantidad_var).grid(row=1, column=1)

        tk.Label(root, text="Precio:").grid(row=2, column=0)
        tk.Entry(root, textvariable=self.precio_var).grid(row=2, column=1)

        # Botones
        tk.Button(root, text="Agregar", command=self.agregar_producto).grid(row=3, column=0)
        tk.Button(root, text="Actualizar", command=self.actualizar_producto).grid(row=3, column=1)
        tk.Button(root, text="Eliminar", command=self.eliminar_producto).grid(row=4, column=0)
        tk.Button(root, text="Mostrar", command=self.mostrar_inventario).grid(row=4, column=1)

        # Lista
        self.lista = tk.Listbox(root, width=50)
        self.lista.grid(row=5, column=0, columnspan=2)

    def agregar_producto(self):
        nombre = self.nombre_var.get()
        cantidad = self.cantidad_var.get()
        precio = self.precio_var.get()
        if nombre in self.inventario:
            messagebox.showwarning("Ya existe", "El producto ya está en el inventario.")
        else:
            self.inventario[nombre] = Producto(nombre, cantidad, precio)
            self.mostrar_inventario()

    def actualizar_producto(self):
        nombre = self.nombre_var.get()
        if nombre in self.inventario:
            self.inventario[nombre].cantidad = self.cantidad_var.get()
            self.inventario[nombre].precio = self.precio_var.get()
            self.mostrar_inventario()
        else:
            messagebox.showerror("No encontrado", "Producto no existe.")

    def eliminar_producto(self):
        nombre = self.nombre_var.get()
        if nombre in self.inventario:
            del self.inventario[nombre]
            self.mostrar_inventario()
        else:
            messagebox.showerror("No encontrado", "Producto no existe.")

    def mostrar_inventario(self):
        self.lista.delete(0, tk.END)
        for producto in self.inventario.values():
            self.lista.insert(tk.END, str(producto))

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()