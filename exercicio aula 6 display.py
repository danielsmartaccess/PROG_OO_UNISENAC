import tkinter as tk
from tkinter import messagebox, simpledialog

def is_valid_name(name: str) -> bool:
    return name.isalpha()

def is_valid_phone(phone: str) -> bool:
    return phone.isdigit()

class Pessoa:
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefones = [telefone]

    def get_nome(self):
        return self.__nome

    def get_telefones(self):
        return self.__telefones

    def adicionar_telefone(self, telefone):
        self.__telefones.append(telefone)

    def remover_telefone(self, telefone):
        self.__telefones.remove(telefone)

agenda = []

def adicionar_excluir():
    botao_adicionar = tk.Button(adicionar_excluir_window, text="Adicionar", command=adicionar)
    botao_adicionar.pack() 
    botao_excluir = tk.Button(adicionar_excluir_window, text="Excluir", command=excluir)
    botao_excluir.pack()

    agenda_label = tk.Label(agenda_window, text="Agenda:")
    agenda_label.pack()
    
    adicionar_excluir_window = tk.Toplevel(root)
    adicionar_excluir_window.title("Adicionar / Excluir")
    adicionar_excluir_window.geometry("300x200")

    nome_label = tk.Label(adicionar_excluir_window, text="Nome:")
    nome_label.pack()
    nome_entry = tk.Entry(adicionar_excluir_window)
    nome_entry.pack()

    telefone_label = tk.Label(adicionar_excluir_window, text="Telefone:")
    telefone_label.pack()
    telefone_entry = tk.Entry(adicionar_excluir_window)
    telefone_entry.pack()

    def adicionar():
        nome = nome_entry.get().strip()
        if not is_valid_name(nome):
            messagebox.showerror("Erro", "Nome inválido")
            return

        telefone = telefone_entry.get().strip()
        if not is_valid_phone(telefone):
            messagebox.showerror("Erro", "Telefone inválido")
            return

        pessoa = None
        for p in agenda:
            if p.get_nome() == nome:
                pessoa = p
                break

        if pessoa is None:
            nova_pessoa = Pessoa(nome, telefone)
            agenda.append(nova_pessoa)
            messagebox.showinfo("Sucesso", f"{nome} adicionado com sucesso.")
        else:
            telefone_atual = ", ".join(pessoa.get_telefones())
            mensagem = f"Nome: {pessoa.get_nome()}\nTelefones: {telefone_atual}\n\n"
            mensagem += "1- Adicionar outro telefone\n2- Excluir nome\n3- Excluir um número"
            opcao = messagebox.askquestion("Escolha uma opção", mensagem)

            if opcao == "yes":
                telefone_novo = tk.simpledialog.askstring("Adicionar telefone", "Digite o novo telefone:")
                if telefone_novo is None or not is_valid_phone(telefone_novo.strip()):
                    messagebox.showerror("Erro", "Telefone inválido")
                else:
                    pessoa.adicionar_telefone(telefone_novo)
                    messagebox.showinfo("Sucesso", "Telefone adicionado com sucesso.")

            if opcao == "no":
                agenda.remove(pessoa)
                messagebox.showinfo("Sucesso", f"{nome} excluído com sucesso.")
            elif opcao == "cancel":
                return
            else:
                telefone_remover = tk.simpledialog.askstring("Remover telefone", "Digite o telefone a ser excluído:")
                if telefone_remover is None or not is_valid_phone(telefone_remover.strip()):
                    messagebox.showerror("Erro", "Telefone inválido")
                    return
                pessoa.remover_telefone(telefone_remover)
                messagebox.showinfo("Sucesso", "Telefone excluído com sucesso.")

    def excluir():
        nome = nome_entry.get().strip()
        if not is_valid_name(nome):
            messagebox.showerror("Erro", "Nome inválido")
            return

        pessoa = None
        for p in agenda:
            if p.get_nome() == nome:
                pessoa = p
                break

        if pessoa is None:
            messagebox.showerror("Erro", "Nome não encontrado")
        else:
            agenda.remove(pessoa)
            messagebox.showinfo("Sucesso", f"{nome} excluído com sucesso.")
        
root = tk.Tk()
root.title("Agenda")
root.geometry("300x200")


nome_label = tk.Label(root, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

telefone_label = tk.Label(root, text="Telefone:")
telefone_label.pack()
telefone_entry = tk.Entry(root)
telefone_entry.pack()

botao_adicionar_excluir = tk.Button(root, text="Adicionar / Excluir", command=adicionar_excluir)
botao_adicionar_excluir.pack(pady=10)

root.mainloop()

# Path: exercicio aula 6 display.py




