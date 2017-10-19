# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(436, 212)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.le_bucket = QtWidgets.QLineEdit(self.centralwidget)
        self.le_bucket.setObjectName("le_bucket")
        self.gridLayout.addWidget(self.le_bucket, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.le_sync_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.le_sync_dir.setObjectName("le_sync_dir")
        self.gridLayout_2.addWidget(self.le_sync_dir, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.tb_browser = QtWidgets.QToolButton(self.centralwidget)
        self.tb_browser.setObjectName("tb_browser")
        self.gridLayout_2.addWidget(self.tb_browser, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 2, 1)
        self.pb_sync = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_sync.sizePolicy().hasHeightForWidth())
        self.pb_sync.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pb_sync.setFont(font)
        self.pb_sync.setObjectName("pb_sync")
        self.gridLayout_4.addWidget(self.pb_sync, 4, 0, 1, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.pb_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.pb_progress.setProperty("value", 24)
        self.pb_progress.setObjectName("pb_progress")
        self.gridLayout_3.addWidget(self.pb_progress, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hs_SCSync"))
        self.label.setText(_translate("MainWindow", "Bucket"))
        self.label_3.setText(_translate("MainWindow", "Sync Dir"))
        self.tb_browser.setText(_translate("MainWindow", "..."))
        self.pb_sync.setText(_translate("MainWindow", "Click to sync!"))
        self.label_2.setText(_translate("MainWindow", "Progress"))

