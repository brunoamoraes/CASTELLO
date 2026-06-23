# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!" -- Tkinter
import tkinter as tk
def registrar_operador():
    nome = ent_nome.get()
    turno = ent_turno.get().upper()
    if turno in ['A', 'B', 'C']:
        resultado = f"Operador {nome} registrado no Turno {turno}. Boa jornada!"
    else:
        resultado = "Turno inválido. Por favor, insira A, B ou C."
    lbl_resultado.config(text=resultado)
root = tk.Tk()
root.title("Registro de Operador")
root.geometry("500x300")
lbl_nome = tk.Label(root, text="Nome do Operador:")
lbl_nome.pack()
ent_nome = tk.Entry(root)
ent_nome.pack()
lbl_turno = tk.Label(root, text="Turno (A, B ou C):")
lbl_turno.pack()
ent_turno = tk.Entry(root)
ent_turno.pack()
button_registrar = tk.Button(root, text="Registrar", command=registrar_operador)
button_registrar.pack() 
lbl_resultado = tk.Label(root, text="")
lbl_resultado.pack()
root.mainloop()

