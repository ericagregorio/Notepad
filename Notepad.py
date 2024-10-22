import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class BlocoDeNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Notas Simples")
        self.root.geometry("600x400")

        # Criar o campo de texto
        self.text_area = tk.Text(self.root, font=("Arial", 12), undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Criar um menu
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Criar submenus
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)
        self.file_menu.add_command(label="Novo", command=self.new_file)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Salvar", command=self.save_file)
        self.file_menu.add_command(label="Salvar como...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.root.quit)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)
        self.edit_menu.add_command(label="Desfazer", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Refazer", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copiar", command=lambda: self.root.focus_get().event_generate('<<Copy>>'))
        self.edit_menu.add_command(label="Colar", command=lambda: self.root.focus_get().event_generate('<<Paste>>'))
        self.edit_menu.add_command(label="Cortar", command=lambda: self.root.focus_get().event_generate('<<Cut>>'))

        # Variáveis de controle de arquivo
        self.file_path = None

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = None

    def open_file(self):
        self.file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                    filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")])
        if self.file_path:
            with open(self.file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        self.file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                      filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")])
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

import tkinter as tk
from tkinter import colorchooser

class BlocoDeNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Notas Simples")
        self.root.geometry("600x400")

        # Criar o campo de texto
        self.text_area = tk.Text(self.root, font=("Arial", 12), undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Criar um menu
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Menu para alterar as cores
        self.color_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Formatar", menu=self.color_menu)
        self.color_menu.add_command(label="Cor de Fundo", command=self.change_bg_color)
        self.color_menu.add_command(label="Cor da Letra", command=self.change_text_color)

    def change_bg_color(self):
        # Escolher cor para o fundo
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(bg=color)

    def change_text_color(self):
        # Escolher cor para o texto
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(fg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = BlocoDeNotas(root)
    root.mainloop()