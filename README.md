# IMG Convert

**IMG Convert** é um aplicativo desktop desenvolvido em **Python** com foco na **conversão de imagens** de forma rápida, simples e visual. Criado inicialmente como um módulo básico com a biblioteca `Pillow` (PIL), o projeto evoluiu para incorporar interfaces gráficas com **Tkinter** e, posteriormente, **PySide6**, permitindo uma experiência mais moderna e organizada.

## ✨ Funcionalidades

- Conversão de imagens entre os principais formatos (PNG, JPG, BMP, WEBP, etc.)
- Interface gráfica moderna com **PySide6**
- Interface alternativa com **Tkinter** (modo clássico)
- Suporte a múltiplos modos de operação: imagem única ou pasta inteira
- Progresso visual da conversão com barra de carregamento

## 🚧 Status

O projeto ainda está em desenvolvimento. Atualmente, todas as telas foram modeladas com Qt Designer, porém ainda sem funcionalidades implementadas.

## 💡 Futuras Implementações

- Arrastar e soltar arquivos diretamente na interface
- Edição básica de imagens (girar, redimensionar, converter cor)
- Integração com formatos menos comuns
- Histórico de conversões realizadas

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Pillow (PIL)**
- **PySide6 (Qt for Python)**
- **Tkinter (modo alternativo)**

## 📦 Instalação

```bash
git clone https://github.com/seu-usuario/img-convert.git
cd img-convert
pip install -r requirements.txt
python main.py
```

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
