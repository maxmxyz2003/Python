import tkinter as tk
# Función para actualizar la expresión en el cuadro de entrada
def click_button(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Función para evaluar la expresión
def evaluate():
    try:
        global expression
        result = str(eval(expression))  # Evaluar la expresión
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""
 
# Función para limpiar la entrada
def clear():
    global expression
    expression = ""
    input_text.set("")

# Configuración de la ventana principal
window = tk.Tk()
window.title("Calculadora")
window.geometry("400x400")
expression = ""
input_text = tk.StringVar()

# Cuadro de entrada
input_frame = tk.Frame(window)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # ipady para aumentar la altura del cuadro de entrada

# Marco para los botones
btns_frame = tk.Frame(window)
btns_frame.pack()

# Primera fila
tk.Button(btns_frame, text='7', fg='black', width=10, height=3, command=lambda: click_button(7)).grid(row=1, column=0)
tk.Button(btns_frame, text='8', fg='black', width=10, height=3, command=lambda: click_button(8)).grid(row=1, column=1)
tk.Button(btns_frame, text='9', fg='black', width=10, height=3, command=lambda: click_button(9)).grid(row=1, column=2)
tk.Button(btns_frame, text='/', fg='black', width=10, height=3, command=lambda: click_button('/')).grid(row=1, column=3)

# Segunda fila
tk.Button(btns_frame, text='4', fg='black', width=10, height=3, command=lambda: click_button(4)).grid(row=2, column=0)
tk.Button(btns_frame, text='5', fg='black', width=10, height=3, command=lambda: click_button(5)).grid(row=2, column=1)
tk.Button(btns_frame, text='6', fg='black', width=10, height=3, command=lambda: click_button(6)).grid(row=2, column=2)
tk.Button(btns_frame, text='*', fg='black', width=10, height=3, command=lambda: click_button('*')).grid(row=2, column=3)

# Tercera fila
tk.Button(btns_frame, text='1', fg='black', width=10, height=3, command=lambda: click_button(1)).grid(row=3, column=0)
tk.Button(btns_frame, text='2', fg='black', width=10, height=3, command=lambda: click_button(2)).grid(row=3, column=1)
tk.Button(btns_frame, text='3', fg='black', width=10, height=3, command=lambda: click_button(3)).grid(row=3, column=2)
tk.Button(btns_frame, text='-', fg='black', width=10, height=3, command=lambda: click_button('-')).grid(row=3, column=3)

# Cuarta fila
tk.Button(btns_frame, text='C', fg='black', width=10, height=3, command=clear).grid(row=4, column=0)
tk.Button(btns_frame, text='0', fg='black', width=10, height=3, command=lambda: click_button(0)).grid(row=4, column=1)
tk.Button(btns_frame, text='=', fg='black', width=10, height=3, command=evaluate).grid(row=4, column=2)
tk.Button(btns_frame, text='+', fg='black', width=10, height=3, command=lambda: click_button('+')).grid(row=4, column=3)

window.mainloop()
