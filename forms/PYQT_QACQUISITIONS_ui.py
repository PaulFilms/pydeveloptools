# Form implementation generated from reading ui file 'forms/PYQT_QACQUISITIONS.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(388, 477)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        Dialog.setFont(font)
        Dialog.setWhatsThis("")
        Dialog.setAccessibleName("")
        Dialog.setAccessibleDescription("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tx_cal_devinfo = QtWidgets.QLineEdit(parent=Dialog)
        self.tx_cal_devinfo.setMinimumSize(QtCore.QSize(0, 27))
        self.tx_cal_devinfo.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        self.tx_cal_devinfo.setFont(font)
        self.tx_cal_devinfo.setToolTip("")
        self.tx_cal_devinfo.setStatusTip("")
        self.tx_cal_devinfo.setWhatsThis("")
        self.tx_cal_devinfo.setAccessibleName("")
        self.tx_cal_devinfo.setAccessibleDescription("")
        self.tx_cal_devinfo.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.tx_cal_devinfo.setInputMask("")
        self.tx_cal_devinfo.setText("")
        self.tx_cal_devinfo.setFrame(True)
        self.tx_cal_devinfo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tx_cal_devinfo.setReadOnly(True)
        self.tx_cal_devinfo.setPlaceholderText("")
        self.tx_cal_devinfo.setObjectName("tx_cal_devinfo")
        self.verticalLayout.addWidget(self.tx_cal_devinfo)
        self.grp_value = QtWidgets.QGroupBox(parent=Dialog)
        self.grp_value.setMinimumSize(QtCore.QSize(0, 170))
        self.grp_value.setMaximumSize(QtCore.QSize(16777215, 170))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(7)
        self.grp_value.setFont(font)
        self.grp_value.setToolTip("")
        self.grp_value.setStatusTip("")
        self.grp_value.setWhatsThis("")
        self.grp_value.setAccessibleName("")
        self.grp_value.setAccessibleDescription("")
        self.grp_value.setTitle("TYPE / VALUE / UNIT")
        self.grp_value.setObjectName("grp_value")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.grp_value)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tx_value = QtWidgets.QLineEdit(parent=self.grp_value)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(self.tx_value.sizePolicy().hasHeightForWidth())
        self.tx_value.setSizePolicy(sizePolicy)
        self.tx_value.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.tx_value.setFont(font)
        self.tx_value.setToolTip("")
        self.tx_value.setStatusTip("")
        self.tx_value.setWhatsThis("")
        self.tx_value.setAccessibleName("")
        self.tx_value.setAccessibleDescription("")
        self.tx_value.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tx_value.setInputMask("")
        self.tx_value.setText("")
        self.tx_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tx_value.setPlaceholderText("")
        self.tx_value.setObjectName("tx_value")
        self.gridLayout_3.addWidget(self.tx_value, 1, 0, 1, 1)
        self.cb_type = QtWidgets.QComboBox(parent=self.grp_value)
        self.cb_type.setMinimumSize(QtCore.QSize(300, 30))
        self.cb_type.setMaximumSize(QtCore.QSize(2000000, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.cb_type.setFont(font)
        self.cb_type.setToolTip("")
        self.cb_type.setStatusTip("")
        self.cb_type.setWhatsThis("")
        self.cb_type.setAccessibleName("")
        self.cb_type.setAccessibleDescription("")
        self.cb_type.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.cb_type.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedKingdom))
        self.cb_type.setCurrentText("")
        self.cb_type.setObjectName("cb_type")
        self.gridLayout_3.addWidget(self.cb_type, 0, 0, 1, 2)
        self.btn_addvalue = QtWidgets.QPushButton(parent=self.grp_value)
        self.btn_addvalue.setMinimumSize(QtCore.QSize(350, 40))
        self.btn_addvalue.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_addvalue.setFont(font)
        self.btn_addvalue.setToolTip("")
        self.btn_addvalue.setStatusTip("")
        self.btn_addvalue.setWhatsThis("")
        self.btn_addvalue.setAccessibleName("")
        self.btn_addvalue.setAccessibleDescription("")
        self.btn_addvalue.setText("ADD VALUE")
        self.btn_addvalue.setShortcut("")
        self.btn_addvalue.setObjectName("btn_addvalue")
        self.gridLayout_3.addWidget(self.btn_addvalue, 2, 0, 1, 2)
        self.cb_units = QtWidgets.QComboBox(parent=self.grp_value)
        self.cb_units.setMinimumSize(QtCore.QSize(120, 45))
        self.cb_units.setMaximumSize(QtCore.QSize(120, 45))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.cb_units.setFont(font)
        self.cb_units.setToolTip("")
        self.cb_units.setStatusTip("")
        self.cb_units.setWhatsThis("")
        self.cb_units.setAccessibleName("")
        self.cb_units.setAccessibleDescription("")
        self.cb_units.setEditable(False)
        self.cb_units.setCurrentText("")
        self.cb_units.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.cb_units.setDuplicatesEnabled(True)
        self.cb_units.setFrame(True)
        self.cb_units.setObjectName("cb_units")
        self.gridLayout_3.addWidget(self.cb_units, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.grp_value)
        self.grp_list = QtWidgets.QGroupBox(parent=Dialog)
        self.grp_list.setMinimumSize(QtCore.QSize(0, 250))
        self.grp_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(7)
        self.grp_list.setFont(font)
        self.grp_list.setToolTip("")
        self.grp_list.setStatusTip("")
        self.grp_list.setWhatsThis("")
        self.grp_list.setAccessibleName("")
        self.grp_list.setAccessibleDescription("")
        self.grp_list.setTitle("ACQUISITIONS")
        self.grp_list.setObjectName("grp_list")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.grp_list)
        self.gridLayout_2.setContentsMargins(20, -1, 20, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_delete = QtWidgets.QPushButton(parent=self.grp_list)
        self.btn_delete.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_delete.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        self.btn_delete.setFont(font)
        self.btn_delete.setToolTip("")
        self.btn_delete.setStatusTip("")
        self.btn_delete.setWhatsThis("")
        self.btn_delete.setAccessibleName("")
        self.btn_delete.setAccessibleDescription("")
        self.btn_delete.setText("DEL. VALUE")
        self.btn_delete.setShortcut("")
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout_2.addWidget(self.btn_delete, 1, 1, 1, 1)
        self.btn_exit = QtWidgets.QPushButton(parent=self.grp_list)
        self.btn_exit.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_exit.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        self.btn_exit.setFont(font)
        self.btn_exit.setToolTip("")
        self.btn_exit.setStatusTip("")
        self.btn_exit.setWhatsThis("")
        self.btn_exit.setAccessibleName("")
        self.btn_exit.setAccessibleDescription("")
        self.btn_exit.setText("SAVE & EXIT")
        self.btn_exit.setShortcut("")
        self.btn_exit.setObjectName("btn_exit")
        self.gridLayout_2.addWidget(self.btn_exit, 1, 2, 1, 1)
        self.btn_left = QtWidgets.QPushButton(parent=self.grp_list)
        self.btn_left.setEnabled(False)
        self.btn_left.setMinimumSize(QtCore.QSize(50, 40))
        self.btn_left.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        font.setBold(True)
        self.btn_left.setFont(font)
        self.btn_left.setToolTip("")
        self.btn_left.setStatusTip("")
        self.btn_left.setWhatsThis("")
        self.btn_left.setAccessibleName("")
        self.btn_left.setAccessibleDescription("")
        self.btn_left.setText("<")
        self.btn_left.setShortcut("")
        self.btn_left.setObjectName("btn_left")
        self.gridLayout_2.addWidget(self.btn_left, 1, 0, 1, 1)
        self.btn_right = QtWidgets.QPushButton(parent=self.grp_list)
        self.btn_right.setEnabled(False)
        self.btn_right.setMinimumSize(QtCore.QSize(50, 40))
        self.btn_right.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        font.setBold(True)
        self.btn_right.setFont(font)
        self.btn_right.setToolTip("")
        self.btn_right.setStatusTip("")
        self.btn_right.setWhatsThis("")
        self.btn_right.setAccessibleName("")
        self.btn_right.setAccessibleDescription("")
        self.btn_right.setText(">")
        self.btn_right.setShortcut("")
        self.btn_right.setObjectName("btn_right")
        self.gridLayout_2.addWidget(self.btn_right, 1, 3, 1, 1)
        self.tbl_values = QtWidgets.QTableWidget(parent=self.grp_list)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        self.tbl_values.setFont(font)
        self.tbl_values.setToolTip("")
        self.tbl_values.setStatusTip("")
        self.tbl_values.setWhatsThis("")
        self.tbl_values.setAccessibleName("")
        self.tbl_values.setAccessibleDescription("")
        self.tbl_values.setAlternatingRowColors(True)
        self.tbl_values.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_values.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_values.setObjectName("tbl_values")
        self.tbl_values.setColumnCount(2)
        self.tbl_values.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setText("TYPE")
        self.tbl_values.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("VALUE")
        self.tbl_values.setHorizontalHeaderItem(1, item)
        self.tbl_values.horizontalHeader().setDefaultSectionSize(100)
        self.tbl_values.horizontalHeader().setMinimumSectionSize(25)
        self.tbl_values.verticalHeader().setVisible(False)
        self.tbl_values.verticalHeader().setDefaultSectionSize(35)
        self.tbl_values.verticalHeader().setHighlightSections(True)
        self.tbl_values.verticalHeader().setMinimumSectionSize(35)
        self.gridLayout_2.addWidget(self.tbl_values, 0, 0, 1, 4)
        self.verticalLayout.addWidget(self.grp_list)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ACQUISITIONS"))
