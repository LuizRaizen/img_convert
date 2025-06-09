# -*- coding: UTF-8 -*-
"""
IMG Convert - Conversor de imagens básico com Tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from img_convert.core.converter import ImageConverter
from img_convert.core.strategies.pillow_strategy import PillowConversionStrategy


# ---------- Utilitários ----------

def get_hex_from_rgb(r: int, g: int, b: int) -> str:
    """Converte valores RGB para uma string hexadecimal."""
    return f"#{r:02x}{g:02x}{b:02x}"

FNT_DEFAULT = ("Helvetica", 14)
FNT_INACTIVE = ("Helvetica", 14, "italic")
COL_INACTIVE = get_hex_from_rgb(180, 180, 180)
COL_DEFAULT = "#000"

# ---------- Classe Principal ----------

class ImgConvertApp(tk.Frame):
    """Classe principal da aplicação IMG Convert com Tkinter."""

    def __init__(self, master=None):
        super().__init__(master)
        self.converter = ImageConverter(PillowConversionStrategy())
        self.master.title("IMG Convert")
        self.master.resizable(False, False)
        self.master.configure(padx=20, pady=20)
        self.configure(relief=tk.SUNKEN, border=2, padx=20, pady=20)

        self.var_mode = tk.StringVar(value="file")
        
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        """Configura todos os widgets da interface."""
        # Título
        title = tk.Label(self, text="IMG Convert (alpha ver.)", font=("Helvetica", 18, "bold"))
        title.pack(side=tk.TOP)

        # Entradas
        self.from_entry = self.create_entry("Converter de...", self.open_from_dialog)
        self.to_entry = self.create_entry("Salvar em...", self.open_to_dialog)

        # Formato de saída
        format_frame = tk.Frame(self, pady=10)
        format_frame.pack(anchor=tk.W)
        tk.Label(format_frame, text="Formato de saída:").pack(anchor=tk.W)

        self.cb_format = ttk.Combobox(format_frame, font=FNT_DEFAULT, width=6, values=['.bmp', '.png', '.jpg', '.jpeg', '.gif'])
        self.cb_format.set('.png')
        self.cb_format.pack(anchor=tk.W)

        # Opções de modo
        radios_frame = tk.Frame(self, pady=20)
        radios_frame.pack(anchor=tk.W)

        modes = [("Converter uma única imagem", "file"),
                 ("Converter várias imagens em um diretório", "dir")]

        for text, mode in modes:
            rb = tk.Radiobutton(radios_frame, text=text, variable=self.var_mode, value=mode, command=self.reset_from_entry)
            rb.pack(anchor=tk.W)

        # Botão de converter
        convert_btn = tk.Button(self, text="Converter", font=("Helvetica", 16, "bold"),
                                foreground="white", background="green",
                                activebackground=get_hex_from_rgb(20, 200, 20),
                                activeforeground="#fff", pady=10, command=self.start_conversion)
        convert_btn.pack()

    def create_entry(self, label_text: str, command) -> tk.Entry:
        """Cria uma entrada com botão para seleção de arquivo ou pasta."""
        frame = tk.Frame(self, pady=10)
        frame.pack()

        tk.Label(frame, text=label_text).pack(anchor=tk.W)

        entry = tk.Entry(frame, font=FNT_INACTIVE, foreground=COL_INACTIVE, width=40)
        entry.insert(0, "<?>")
        entry.pack(side=tk.LEFT)

        entry.bind('<FocusIn>', self.on_focus_in)
        entry.bind('<FocusOut>', self.on_focus_out)

        btn = tk.Button(frame, text="...", width=2, command=lambda: command(entry))
        btn.pack(side=tk.RIGHT)

        return entry

    def on_focus_in(self, event):
        if event.widget['font'] == FNT_INACTIVE:
            event.widget.configure(font=FNT_DEFAULT, foreground=COL_DEFAULT)
            event.widget.delete(0, tk.END)

    def on_focus_out(self, event):
        if not event.widget.get():
            event.widget.configure(font=FNT_INACTIVE, foreground=COL_INACTIVE)
            event.widget.insert(0, "<?>")

    def reset_from_entry(self):
        """Reseta a entrada de origem quando o modo é alterado."""
        self.from_entry.configure(font=FNT_INACTIVE, foreground=COL_INACTIVE)
        self.from_entry.delete(0, tk.END)
        self.from_entry.insert(0, "<?>")

    def open_from_dialog(self, entry: tk.Entry):
        """Abre diálogo para selecionar arquivo ou diretório de origem."""
        if self.var_mode.get() == 'file':
            file = filedialog.askopenfilename(title="Abrir arquivo de imagem", initialdir='.')
            if file:
                self.set_entry(entry, file)
        else:
            dir_ = filedialog.askdirectory(title="Escolher um diretório com imagens", initialdir='.')
            if dir_:
                self.set_entry(entry, dir_)

    def open_to_dialog(self, entry: tk.Entry):
        """Abre diálogo para selecionar diretório de destino."""
        dir_ = filedialog.askdirectory(title="Salvar arquivo convertido em...", initialdir='.')
        if dir_:
            self.set_entry(entry, dir_)

    def set_entry(self, entry: tk.Entry, value: str):
        """Atualiza entrada com valor selecionado."""
        entry.configure(font=FNT_DEFAULT, foreground=COL_DEFAULT)
        entry.delete(0, tk.END)
        entry.insert(0, value)

    def start_conversion(self):
        """Inicia a conversão de imagens."""
        from_path = self.from_entry.get()
        save_path = self.to_entry.get()
        fmt = self.cb_format.get()

        if not from_path or from_path == "<?>":
            messagebox.showerror("Erro", "Por favor, selecione a origem das imagens.")
            return
        if not save_path or save_path == "<?>":
            messagebox.showerror("Erro", "Por favor, selecione o diretório de destino.")
            return

        try:
            if self.var_mode.get() == 'file':
                self.converter.convert_file(from_path, save_path, fmt)
            else:
                self.converter.convert_directory(from_path, save_path, fmt)

            messagebox.showinfo("Sucesso", "Conversão concluída com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro na conversão", str(e))


def run_tk():
    import tkinter as tk
    root = tk.Tk()
    app = ImgConvertApp(root)
    root.mainloop()


# ---------- Execução ----------

if __name__ == '__main__':
    root = tk.Tk()
    app = ImgConvertApp(master=root)
    app.mainloop()
