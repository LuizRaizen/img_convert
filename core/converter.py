import os
import logging

logging.basicConfig(level=logging.INFO)

SUPPORTED_EXTENSIONS = ('bmp', 'png', 'gif', 'jpg', 'jpeg', 'ico')


class ImageConverter:
    """
    Classe responsável por converter imagens utilizando uma estratégia.
    """

    def __init__(self, strategy):
        """
        Inicializa o conversor com uma estratégia de conversão.

        Args:
            strategy (ConversionStrategy): Estratégia a ser utilizada.
        """
        self.strategy = strategy

    def get_all_images(self, path):
        """
        Obtém todas as imagens suportadas no diretório.

        Args:
            path (str): Caminho do diretório.

        Returns:
            list: Lista de arquivos de imagem.
        """
        return [
            f for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f)) and f.lower().endswith(SUPPORTED_EXTENSIONS)
        ]

    def convert_file(self, filepath, savepath, new_format):
        """
        Converte um arquivo de imagem.

        Args:
            filepath (str): Caminho do arquivo de imagem.
            savepath (str): Caminho onde salvar.
            new_format (str): Novo formato.

        Returns:
            bool: True se sucesso, False se falha.
        """
        return self.strategy.convert(filepath, savepath, new_format)

    def convert_directory(self, dirpath, savepath, new_format):
        """
        Converte todas as imagens de um diretório.

        Args:
            dirpath (str): Caminho do diretório.
            savepath (str): Diretório de saída.
            new_format (str): Novo formato.
        """
        all_images = self.get_all_images(dirpath)

        if not all_images:
            logging.info(f"Nenhuma imagem encontrada em '{dirpath}'.")
            return

        for image in all_images:
            filepath = os.path.join(dirpath, image)
            self.convert_file(filepath, savepath, new_format)
