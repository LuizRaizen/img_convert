# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'to_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QListView, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ToDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(500, 320)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(500, 320))
        Dialog.setMaximumSize(QSize(500, 320))
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.lbl_dir = QLabel(Dialog)
        self.lbl_dir.setObjectName(u"lbl_dir")
        self.lbl_dir.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout.addWidget(self.lbl_dir)

        self.cb_dir = QComboBox(Dialog)
        self.cb_dir.setObjectName(u"cb_dir")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_dir.sizePolicy().hasHeightForWidth())
        self.cb_dir.setSizePolicy(sizePolicy1)
        self.cb_dir.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_dir.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.cb_dir)

        self.bbox_open = QDialogButtonBox(Dialog)
        self.bbox_open.setObjectName(u"bbox_open")
        sizePolicy.setHeightForWidth(self.bbox_open.sizePolicy().hasHeightForWidth())
        self.bbox_open.setSizePolicy(sizePolicy)
        self.bbox_open.setMinimumSize(QSize(30, 0))
        self.bbox_open.setMaximumSize(QSize(30, 25))
        self.bbox_open.setStandardButtons(QDialogButtonBox.Open)

        self.horizontalLayout.addWidget(self.bbox_open)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.lv_files = QListView(Dialog)
        self.lv_files.setObjectName(u"lv_files")
        self.lv_files.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_2.addWidget(self.lv_files)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 11)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_file_name = QLabel(Dialog)
        self.lbl_file_name.setObjectName(u"lbl_file_name")

        self.horizontalLayout_3.addWidget(self.lbl_file_name)

        self.le_file_name = QLineEdit(Dialog)
        self.le_file_name.setObjectName(u"le_file_name")

        self.horizontalLayout_3.addWidget(self.le_file_name)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.bbox_ok_cancel = QDialogButtonBox(Dialog)
        self.bbox_ok_cancel.setObjectName(u"bbox_ok_cancel")
        self.bbox_ok_cancel.setEnabled(True)
        self.bbox_ok_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.bbox_ok_cancel.setOrientation(Qt.Vertical)
        self.bbox_ok_cancel.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_4.addWidget(self.bbox_ok_cancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)
        self.bbox_ok_cancel.accepted.connect(Dialog.accept)
        self.bbox_ok_cancel.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Escolha um local para salvar a imagem", None))
        self.lbl_dir.setText(QCoreApplication.translate("Dialog", u"Diret\u00f3rio:", None))
        self.lbl_file_name.setText(QCoreApplication.translate("Dialog", u"Sele\u00e7\u00e3o:", None))
    # retranslateUi

