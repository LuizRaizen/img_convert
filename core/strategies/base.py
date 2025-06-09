from abc import ABC, abstractmethod

class ConversionStrategy(ABC):
    """
    Interface para estratégias de conversão de imagem.
    """

    @abstractmethod
    def convert(self, filepath, savepath, new_format):
        """
        Converte a imagem.
        """
        pass
