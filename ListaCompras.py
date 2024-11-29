import tkinter as tk
from tkinter import messagebox


def adicionar_produto():
    produto = entrada_produto.get() 
    if produto:
        lista_produtos.insert(tk.END, produto) 
        entrada_produto.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, insira um produto.") 

def excluir_produto():
    try:
        produto_selecionado = lista_produtos.curselection()  
        lista_produtos.delete(produto_selecionado)
    except:
        messagebox.showwarning("Seleção inválida", "Por favor, selecione um produto para excluir.")

def concluir_produto():
    try:
        produto_selecionado = lista_produtos.curselection()  
        produto = lista_produtos.get(produto_selecionado) 
        lista_produtos.delete(produto_selecionado) 
        lista_concluidos.insert(tk.END, produto)  
    except:
        messagebox.showwarning("Seleção inválida", "Por favor, selecione um produto para concluir.")

janela = tk.Tk()
janela.title("Lista de Compras")

entrada_produto = tk.Entry(janela, width=40)
entrada_produto.grid(row=0, column=0, padx=10, pady=10)

tk.Button(janela, text="Adicionar Produto", width=20, command=adicionar_produto).grid(row=0, column=1, padx=10, pady=10)
tk.Button(janela, text="Excluir Produto", width=20, command=excluir_produto).grid(row=1, column=0, padx=10, pady=10)
tk.Button(janela, text="Comprar Produto", width=20, command=concluir_produto).grid(row=1, column=1, padx=10, pady=10)

lista_produtos = tk.Listbox(janela, height=10, width=50)
lista_produtos.grid(row=2, column=0, padx=10, pady=10)

lista_concluidos = tk.Listbox(janela, height=10, width=50)
lista_concluidos.grid(row=2, column=1, padx=10, pady=10)

janela.mainloop()
