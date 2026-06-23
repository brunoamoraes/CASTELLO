import tkinter as tk
from tkinter import messagebox, ttk

def bemvindo():
    # .get() serve para buscar o texto da caixa
    nome_usuario = usuario_nome.get()
    idade_usaario = usuario_idade.get()
    pais_usuario = combo_nivel.get()


    if nome_usuario == "" and idade_usaario == "" and pais_usuario == "":
        messagebox.showwarning("Aviso", "Por favor digite seu nome, idade e selecione seu país! :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá {nome_usuario}, logando no sistema! e sua idade é {idade_usaario} e seu país é {pais_usuario} :)")

def segunda_janela():
    segunda_janela = tk.Toplevel(janela_bemvindo)
    segunda_janela.title("Segunda Janela")
    segunda_janela.geometry("500x500")

    lbl_segunda_janela = tk.Label(segunda_janela, text="Bem-Vindo a Segunda Janela :)", font=('Arial', 12), fg='blue')
    lbl_segunda_janela.grid(row=0, column=0, pady=10, padx=10)

# Janela
janela_bemvindo = tk.Tk()
janela_bemvindo.title("Saudações do Usuário")
janela_bemvindo.geometry("500x500")

# Componentes
# Labels
lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="Digite seu nome :)")
lbl_mensagem_usuario.grid(row=0, column=0, pady=10, padx=10)

lbl_mensagem_idade = tk.Label(janela_bemvindo, text="Digite sua idade :)")
lbl_mensagem_idade.grid(row=1, column=1, pady=10, padx=10)

lbl_mensagem_pais = tk.Label(janela_bemvindo, text="Selecione seu país :)")
lbl_mensagem_pais.grid(row=1, column=0, pady=10, padx=10)

lbl_segunda_janela = tk.Label(janela_bemvindo, text="Clique para abrir a segunda janela :)")
lbl_segunda_janela.grid(row=2, column=0, pady=10, padx=10)



# Entrys
usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
usuario_nome.grid(row=2,column=1,pady=10,padx=10)

usuario_idade = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
usuario_idade.grid(row=3,column=1,pady=10,padx=10)

# Componentes de ComboBox
combo_nivel = tk.ttk.Combobox(janela_bemvindo, values=["Brasil", "Marrocos", "Egito", "Escócia"], width=30)
combo_nivel.grid(row=1, column=1, pady=10, padx=10)


# Botão
btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Enviar Mensagem", command=bemvindo)
btn_enviar_mensagem.grid(row=2, column=0, pady=10, padx=10)

btn_segunda_janela = tk.Button(janela_bemvindo, text="Abrir Segunda Janela", command=segunda_janela)
btn_segunda_janela.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar Janela", command=janela_bemvindo.destroy)
btn_fechar_janela.grid(row=4, column=0, pady=10, padx=10)

# Rodar interface
janela_bemvindo.mainloop()
