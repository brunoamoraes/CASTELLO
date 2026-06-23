import tkinter as tk
from tkinter import messagebox, ttk

# .get() serve para buscar informação na caixa de texto
def janela_bemvindo():
    nome = nome_usuario.get()
    idade = idade_usuario.get()



    if nome == "" and idade == "":
        messagebox.showwarning("Aviso", "Digite seu nome e sua idade :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá usuário, {nome} e {idade} - Seja bem-vindo ao nosso sistema")

def segunda_janela():
    segunda_janela = tk.Toplevel(janela)
    segunda_janela.tilte("Segunda Janela")
    segunda_janela.geometry("300x300")


# Configurações da Janela
janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("300x300")
janela.configure(bg="pink")

# Componentes
# Labels
lbl_mensagem = tk.Label(janela, text="Digite seu nome :)")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
lbl_idade = tk.Label(janela, text="Digite sua idade :)")
lbl_idade.grid(row=1, column=0, pady=10, padx=10)

# Entrys
nome_usuario = tk.Entry(janela, font=("Arial", 12), width=15)
nome_usuario.grid(row=0, column=1, pady=10, padx=10)
idade_usuario = tk.Entry(janela, font=("Arial", 12), width=15)
idade_usuario.grid(row=1, column=1, pady=10, padx=10)

#Selections
sel_nivel = tk.Spinbox(janela, from_=1, to=10, width=10)
sel_nivel.grid(row=2, column=1, pady=10, padx=10)

# ComboBox
combo_nivel = tk.ttk.Combobox(janela, values=["Fácil", "Médio", "Difícil"], width=10)
combo_nivel.grid(row=3, column=1, pady=10, padx=10)


btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

btn_segunda_janela = tk.Button(janela, text="Abrindo Segunda Janela", command=segunda_janela)
btn_segunda_janela.grid(row=3, column=0, pady=10, padx=10)

# Rodar interface
janela.mainloop()



