# -*- coding: UTF-8 -*-
""" Conversor de imagens básico criado com PIL e Tkinter.
    - Nome: IMG Convert
    - Versão: alpha
    - Autor (e-mail): luizrdererita@gmail.com
    - Pode converter um arquivo de imagem único;
    - Pode converter todas as imagens em um diretório selecionado;
    - Nas próximas versões:
        * Possibilidade de usar o App em dois modos: Terminal e GUI;
        * Possibilidade de selecionar várias imagens específicas em
        um diretório;
        * Preview das imagens selecionadas;
        * Dialog de loading exibindo o progresso das conversões;
        * Ajustes para o melhor desempenho do App;
        
"""

from tkinter import *
from tkinter.filedialog import askopenfile, askdirectory
from tkinter.commondialog import Dialog

from converter import *


def get_hex_from_rgb(r, g, b):
    
    return "#%02x%02x%02x" %(r, g, b)


class Main(Frame):
    """ Classe principal da aplicação """
    
    def __init__(self, master=None):
        """ Inicializa a aplicação """
        
        # Inicializa a superclasse;
        super().__init__(master)
        
        self.fnt_default = "Helvetica 14"
        self.fnt_inactive = "Helvetica 14 italic"
        self.col_inactive = get_hex_from_rgb(180, 180, 180)
        self.col_default = "#000"
        self.var_mode = StringVar(self)
        self.var_mode.set("file")
        
        # Define o título da janela;
        self.master.title("IMG Convert")
        # Desabilita o redimensionamento de tela;
        self.master.resizable(False, False)
        self.master.configure(padx=20, pady=20)
        # Configura o espaçamento entre as bodas da tela e os widgets;
        self.configure(relief=RAISED, border=2, padx=20, pady=20)
        
        # Título;
        self.lbl_title = Label(self, name='lbl_title', text="IMG Convert (alpha ver.)")
        self.lbl_title.configure(font="Helvetica 18 bold")
        self.lbl_title.pack(side=TOP)
        
        # Cria os campos de entrada para o(s) caminho da(s) imagem(s);
        entry1 = ('from', "Converter de...", "<?>", self.open_from_dialog)
        entry2 = ('to', "Salvar em...", "<?>", self.open_to_dialog)
        
        for entry in (entry1, entry2):
            self.create_entry(self, *entry)
        
        # Cria o campo para seleção do formato de saída;    
        self.frm_format = Frame(self, name='frm_format', pady=10)
        self.frm_format.pack(anchor=W)
        
        self.lbl_format = Label(self.frm_format, text="Formato de saída: ")
        self.lbl_format.pack(anchor=W)
        
        self.txt_format = Entry(self.frm_format)
        self.txt_format.configure(font=self.fnt_default,
                                  readonlybackground='#FFF', width=6)
        self.txt_format.insert(0, '.png')
        self.txt_format.bind('<1>', self.view_all_formats)
        self.txt_format.pack(anchor=W)
            
        # Container dos botões de rádio;
        self.frm_radios = Frame(self, name='frm_radios', pady=20)
        self.frm_radios.pack(side=TOP, anchor=W)
        # Botão de rádio para a conversão de várias imagens;
        self.rad_file = Radiobutton(self.frm_radios, name='rad_file')
        self.rad_file.configure(text="Converter uma única imagem",
                                variable=self.var_mode, value="file")
        self.rad_file.bind('<Button-1>', self.set_mode)
        self.rad_file.pack(anchor=W)
        # Botão de rádio para conversão de uma imagem única;
        self.rad_dir = Radiobutton(self.frm_radios, name='rad_dir')
        self.rad_dir.configure(text="Converter várias imagens em um diretório",
                               variable=self.var_mode, value="dir")
        self.rad_dir.bind('<Button-1>', self.set_mode)
        self.rad_dir.pack(anchor=W)
        
        # Botão para converter;
        self.btn_convert = Button(self, text="Converter", font="Helvetica 16 bold")
        self.btn_convert.configure(foreground="white", background="green",
                                   activebackground=get_hex_from_rgb(20, 200, 20),
                                   activeforeground=get_hex_from_rgb(255, 255, 255),
                                   command=self.start_convertion, pady=10)
        # Posiciona e exibe o widget na tela;
        self.btn_convert.pack()
        
        
        # Armazena os menus pulldown ativos;
        self.pulldowns = list()
        # Destrói os menus pulldown ativos se clicar na tela;
        self.bind('<Button>', self.destroy_pulldowns)
        
        # Exibir o layout da aplicação;
        self.pack()

    def create_entry(self, frame, name, label, default, command):
        """ Criar as caixas de entrada os botões de pesquisa """
        
        # Container para isolar um único campo de entrada e seus elementos;
        frm = Frame(frame, name='frm_'+name, pady=10)
        frm.pack(side=TOP)
        
        # Label da entrada;
        lbl = Label(frm, name='lbl_'+name, text=label)
        lbl.pack(side=TOP, anchor=W)
        
        # Definição da caixa de entrada;
        txt = Entry(frm, name='txt_'+name, font=self.fnt_default, width=40)
        txt.configure(font=self.fnt_inactive, foreground=self.col_inactive)
        txt.bind('<FocusIn>', self.get_entry_events)
        txt.bind('<FocusOut>', self.get_entry_events)
        txt.insert(0, default)
        txt.pack(side=LEFT)
        
        # Botão para abrir o arquivo ou diretório das imagens;
        btn = Button(frm, name='btn_'+name, text="...", width=2)
        btn.bind('<Button-1>', command)
        btn.pack(side=RIGHT)    

    def get_entry_events(self, event):
        """ Administra o comportamento das entradas que recebem foco """
        
        widget = event.widget
        
        if widget['font'] == self.fnt_inactive:
            widget.configure(font=self.fnt_default, foreground=self.col_default)
            widget.delete(0, len(widget.get()))
            
        elif widget['font'] == self.fnt_default and not widget.get():
            widget.configure(font=self.fnt_inactive, foreground=self.col_inactive)
            widget.insert(0, "<?>")
            
    def open_from_dialog(self, event):
        """ Abre um filedialog para encontrar a imagem ou diretório """
        
        button = event.widget
        entry = self.children['frm_from'].children['txt_from']
        
        if self.var_mode.get() == 'file':
            # types = ['bmp', 'png', 'jpg', 'jpeg', 'gif']
            file = askopenfile(title="Abrir arquivo de imagem",
                               initialdir='.')
            
            if file:
                entry.configure(font=self.fnt_default, foreground=self.col_default)
                entry.delete(0, END)
                entry.insert(0, file.name)
                
        if self.var_mode.get() == 'dir':
            dir = askdirectory(title="Escolher um diretório com as imagens",
                               initialdir='.')
            
            if dir:
                entry.configure(font=self.fnt_default, foreground=self.col_default)
                entry.delete(0, END)
                entry.insert(0, dir)
                
        button.configure(state=DISABLED)
    
    def open_to_dialog(self, event):
        """ Abre um filedialog para definir diretório de destino """
        
        button = event.widget
        entry = self.children['frm_to'].children['txt_to']
        dir = askdirectory(title="Salvar arquivo convertido em...",
                           initialdir='.')
            
        if dir:
            entry.configure(font=self.fnt_default, foreground=self.col_default)
            entry.delete(0, END)
            entry.insert(0, dir)
            
        button.configure(state=DISABLED)

    def set_mode(self, event):
        """ Define o modo de conversão de imagem """
        
        entry = self.children['frm_from'].children['txt_from']
        entry.configure(font=self.fnt_inactive, foreground=self.col_inactive)
        entry.delete(0, END)
        entry.insert(0, "<?>")
        
    def start_convertion(self):
        """ Inicia a conversão quando o botão 'Converter' for pressionado """
        
        frompath = self.children['frm_from'].children['txt_from'].get()
        savepath = self.children['frm_to'].children['txt_to'].get()
        
        if self.var_mode.get() == 'file':
            file_convert(frompath, savepath, self.txt_format.get())
            
        elif self.var_mode.get() == 'dir':
            dir_convert(frompath, savepath, self.txt_format.get())
            
    def view_all_formats(self, event):
        """ Exibe todos os formatos de imagem disponíveis para conversão """
        
        # Obtém a instância da caixa de entrada que exibe os formatos;
        entry = event.widget
        
        # Cria um menu para exibir os formatos de conversão;
        formats = Menu(self, font=self.fnt_default, background='#FFF')
        formats.configure(type='tearoff', tearoff=FALSE)
        # Adiciona o menu de opções de conversão para 'pulldowns';
        self.pulldowns.append(formats)
        
        # Adiciona as opções de formato ao menu;
        for label in ('.bmp', '.png', '.jpg', '.jpeg', '.gif'):
            call = lambda p=formats, f=label: self.change_format(p, f)
            formats.add_command(label=label, command=call)
        
        # Exibe o menu a baixo da caixa de entrada;
        formats.post(entry.winfo_rootx(),
                     entry.winfo_rooty()+entry.winfo_height())
        
    def change_format(self, pulldown, format):
        """ Altera o formato de saída da imagem que será convertida """
        
        # Delete o conteúdo atual de 'txt_format';
        self.txt_format.delete(0, END)
        # Insere o formato de imagem selecionado em 'txt_format';
        self.txt_format.insert(0, format)
        
        # Destrói a instância do menu de opções;
        pulldown.destroy()
    
    def destroy_pulldowns(self, event):
        """ Destroy os menus pulldowns se clicar na tela """
        
        if self.pulldowns:
            for menu in self.pulldowns:
                menu.destroy()
        
    
if __name__ == '__main__':
    Main().mainloop()
