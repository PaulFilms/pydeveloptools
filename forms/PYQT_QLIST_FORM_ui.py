# Form implementation generated from reading ui file 'forms/PYQT_QLIST_FORM.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(291, 207)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        Dialog.setFont(font)
        Dialog.setWindowTitle("LIST FORM")
        Dialog.setToolTip("")
        Dialog.setStatusTip("")
        Dialog.setWhatsThis("")
        Dialog.setAccessibleName("")
        Dialog.setAccessibleDescription("")
        Dialog.setWindowFilePath("")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tx_newitem = QtWidgets.QLineEdit(parent=Dialog)
        self.tx_newitem.setMinimumSize(QtCore.QSize(221, 41))
        self.tx_newitem.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.tx_newitem.setFont(font)
        self.tx_newitem.setToolTip("")
        self.tx_newitem.setStatusTip("")
        self.tx_newitem.setWhatsThis("")
        self.tx_newitem.setAccessibleName("")
        self.tx_newitem.setAccessibleDescription("")
        self.tx_newitem.setInputMask("")
        self.tx_newitem.setText("")
        self.tx_newitem.setPlaceholderText("")
        self.tx_newitem.setObjectName("tx_newitem")
        self.gridLayout.addWidget(self.tx_newitem, 0, 0, 1, 1)
        self.lst_items = QtWidgets.QListWidget(parent=Dialog)
        self.lst_items.setMinimumSize(QtCore.QSize(221, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lst_items.setFont(font)
        self.lst_items.setToolTip("")
        self.lst_items.setStatusTip("")
        self.lst_items.setWhatsThis("")
        self.lst_items.setAccessibleName("")
        self.lst_items.setAccessibleDescription("")
        self.lst_items.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedKingdom))
        self.lst_items.setAlternatingRowColors(True)
        self.lst_items.setProperty("isWrapping", False)
        self.lst_items.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.lst_items.setUniformItemSizes(False)
        self.lst_items.setWordWrap(False)
        self.lst_items.setSelectionRectVisible(False)
        self.lst_items.setObjectName("lst_items")
        self.gridLayout.addWidget(self.lst_items, 1, 0, 4, 1)
        self.btn_del = QtWidgets.QPushButton(parent=Dialog)
        self.btn_del.setMinimumSize(QtCore.QSize(41, 41))
        self.btn_del.setMaximumSize(QtCore.QSize(41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(14)
        font.setBold(False)
        self.btn_del.setFont(font)
        self.btn_del.setToolTip("")
        self.btn_del.setStatusTip("")
        self.btn_del.setWhatsThis("")
        self.btn_del.setAccessibleName("")
        self.btn_del.setAccessibleDescription("")
        self.btn_del.setText("-")
        self.btn_del.setShortcut("")
        self.btn_del.setObjectName("btn_del")
        self.gridLayout.addWidget(self.btn_del, 1, 1, 1, 1)
        self.btn_add = QtWidgets.QPushButton(parent=Dialog)
        self.btn_add.setMinimumSize(QtCore.QSize(41, 41))
        self.btn_add.setMaximumSize(QtCore.QSize(41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(14)
        font.setBold(False)
        self.btn_add.setFont(font)
        self.btn_add.setToolTip("")
        self.btn_add.setStatusTip("")
        self.btn_add.setWhatsThis("")
        self.btn_add.setAccessibleName("")
        self.btn_add.setAccessibleDescription("")
        self.btn_add.setText("+")
        self.btn_add.setShortcut("")
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 0, 1, 1, 1)
        self.btn_up = QtWidgets.QPushButton(parent=Dialog)
        self.btn_up.setMinimumSize(QtCore.QSize(41, 41))
        self.btn_up.setMaximumSize(QtCore.QSize(41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(False)
        self.btn_up.setFont(font)
        self.btn_up.setToolTip("")
        self.btn_up.setStatusTip("")
        self.btn_up.setWhatsThis("")
        self.btn_up.setAccessibleName("")
        self.btn_up.setAccessibleDescription("")
        self.btn_up.setText("U")
        self.btn_up.setShortcut("")
        self.btn_up.setObjectName("btn_up")
        self.gridLayout.addWidget(self.btn_up, 2, 1, 1, 1)
        self.btn_down = QtWidgets.QPushButton(parent=Dialog)
        self.btn_down.setMinimumSize(QtCore.QSize(41, 41))
        self.btn_down.setMaximumSize(QtCore.QSize(41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(False)
        self.btn_down.setFont(font)
        self.btn_down.setToolTip("")
        self.btn_down.setStatusTip("")
        self.btn_down.setWhatsThis("")
        self.btn_down.setAccessibleName("")
        self.btn_down.setAccessibleDescription("")
        self.btn_down.setText("D")
        self.btn_down.setShortcut("")
        self.btn_down.setObjectName("btn_down")
        self.gridLayout.addWidget(self.btn_down, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.btn_del.clicked.connect(self.lst_items.clearSelection) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tx_newitem, self.btn_add)
        Dialog.setTabOrder(self.btn_add, self.lst_items)
        Dialog.setTabOrder(self.lst_items, self.btn_del)
        Dialog.setTabOrder(self.btn_del, self.btn_up)
        Dialog.setTabOrder(self.btn_up, self.btn_down)

    def retranslateUi(self, Dialog):
        pass
