import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas():
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(listbox.get(0, tk.END), f)

def adicionar_tarefa():
    tarefa = entry.get().strip()
    if tarefa:
        listbox.insert(tk.END, tarefa)
        entry.delete(0, tk.END)
        salvar_tarefas()
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa!")

def remover_tarefa():
    selecionado = listbox.curselection()
    if selecionado:
        listbox.delete(selecionado)
        salvar_tarefas()
    else:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")

def marcar_concluida():
    selecionado = listbox.curselection()
    if selecionado:
        indice = selecionado[0]
        tarefa = listbox.get(indice)
        if not tarefa.startswith("✔ "):
            listbox.delete(indice)
            listbox.insert(indice, "✔ " + tarefa)
            salvar_tarefas()

# Janela principal
root = tk.Tk()
root.title("Gerenciador de Tarefas - Jonathan Rocha Castro")
root.geometry("600x600")
root.configure(bg="#f0f0f0")

# Título
titulo = tk.Label(root, text="Minhas Tarefas do Dia 📋", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
titulo.pack(pady=20)

# Entrada
entry = tk.Entry(root, font=("Helvetica", 14), width=40)
entry.pack(pady=10)

# Botões
frame_botoes = tk.Frame(root, bg="#f0f0f0")
frame_botoes.pack(pady=10)

btn_adicionar = ttk.Button(frame_botoes, text="Adicionar Tarefa ➕", command=adicionar_tarefa)
btn_adicionar.grid(row=0, column=0, padx=10)

btn_remover = ttk.Button(frame_botoes, text="Remover Tarefa 🗑️", command=remover_tarefa)
btn_remover.grid(row=0, column=1, padx=10)

btn_concluir = ttk.Button(frame_botoes, text="Marcar Concluída ✅", command=marcar_concluida)
btn_concluir.grid(row=0, column=2, padx=10)

# Lista de tarefas
listbox = tk.Listbox(root, font=("Helvetica", 12), width=60, height=15, selectmode=tk.SINGLE)
listbox.pack(pady=20)

# Carregar tarefas salvas
for tarefa in carregar_tarefas():
    listbox.insert(tk.END, tarefa)

root.mainloop()