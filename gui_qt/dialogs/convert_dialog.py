# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convert_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QListView,
    QProgressBar, QScrollBar, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ConvertDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(500, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(500, 300))
        Dialog.setMaximumSize(QSize(500, 300))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout.addWidget(self.progressBar)

        self.bbox_cancel = QDialogButtonBox(Dialog)
        self.bbox_cancel.setObjectName(u"bbox_cancel")
        sizePolicy.setHeightForWidth(self.bbox_cancel.sizePolicy().hasHeightForWidth())
        self.bbox_cancel.setSizePolicy(sizePolicy)
        self.bbox_cancel.setOrientation(Qt.Horizontal)
        self.bbox_cancel.setStandardButtons(QDialogButtonBox.Cancel)

        self.horizontalLayout.addWidget(self.bbox_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.lbl_more_min = QLabel(Dialog)
        self.lbl_more_min.setObjectName(u"lbl_more_min")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_more_min.sizePolicy().hasHeightForWidth())
        self.lbl_more_min.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lbl_more_min.setFont(font)
        self.lbl_more_min.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.lbl_more_min)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout_9.addWidget(self.listView)

        self.verticalScrollBar = QScrollBar(Dialog)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.horizontalLayout_9.addWidget(self.verticalScrollBar)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.retranslateUi(Dialog)
        self.bbox_cancel.accepted.connect(Dialog.accept)
        self.bbox_cancel.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Convertendo imagens...", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.lbl_more_min.setText(QCoreApplication.translate("Dialog", u"Ver menos...", None))
    # retranslateUi

