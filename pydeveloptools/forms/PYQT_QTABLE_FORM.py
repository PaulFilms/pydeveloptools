# Form implementation generated from reading ui file 'Forms_UI/QTABLE_FORM.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 300)
        Dialog.setMinimumSize(QtCore.QSize(450, 300))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        Dialog.setFont(font)
        Dialog.setToolTip("")
        Dialog.setStatusTip("")
        Dialog.setWhatsThis("")
        Dialog.setAccessibleName("")
        Dialog.setAccessibleDescription("")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedKingdom))
        Dialog.setWindowFilePath("")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tbl_form = QtWidgets.QTableWidget(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.tbl_form.setFont(font)
        self.tbl_form.setToolTip("")
        self.tbl_form.setStatusTip("")
        self.tbl_form.setWhatsThis("")
        self.tbl_form.setAccessibleName("")
        self.tbl_form.setAccessibleDescription("")
        self.tbl_form.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_form.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_form.setObjectName("tbl_form")
        self.tbl_form.setColumnCount(0)
        self.tbl_form.setRowCount(0)
        self.tbl_form.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tbl_form, 0, 0, 1, 1)
        self.btn_intro = QtWidgets.QPushButton(parent=Dialog)
        self.btn_intro.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_intro.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(15)
        self.btn_intro.setFont(font)
        self.btn_intro.setToolTip("")
        self.btn_intro.setStatusTip("")
        self.btn_intro.setWhatsThis("")
        self.btn_intro.setAccessibleName("")
        self.btn_intro.setAccessibleDescription("")
        self.btn_intro.setText("INTRO")
        self.btn_intro.setShortcut("")
        self.btn_intro.setObjectName("btn_intro")
        self.gridLayout.addWidget(self.btn_intro, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
