import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="IMG Convert - Conversor de Imagens")
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--qt', action='store_true', help='Abrir interface PySide6 (GUI moderna)')
    group.add_argument('--tk', action='store_true', help='Abrir interface Tkinter (GUI clássica)')
    group.add_argument('--cli', action='store_true', help='Usar via linha de comando (modo texto)')

    args = parser.parse_args()

    if args.qt:
        from img_convert.gui_qt.main_app import run_qt
        run_qt()

    elif args.tk:
        from img_convert.gui_tk.main_app import run_tk
        run_tk()

    elif args.cli:
        from img_convert.cli.main_app import run_cli
        run_cli()

if __name__ == "__main__":
    main()
