# -*- coding: UTF-8 -*-
"""
Aplicação CLI para o Image Converter com suporte a arquivo único ou diretório.
"""

import argparse
import logging
import os

from img_convert.core.converter import ImageConverter
from img_convert.core.strategies.pillow_strategy import PillowConversionStrategy

def run_cli():
    """
    Função principal chamada a partir do __main__.py para executar o modo CLI.
    """
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    parser = argparse.ArgumentParser(
        description='IMG Convert CLI - Converta imagens de um arquivo ou diretório.'
    )

    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Caminho do diretório ou arquivo de entrada.'
    )

    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Diretório de saída ou caminho do novo arquivo.'
    )

    parser.add_argument(
        '-f', '--format',
        required=True,
        help='Novo formato das imagens (ex: png, jpg, bmp, etc).'
    )

    args = parser.parse_args()

    # Instancia a estratégia e o conversor
    strategy = PillowConversionStrategy()
    converter = ImageConverter(strategy)

    # Verifica se input é arquivo ou diretório
    if os.path.isfile(args.input):
        logging.info(f"Convertendo o arquivo '{args.input}' para '{args.output}' no formato '{args.format}'...")
        converter.convert_file(args.input, args.output, args.format)

    elif os.path.isdir(args.input):
        logging.info(f"Convertendo todas as imagens em '{args.input}' para '{args.output}' no formato '{args.format}'...")
        converter.convert_directory(args.input, args.output, args.format)

    else:
        logging.error(f"O caminho '{args.input}' não é um arquivo nem um diretório válido.")
        return

    logging.info("✅ Conversão concluída com sucesso!")
