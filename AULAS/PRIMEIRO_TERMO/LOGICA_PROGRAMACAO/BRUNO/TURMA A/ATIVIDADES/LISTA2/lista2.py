# 11.Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
# O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado. (Tkinter)

import tkinter as tk

peso_total = 0.0

def somar_producao():
    global peso_total

    texto_peso = ent_peso.get().strip()
    if not texto_peso:
        lbl_resultado.config(text="Digite um peso antes de adicionar.")
        return

    try:
        peso = float(texto_peso)
    except ValueError:
        lbl_resultado.config(text="Valor inválido. Digite um número válido.")
        return

    if peso == 0:
        lbl_resultado.config(text=f"Peso total acumulado: {peso_total:.2f} kg")
        return

    peso_total += peso
    ent_peso.delete(0, tk.END)
    lbl_resultado.config(text=f"Peso parcial acumulado: {peso_total:.2f} kg")

root = tk.Tk()
root.title("Soma de Produção")
root.geometry("400x200")

lbl_peso = tk.Label(root, text="Digite o peso da caixa (0 para parar):")
lbl_peso.pack()

ent_peso = tk.Entry(root)
ent_peso.pack()

button_adicionar = tk.Button(root, text="Adicionar Peso", command=somar_producao)
button_adicionar.pack()

lbl_resultado = tk.Label(root, text="")
lbl_resultado.pack()
root.mainloop()
