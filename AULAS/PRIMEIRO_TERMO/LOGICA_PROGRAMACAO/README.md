# 🐍 Lógica de Programação com Python
> **Foco:** Fundamentos, Clean Code e Versionamento Profissional

---

## 1. 📂 Fundamentos de Python
Python é uma linguagem de alto nível, interpretada e com foco na legibilidade.

### Conceitos Chave:
*   **Variáveis e Tipos de Dados:** `int`, `float`, `str`, `bool`.
*   **Estruturas de Controle:** `if`, `elif`, `else`.
*   **Laços de Repetição:** `for` (iterações sobre sequências) e `while` (baseado em condições).
*   **Estruturas de Dados:** Listas, Dicionários e Tuplas.

```python
# Exemplo de Lógica Simples
def verificar_maioridade(idade):
    if idade >= 18:
        return "Acesso liberado"
    return "Acesso negado"

print(verificar_maioridade(20))
```

---

## 2. ✨ Clean Code (Código Limpo)
Escrever código que humanos consigam entender, não apenas máquinas.

*   **Nomes Significativos:** Use `valor_total` em vez de `vt` ou `x`.
*   **Funções Pequenas:** Uma função deve fazer apenas uma coisa e fazê-la bem.
*   **Comentários Necessários:** O código deve ser autoexplicativo; use comentários apenas para explicar o "porquê", não o "o quê".
*   **DRY (Don't Repeat Yourself):** Evite duplicar lógica; utilize funções ou classes.

---

## 3. 🌿 Git e GitHub
O controle de versão é essencial para o trabalho em equipe e histórico do projeto.

### Fluxo Básico (Git CLI):
1.  `git init`: Inicia o repositório local.
2.  `git add .`: Adiciona os arquivos para a área de espera (*staging*).
3.  `git commit -m "mensagem"`: Grava as alterações com uma explicação.
4.  `git push origin main`: Envia o código para o servidor remoto no **GitHub**.

### GitHub:
*   Hospedagem de repositórios.
*   Colaboração via *Pull Requests*.
*   Portfólio de projetos para o mercado.

---

## 🚀 Projetos Práticos
Sugestões de aplicação dos conceitos aprendidos:

1.  **Calculadora de IMC:** Prática de variáveis, entrada de dados e condicionais.
2.  **Lista de Tarefas (To-Do List):** Uso de listas, loops e manipulação de arquivos.
3.  **Conversor de Moedas com API:** Introdução à integração de dados externos e dicionários.

---

## 🛠️ Desafio da Aula
1.  Criar um script em Python que resolva um problema de lógica (ex: Gerador de Senhas).
2.  Aplicar os princípios de **Clean Code** (nomes de funções e variáveis claros).
3.  Subir o código em um novo repositório no **GitHub** utilizando o Git.

---

## 📚 Materiais Complementares
*   [PEP 8 -- Style Guide for Python Code](https://python.org)
*   [Documentação Oficial do Git](https://git-scm.com)
*   [Livro: Código Limpo (Robert C. Martin)](https://google.com)
