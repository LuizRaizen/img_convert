# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'img_convert.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(580, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(580, 460))
        MainWindow.setMaximumSize(QSize(580, 460))
        self.actionNovo = QAction(MainWindow)
        self.actionNovo.setObjectName(u"actionNovo")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionSair = QAction(MainWindow)
        self.actionSair.setObjectName(u"actionSair")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frm_paths = QFrame(self.frame_2)
        self.frm_paths.setObjectName(u"frm_paths")
        self.frm_paths.setFrameShape(QFrame.StyledPanel)
        self.frm_paths.setFrameShadow(QFrame.Raised)
        self.frm_paths.setLineWidth(5)
        self.verticalLayout_4 = QVBoxLayout(self.frm_paths)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_convert_from = QLabel(self.frm_paths)
        self.lbl_convert_from.setObjectName(u"lbl_convert_from")

        self.verticalLayout_4.addWidget(self.lbl_convert_from)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_convert_from = QLineEdit(self.frm_paths)
        self.le_convert_from.setObjectName(u"le_convert_from")

        self.horizontalLayout.addWidget(self.le_convert_from)

        self.btn_from_search = QPushButton(self.frm_paths)
        self.btn_from_search.setObjectName(u"btn_from_search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_from_search.sizePolicy().hasHeightForWidth())
        self.btn_from_search.setSizePolicy(sizePolicy1)
        self.btn_from_search.setMaximumSize(QSize(25, 16777215))
        self.btn_from_search.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_from_search)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.lbl_save_in = QLabel(self.frm_paths)
        self.lbl_save_in.setObjectName(u"lbl_save_in")

        self.verticalLayout_4.addWidget(self.lbl_save_in)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.le_save_in = QLineEdit(self.frm_paths)
        self.le_save_in.setObjectName(u"le_save_in")

        self.horizontalLayout_2.addWidget(self.le_save_in)

        self.btn_to_search = QPushButton(self.frm_paths)
        self.btn_to_search.setObjectName(u"btn_to_search")
        self.btn_to_search.setMaximumSize(QSize(25, 16777215))
        self.btn_to_search.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_to_search)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.label = QLabel(self.frm_paths)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.cb_formats = QComboBox(self.frm_paths)
        self.cb_formats.setObjectName(u"cb_formats")
        self.cb_formats.setMaximumSize(QSize(450, 16777215))

        self.verticalLayout_4.addWidget(self.cb_formats)


        self.verticalLayout_5.addWidget(self.frm_paths)

        self.verticalSpacer_2 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.frm_options = QFrame(self.frame_2)
        self.frm_options.setObjectName(u"frm_options")
        self.frm_options.setMaximumSize(QSize(16777215, 120))
        self.frm_options.setFrameShape(QFrame.NoFrame)
        self.frm_options.setFrameShadow(QFrame.Raised)
        self.frm_options.setLineWidth(1)
        self.horizontalLayout_8 = QHBoxLayout(self.frm_options)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox = QGroupBox(self.frm_options)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.rad_onefile = QRadioButton(self.groupBox)
        self.rad_onefile.setObjectName(u"rad_onefile")
        self.rad_onefile.setChecked(True)

        self.verticalLayout_3.addWidget(self.rad_onefile)

        self.rad_directory = QRadioButton(self.groupBox)
        self.rad_directory.setObjectName(u"rad_directory")

        self.verticalLayout_3.addWidget(self.rad_directory)


        self.horizontalLayout_8.addWidget(self.groupBox)


        self.verticalLayout_5.addWidget(self.frm_options)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_convert = QPushButton(self.frame)
        self.btn_convert.setObjectName(u"btn_convert")
        self.btn_convert.setMaximumSize(QSize(200, 40))
        self.btn_convert.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_convert)


        self.verticalLayout_5.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 580, 22))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        self.menuAjuda = QMenu(self.menubar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        self.menuAjuda_2 = QMenu(self.menubar)
        self.menuAjuda_2.setObjectName(u"menuAjuda_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.menubar.addAction(self.menuAjuda_2.menuAction())
        self.menuArquivo.addAction(self.actionNovo)
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionSair)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IMG Convert", None))
        self.actionNovo.setText(QCoreApplication.translate("MainWindow", u"Novo", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionSair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.lbl_convert_from.setText(QCoreApplication.translate("MainWindow", u"Converter de...", None))
        self.btn_from_search.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lbl_save_in.setText(QCoreApplication.translate("MainWindow", u"Salvar em...", None))
        self.btn_to_search.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Formato de sa\u00edda:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Modo de convers\u00e3o:", None))
        self.rad_onefile.setText(QCoreApplication.translate("MainWindow", u"Uma \u00fanica imagem", None))
        self.rad_directory.setText(QCoreApplication.translate("MainWindow", u"V\u00e1rias imagens em um diret\u00f3rio", None))
        self.btn_convert.setText(QCoreApplication.translate("MainWindow", u"Converter", None))
        self.menuArquivo.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.menuAjuda_2.setTitle(QCoreApplication.translate("MainWindow", u"Ajuda", None))
    # retranslateUi

