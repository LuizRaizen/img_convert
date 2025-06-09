#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""IMG Convert - Interface PySide6
    - Aplicativo para conversão de imagens com GUI.
"""

import os
import re
import sys
import logging
from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QDialogButtonBox, QMessageBox
)

from img_convert.gui_qt.dialogs.ui import Ui_MainWindow
from img_convert.gui_qt.dialogs.from_dialog import Ui_FromDialog
from img_convert.gui_qt.dialogs.to_dialog import Ui_ToDialog
from img_convert.gui_qt.dialogs.convert_dialog import Ui_ConvertDialog
from img_convert.core.converter import ImageConverter
from img_convert.core.strategies.pillow_strategy import PillowConversionStrategy

logging.basicConfig(level=logging.INFO)

FORMATS = [
    'Todos os Arquivos',
    'BMP - Windows Bitmap (.bmp)',
    'GIF - Graphics Interchange Format (.gif)',
    'JPEG - Joint Photographic Experts Group (.jpg;.jpeg;.jfif;jif;jpe)',
    'PNG - Portable Network Graphics (.png)',
    'TIFF - Tagged File Image Format (.tif;.tiff)'
]

class PathDialog(QDialog):
    def __init__(self, ui_class, allow_file_selection=True):
        super().__init__()
        self.dialog = QDialog()
        self.ui = ui_class()
        self.ui.setupUi(self.dialog)
        self.model = QStandardItemModel(self.ui.lv_files)
        self.icon_provider = QIcon()
        self.allow_file_selection = allow_file_selection
        self.current_path = os.path.expanduser("~")
        self.selected_path = self.current_path

        self._setup_buttons()
        self._initialize_nav()
        self._setup_paths(initial=True)
        self._initialize_list()

        self.ui.lv_files.clicked.connect(self.file_one_clicked)
        self.ui.lv_files.doubleClicked.connect(self.file_double_clicked)
        self.ui.cb_dir.currentIndexChanged.connect(self.path_selected_from_combobox)
        self.ui.bbox_ok_cancel.accepted.connect(self.button_ok_clicked)
        self.ui.bbox_ok_cancel.rejected.connect(self.button_cancel_clicked)
        self.ui.bbox_open.clicked.connect(self.go_up_directory)

    def _setup_buttons(self):
        ok_button = self.ui.bbox_ok_cancel.button(QDialogButtonBox.Ok)
        ok_button.setText("Ok")
        cancel_button = self.ui.bbox_ok_cancel.button(QDialogButtonBox.Cancel)
        cancel_button.setText("Cancelar")
        open_button = self.ui.bbox_open.button(QDialogButtonBox.Open)
        open_button.setText("⬆")

    def _setup_paths(self, initial=False):
        if initial:
            self.ui.cb_dir.blockSignals(True)
            self.ui.cb_dir.clear()
            self.ui.cb_dir.addItem(self.current_path)
            self.ui.cb_dir.setCurrentIndex(0)
            self.ui.cb_dir.blockSignals(False)

    def _add_to_cb_dir(self, path):
        self.ui.cb_dir.blockSignals(True)
        existing_paths = [self.ui.cb_dir.itemText(i) for i in range(self.ui.cb_dir.count())]
        if path not in existing_paths:
            self.ui.cb_dir.addItem(path)
        index = self.ui.cb_dir.findText(path)
        if index >= 0:
            self.ui.cb_dir.setCurrentIndex(index)
        self.ui.cb_dir.blockSignals(False)

    def _initialize_nav(self, path=None):
        regex = r'^\..*'
        path = path or self.current_path
        try:
            listdir = os.listdir(path)
        except OSError as e:
            logging.error(f"Erro ao listar diretório: {e}")
            listdir = []

        self.files = []
        self.dirs = []
        for item in listdir:
            full_path = os.path.join(path, item)
            if os.path.isfile(full_path) and not re.match(regex, item):
                self.files.append(item)
            elif os.path.isdir(full_path) and not re.match(regex, item):
                self.dirs.append(item)
        self.current_path = path

    def _initialize_list(self):
        self.model.clear()
        for dirname in self.dirs:
            self.add_item(dirname, QIcon.fromTheme("inode-directory"))
        if self.allow_file_selection:
            for filename in self.files:
                icon = self._get_icon_for_file(filename)
                self.add_item(filename, icon)
        self.ui.lv_files.setModel(self.model)

    def _navigate_to_path(self, path, add_to_combo=True):
        self._initialize_nav(path)
        self._initialize_list()
        if add_to_combo:
            self._add_to_cb_dir(path)

    def _get_icon_for_file(self, filename):
        ext = os.path.splitext(filename)[1].lower()
        icon_map = {
            ('.jpg', '.jpeg', '.jfif', '.jif'): "image-x-generic-jpeg",
            ('.bmp',): "image-x-generic-bmp",
            ('.png',): "image-x-generic-png",
            ('.gif',): "image-x-generic-gif",
            ('.tif', '.tiff'): "image-x-generic-tiff",
            ('.mp3',): "audio-x-generic-mp3",
            ('.wav',): "audio-x-generic-wav",
            ('.ogg',): "audio-x-generic-ogg"
        }
        for exts, theme_icon in icon_map.items():
            if ext in exts:
                return QIcon.fromTheme(theme_icon)
        return QIcon.fromTheme("application-x-generic")

    def add_item(self, text, icon):
        item = QStandardItem(icon, text)
        self.model.appendRow(item)

    def get_selected_file(self, index: QModelIndex):
        selected_item = self.model.itemFromIndex(index)
        if selected_item:
            return os.path.join(self.current_path, selected_item.text())
        return None

    def file_one_clicked(self, index: QModelIndex):
        path = self.get_selected_file(index)
        if path:
            self.selected_path = path

    def file_double_clicked(self, index: QModelIndex):
        path = self.get_selected_file(index)
        if path and os.path.isdir(path):
            self._navigate_to_path(path)

    def path_selected_from_combobox(self, index: int):
        path = self.ui.cb_dir.itemText(index)
        if os.path.isdir(path) and path != self.current_path:
            self._navigate_to_path(path, add_to_combo=False)

    def button_ok_clicked(self):
        if os.path.exists(self.selected_path):
            self.dialog.accept()
        else:
            QMessageBox.warning(self.dialog, "Caminho inválido", "Selecione um caminho válido.")

    def button_cancel_clicked(self):
        self.dialog.reject()

    def open(self, master):
        self.master = master
        self.dialog.exec()

    def go_up_directory(self):
        parent_path = os.path.dirname(self.current_path.rstrip(os.path.sep))
        if os.path.exists(parent_path) and parent_path != self.current_path:
            self._navigate_to_path(parent_path)
