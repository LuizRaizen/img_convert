import os
from PIL import Image, ImageFile
import logging
from img_convert.core.strategies.base import ConversionStrategy

ImageFile.LOAD_TRUNCATED_IMAGES = True

SUPPORTED_EXTENSIONS = ('bmp', 'png', 'gif', 'jpg', 'jpeg', 'ico')


class PillowConversionStrategy(ConversionStrategy):
    """
    Estratégia de conversão utilizando Pillow.
    """

    def convert(self, filepath, savepath, new_format):
        try:
            old_file = os.path.basename(filepath)
            name, old_ext = os.path.splitext(old_file)
            old_ext = old_ext.lstrip('.').lower()

            if old_ext not in SUPPORTED_EXTENSIONS:
                logging.warning(f"Ignorado: '{filepath}' (formato não suportado)")
                return False

            new_ext = new_format.lstrip('.').lower()
            new_file = f"{name}.{new_ext}"
            os.makedirs(savepath, exist_ok=True)
            save_file = os.path.join(savepath, new_file)

            image = Image.open(filepath)

            if not os.path.exists(save_file):
                image.save(save_file)
                logging.info(f"{new_file} [OK!]")
            else:
                logging.info(f"Já existe '{new_file}' em '{savepath}'.")

            return True

        except Exception as e:
            logging.error(f"ATENÇÃO! '{filepath}' não pôde ser convertido. Erro: {e}")
            return False
