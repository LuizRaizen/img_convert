# IMG Convert

**IMG Convert** é um aplicativo desktop criado em Python para conversão de imagens de maneira simples, rápida e multiplataforma. O programa oferece três modos de uso: interface moderna com PySide6, interface clássica com Tkinter, e modo CLI via terminal.

## 🚀 Funcionalidades

- Conversão entre múltiplos formatos de imagem (PNG, JPG, BMP, WEBP, etc.)
- Interface gráfica moderna com PySide6
- Interface clássica com Tkinter como alternativa leve
- Modo CLI para automação e uso rápido no terminal
- Suporte a múltiplas imagens (conversão em lote)
- Suporte multiplataforma (Windows e Linux)

## 🖥️ Requisitos

- Python 3.8+
- Bibliotecas: Pillow, PySide6 (opcional), Tkinter (já incluído na maioria das distribuições Python)

## 📦 Instalação

Clone este repositório:

```bash
git clone https://github.com/seu-usuario/img-convert.git
cd img-convert
```

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## ▶️ Como executar

Você pode executar o IMG Convert em três modos distintos:

### Interface moderna com PySide6:

```bash
python main.py --qt
```

### Interface clássica com Tkinter:

```bash
python main.py --tk
```

### Modo linha de comando:

```bash
python main.py --cli
```

> Obs: Certifique-se de estar no diretório raiz do projeto ao executar os comandos acima.

## 📁 Estrutura do Projeto

```
img_convert/
├── cli/              # Modo linha de comando
├── gui_qt/           # Interface moderna com PySide6
├── gui_tk/           # Interface clássica com Tkinter
└── utils/            # Funções auxiliares e utilitários
```

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
