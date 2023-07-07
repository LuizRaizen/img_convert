# -*- coding: UTF-8 -*-
""" Funções para admnistrar a aplicação de conversão """

import os

from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def get_all_images(path):
    """ Obtém todas as imagens do diretório """

    # Lista os todos os arquivos de imagem no diretório obtido;
    images = os.listdir(path)

    # Retorna a lista de caminhos;
    return images


def file_convert(filepath, savepath, new_format):
    """ Converter as imagens para outro formato """

    # Obtém o arquivo de imagem original;
    old_file = filepath.split("/")[-1]
    # Obtém o nome do arquivo de imagem original sem a extensão;
    name = old_file.split(".")[0]
    # Obtém a extensão original do arquivo; 
    old_format = filepath.split(".")[-1].lower()
    
    # Encerrar conversão se o arquivo não for um arquivo de imagem;
    if not old_format in ('bmp', 'png', 'gif', 'jpg', 'jpeg'):
        return
    
    # Obtém o caminho do diretório da imagem;
    old_path = filepath.split("/")[1:-2]
    old_path = "/".join(old_path) + "/"

    # Define o novo formato de imagem;
    if not '.' in new_format:
        new_file = name + '.' + new_format
    else:
        new_file = name + new_format
        
    # Corrigindo referência ao diretório de saída;
    savepath = savepath + "/"
    
    try:
        # Abre o arquivo de imagem original;
        image = Image.open(filepath)

        # Cria um diretório para salvar a imagem se ele nãp existir;
        if not os.path.exists(savepath):
            os.mkdir(savepath)

        # Salva o novo arquivo de imagem se ele não existir;
        if not os.path.exists(savepath+new_file):
            image.save(savepath+new_file)
        else:
            print("Já existe um arquivo '"+new_file+"' em '"+savepath+"'.")
        
        # Exibe uma mensagem se a conversão for feita com sucesso;
        print(new_file+" [OK!]")
        
    except:
        # Exibe uma mensagem se ocorrer algum erro durante a conversão;
        print("ATENÇÃO! '"+filepath+"' não pôde ser convertido.")
    
        
def dir_convert(dirpath, savepath, format):
    """ Converte cada imagen dentro do diretório obtido """

    # Adiciona uma barra no final do caminho, caso ele não tenha; 
    if not dirpath[-1] == '/':
        dirpath += "/"
    
    # Obtém uma lista de todas as imagens dentro do diretório;
    all_images = get_all_images(dirpath)

    # Tenta converter cada imagem da lista de imagens;
    for image in all_images:
        file_convert(dirpath+image, savepath, format)
