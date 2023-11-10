'''
# Toolkit with simplified functions and methods for development with PyQt6

\n
`TASK:`
    - TBL_POP_PANDAS_DF: 
        - Leer el DEBUG
        - Indicar el tipo de dato para preparar la columna ejem: "field": {"type": bool, "data": []}
    - FORMULARIOS:
        - Hay que estudiar el uso de QtCore.pyqtSignal(str)
        - El valor de la class tiene que ser data (por que hay casos que no obtienes un solo valor)
        - Quitar el .ui de todos los formularios
    - crear la función "dataframe_to_txt" para aislar la libreria de SYS

\n
`WARNINGS:`
'''
__update__ = '2023.11.10'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import pandas as pd
from dataclasses import dataclass
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import QEventLoop, QTimer, QDate, QTime, Qt
from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QInputDialog
from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QTextEdit, QComboBox, QSpinBox, QDoubleSpinBox, QCheckBox, QDateEdit, QTimeEdit, QPushButton,
    QHBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem)
from PyQt6.QtGui import QColor, QFont

''' CUSTOM MAIN LIBRARIES '''
pass

''' GLOBAL VARIABLES '''
pass


''' FUNCTIONS
--------------------------------------------------------
'''

def TIME_SLEEP(SEG: float=1):
    '''
    time.sleep function for use with PyQt 
    '''
    time = float(SEG) * 1000
    try:
        time = int(time)
    except:
        time = 10
        print(f"TIME_SLEEP ERROR / TIME (s): {SEG}")
    loop = QEventLoop()
    QTimer.singleShot(time, loop.quit)
    loop.exec()

def DATE_STR_CONVERTER(DATE: str = "2023-01-01") -> QDate:
    '''
    Convert string ISO format date to QDate
    DATE str Format: yyyy-mm-dd 
    '''
    if DATE == "2020-01-01" or DATE == "2020-1-1":
        return None
    try:
        ## OLD METHOD
        # year: int = int(DATE[:4])
        # month: int = int(DATE[5:-3])
        # day: int = int(DATE[-2:])
        ## NEW METHOD
        date_list = DATE.split("-")
        if len(date_list) != 3:
            date_list = DATE.split("/")
        if len(date_list) != 3:
            date_list = DATE.split(".")
        ## GET VALUES
        year = int(date_list[0])
        month = int(date_list[1])
        day = int(date_list[2])
        date = QDate(year, month, day)
        return date
    except:
        return None

def DATE_QDATE_CONVERTER(DATE: QDate) -> str:
    '''
    Convert QDate to string ISO format date
    DATE str Format: yyyy-mm-dd 
    '''
    if DATE == None:
        return None
    YEAR = DATE.year()
    MONTH = f"{DATE.month():02d}"
    DAY = f'{DATE.day():02d}'
    DATE = f"{YEAR}-{MONTH}-{DAY}"
    return DATE
    
def TIME_STR_CONVERTER(TIME: str = "00:00") -> QTime:
    '''
    Convert string format time to QTime
    TIME str Format: hh:mm
    '''
    try:
        hour: int = int(TIME[:2])
        minute: int = int(TIME[-2:])
        time = QTime(hour, minute)
        return time
    except:
        return None


''' WIDGETS
--------------------------------------------------------
'''

def WIDGET_WR(WIDGET, VALUE: None) -> None:
    '''
    Edit value in selected QtWidgets \n
    `Supported QtWidgets:`
        - QTextEdit / QLineEdit
        - QComboBox
        - QSpinBox / QDoubleSpinBox
        - QCheckBox
        - QDateEdit <str: "yyyy-mm-dd"> / QTimeEdit <str: "hh:mm">
        - QPushButton
        - QWidget (Layout) <QCheckBox>
    
    `DEBUG:` 
        - QSpinBox:
            - tener en cuenta el caso en se use un valor con coma o negativo
            - tener en cuenta minimo y maximo
    '''
    ## QLineEdit
    if type(WIDGET) == QLineEdit or type(WIDGET) == QTextEdit:
        if VALUE == None: 
            WIDGET.setText("")
        else: 
            WIDGET.setText(str(VALUE))
    ## QComboBox
    elif type(WIDGET) == QComboBox:
        if WIDGET.count() == 0:
            WIDGET.addItem(str(VALUE))
        WIDGET.setCurrentIndex(WIDGET.findText(VALUE))
    ## QSpinBox
    elif type(WIDGET) == QSpinBox:
        if VALUE == None:
            WIDGET.setValue(WIDGET.minimum())
        else:
            WIDGET.setValue(int(VALUE))
    ## QDoubleSpinBox
    elif type(WIDGET) == QDoubleSpinBox:
        if VALUE == None:
            WIDGET.setValue(WIDGET.minimum())
        else:
            WIDGET.setValue(float(VALUE))
    ## QCheckBox
    elif type(WIDGET) == QCheckBox:
        if VALUE == 1 or VALUE == "1" or VALUE == True or VALUE == "TRUE": 
            WIDGET.setChecked(True)
        else: 
            WIDGET.setChecked(False)
    ## QDateEdit
    elif type(WIDGET) == QDateEdit:
        if VALUE == None:
            WIDGET.setDate(QDate(WIDGET.minimumDate()))
        elif type(VALUE) == QDate:
            WIDGET.setDate(VALUE)
        elif type(VALUE) == str: # 2023-01-01 / 2023-1-1
            DATE = DATE_STR_CONVERTER(VALUE)
            if DATE:
                WIDGET.setDate(DATE)
            else:
                WIDGET.setDate(QDate(WIDGET.minimumDate()))
    ## QTimeEdit
    elif type(WIDGET) == QTimeEdit:
        if type(VALUE) == QTime:
            WIDGET.setDate(VALUE)
        elif VALUE and type(VALUE) == str and len(VALUE) == 5: # 01:12
            WIDGET.setDate(DATE_STR_CONVERTER(VALUE))
        else:
            WIDGET.setDate(QDate(WIDGET.minimumDate()))
    ## QPushButton
    elif type(WIDGET) == QPushButton:
        WIDGET.setText(str(VALUE))
    ## QWidget <LAYOUT>
    elif type(WIDGET) == QWidget:
        # QCheckBox
        CHILD = WIDGET.findChild(type(QCheckBox()))
        if type(CHILD) == QCheckBox:
            if VALUE == 1 or VALUE == True or VALUE == "TRUE":
                CHILD.setChecked(True)
            else: 
                CHILD.setChecked(False)
    ## NOT IMPLEMENTED
    else:
        print("WIDGET_WR", type(WIDGET), "/ NOT IMPLEMENTED")

def WIDGET_RD(WIDGET):
    '''
    Read value of selected QtWidgets

    `Supported QtWidgets:`
        - QTextEdit / QLineEdit
        - QComboBox
        - QSpinBox / QDoubleSpinBox
        - QCheckBox
        - QDateEdit <str: "yyyy-mm-dd"> / QTimeEdit <str: "hh:mm">
    '''
    VALUE = None
    ## QLineEdit
    if type(WIDGET) == QLineEdit:
        VALUE = WIDGET.text()
    ## QTextEdit
    elif type(WIDGET) == QTextEdit:
        VALUE = WIDGET.toPlainText()
    ## QComboBox
    elif type(WIDGET) == QComboBox:
        VALUE = WIDGET.currentText()
    ## QCheckBox
    elif type(WIDGET) == QCheckBox:
        VALUE = WIDGET.isChecked()
    ## QSpinBox
    elif type(WIDGET) == QSpinBox:
        VALUE = WIDGET.value()
    ## QDoubleSpinBox
    elif type(WIDGET) == QDoubleSpinBox:
        VALUE = WIDGET.value()
    ## QDateEdit
    elif type(WIDGET) == QDateEdit:
        VALUE = WIDGET.date()
        if VALUE != WIDGET.minimumDate():
            VALUE = DATE_QDATE_CONVERTER(VALUE)
        else:
            VALUE = None
    ## QTimeEdit
    elif type(WIDGET) == QTimeEdit:
        VALUE = WIDGET.time()
        VALUE = f"{VALUE.hour()}:{VALUE.minute()}"
    ## NOT IMPLEMENTED
    else:
        print("WIDGET_RD", type(WIDGET), "/ NOT IMPLEMENTED")
    return VALUE

def WIDGET_CLEAR(WIDGET, widgetEnabled: bool = False):
    '''
    Clear data of select widget \n
    `Supported QtWidgets:`
        - QComboBox
        - QLineEdit / QTextEdit
        - QCheckBox
        - QSpinBox
        - QDateEdit
        - QTimeEdit
        - QTableWidget

    ** widgetEnabled: Set the widget like "not enabled" before to clear \n
    ** with QTableWidget only set to 0 the row count \n
    
    `DEBUG:`
        - QComboBox:
            - Hay que ver si merece la pena hacer clear
    '''
    if widgetEnabled: 
        WIDGET.setEnabled(False)
    ## QComboBox
    if type(WIDGET) == QComboBox:
        WIDGET.clear()
        WIDGET.setCurrentText("")
    ## QLineEdit
    elif type(WIDGET) == QLineEdit:
        WIDGET.setText("")
    ## QTextEdit
    elif type(WIDGET) == QTextEdit:
        WIDGET.setText("")
    ## QCheckBox
    elif type(WIDGET) == QCheckBox:
        WIDGET.setChecked(False)
    ## QSpinBox
    elif type(WIDGET) == QSpinBox:
        WIDGET.setValue(WIDGET.minimum())
    ## QDoubleSpinBox
    elif type(WIDGET) == QDoubleSpinBox:
        WIDGET.setValue(WIDGET.minimum())
    ## QDateEdit
    elif type(WIDGET) == QDateEdit:
        WIDGET.setDate(QDate(WIDGET.minimumDate()))
    ## QTimeEdit
    elif type(WIDGET) == QTimeEdit:
        WIDGET.setTime(QTime(WIDGET.minimumTime()))
    ## QTableWidget
    elif type(WIDGET) == QTableWidget:
        WIDGET.setRowCount(0)
    ## QWidget <LAYOUT>
    elif type(WIDGET) == QWidget:
        # QCheckBox
        CHILD = WIDGET.findChild(type(QCheckBox()))
        if type(CHILD) == QCheckBox:
            CHILD.setChecked(False)
    ## NOT IMPLEMENTED
    else:
        print("WIDGET_CLEAR", type(WIDGET), "/ NOT IMPLEMENTED")
    if widgetEnabled: 
        WIDGET.setEnabled(True)

def WIDGET_CONNECT(WIDGET, FUNCTION):
    '''
    Connect select widget with selected function\n
    `Supported QtWidgets:`
        - QComboBox
        - QLineEdit / QTextEdit
        - QCheckBox
        - QSpinBox
        - QDoubleSpinBox
        - QDateEdit
        - QTimeEdit
        - QWidget <LAYOUT>: QCheckBox
    '''
    ## QComboBox
    if type(WIDGET) == QComboBox:
        WIDGET.currentTextChanged.connect(FUNCTION)
    ## QLineEdit / QTextEdit
    elif type(WIDGET) == QLineEdit or type(WIDGET) == QTextEdit:
        WIDGET.textChanged.connect(FUNCTION)
    ## QCheckBox
    elif type(WIDGET) == QCheckBox:
        WIDGET.stateChanged.connect(FUNCTION)
    ## QSpinBox
    elif type(WIDGET) == QSpinBox:
        WIDGET.valueChanged.connect(FUNCTION)
    ## QDoubleSpinBox
    elif type(WIDGET) == QDoubleSpinBox:
        WIDGET.valueChanged.connect(FUNCTION)
    ## QDateEdit
    elif type(WIDGET) == QDateEdit:
        WIDGET.dateChanged.connect(FUNCTION)
    ## QTimeEdit
    elif type(WIDGET) == QTimeEdit:
        WIDGET.timeChanged.connect(FUNCTION)
    ## QWidget <LAYOUT>
    elif type(WIDGET) == QWidget:
        # QCheckBox
        CHILD = WIDGET.findChild(type(QCheckBox()))
        if type(CHILD) == QCheckBox:
            CHILD.stateChanged.connect(FUNCTION)
    ## NOT IMPLEMENTED
    else:
        print("WIDGET_CONNECT", type(WIDGET), "/ NOT IMPLEMENTED")

def CELL_WR(TABLE: QTableWidget, ROW: int, COLUMN: int | str, VALUE):
    '''
    Write value in select cell
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    WIDGET = TABLE.cellWidget(ROW, COLUMN_INDEX)
    if WIDGET:
        WIDGET_WR(WIDGET, VALUE)
    else:
        if VALUE == None:
            valueStr = ""
        else:
            valueStr = str(VALUE)
        ITEM = QTableWidgetItem(valueStr)
        TABLE.setItem(ROW, COLUMN_INDEX, ITEM)

def CELL_RD(TABLE: QTableWidget, ROW: int, COLUMN: int | str):
    '''
    Read value of select cell \n
    `Supported cellWidget:`
        - cellWidget
        - QLineEdit / QTextEdit
        - QComboBox
        - QSpinBox
        - QSpinBox / QDoubleSpinBox
        - QCheckBox
        - QDateEdit
    
    `DEBUG:` 
        - QPushButton: De un boton se puede obtener el nombre para automatizar procesos
        - QCheckBox: Al usar un layout para centrarlo, hay que mirar dentro del layout
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    ITEM = TABLE.item(ROW, COLUMN_INDEX)
    CELL = TABLE.cellWidget(ROW, COLUMN_INDEX)
    value = ""
    # CELL
    if CELL == None:
        if ITEM == None:
            value = ""
        else:
            value = ITEM.text()
    # QLineEdit / QTextEdit
    elif type(CELL) == QLineEdit or type(CELL) == QTextEdit:
        value = ITEM.text()
    # QComboBox
    elif type(CELL) == QComboBox:
        value = CELL.currentText()
    # QCheckBox
    elif type(CELL) == QCheckBox:
        value = CELL.isChecked()
    # QSpinBox / QDoubleSpinBox
    elif type(CELL) == QSpinBox or type(CELL) == QDoubleSpinBox:
        value = CELL.value()
    # QPushButton
    elif type(CELL) == QPushButton:
        value = CELL.text()
    ## QDateEdit
    elif type(CELL) == QDateEdit:
        value = CELL.date()
        value = DATE_QDATE_CONVERTER(value)
    ## QWidget <LAYOUT> QCheckBox
    elif type(CELL) == QWidget:
        # QCheckBox
        CHILD = CELL.findChild(type(QCheckBox()))
        if type(CHILD) == QCheckBox:
            value = CHILD.isChecked()
    ## NOT IMPLEMENTED
    else:
        print("CELL_RD", type(CELL), "/ NOT IMPLEMENTED")
    # 
    return value

def CELL_READONLY(TABLE: QTableWidget, ROW: int, COLUMN: int | str):
    '''
    Set the cell as non-editable \n
    `Info:`
        - If you edit a protected cell, the cell loses protection
    
    `DEBUG:`
        - Si la celda no tiene widget y no tiene ningun valor escrito, obtiene un None como item, la solución es escribir ""
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ## Make non-editable
    ITEM = TABLE.item(ROW, COLUMN_INDEX)
    CELL = TABLE.cellWidget(ROW, COLUMN_INDEX)
    # print(ITEM, CELL)
    if CELL != None:
        CELL.setEnabled(False)
    if ITEM != None: 
        ITEM.setFlags(ITEM.flags() ^ Qt.ItemFlag.ItemIsEditable)

def CELL_TX(TABLE: QTableWidget, ROW: int, COLUMN: int | str, TEXT: bool | str | int | float) -> None:
    '''
    Set Text Item in selected cell \n
    `DEBUG:`
        - La pongo para usar WR para editar cells con widgets y esta para forzar solo texto
        - Forzar la escritura de texto, y en caso de recibir texto usar ""
        - Añadir la funcion ReadOnly
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    text = TEXT
    if TEXT == None:
        text = ""
    TABLE.setCellWidget(ROW,COLUMN_INDEX,None)
    TABLE.setItem(ROW, COLUMN_INDEX, QTableWidgetItem(str(text)))

def CELL_COMBOBOX(TABLE: QTableWidget, ROW: int, COLUMN: int | str, LIST: list, EDITABLE: bool = False) -> None:
    '''
    setCellWidget -> QComboBox
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    combo = QComboBox()
    combo.setEditable(EDITABLE)
    combo.list = LIST
    combo.addItems(LIST)
    ##
    TABLE.setCellWidget(ROW,COLUMN_INDEX,combo)

def CELL_CHECKBOX(TABLE: QTableWidget, ROW: int, COLUMN: int | str, STATE: bool = False) -> None:
    '''
    setCellWidget -> QWidget
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    checkBox = QCheckBox()
    if STATE == 1 or STATE == True or STATE == "TRUE":
        checkBox.setChecked(True)
    else:
        checkBox.setChecked(False)
    ##
    TABLE.setCellWidget(ROW, COLUMN_INDEX, checkBox)

def CELL_CHECKBOB_LAYOUT(TABLE: QTableWidget, ROW: int, COLUMN: int | str, STATE: bool = False) -> None:
    '''
    setCellWidget -> QWidget <QCheckBox>
    Set the QCheckBox centered into cell
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    widget = QWidget()
    item = QCheckBox()
    if STATE == 1 or STATE == "1" or STATE == True or STATE == "TRUE":
        item.setChecked(True)
    else:
        item.setChecked(False)
    def select_cell() -> None:
        TABLE.setCurrentCell(ROW,COLUMN_INDEX)
    item.stateChanged.connect(select_cell)
    layout = QHBoxLayout()
    layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    layout.addWidget(item)
    layout.setContentsMargins(0,0,0,0)
    widget.setLayout(layout)
    ##
    TABLE.setCellWidget(ROW, COLUMN_INDEX, widget)

def CELL_SPINBOX(TABLE: QTableWidget, ROW: int, COLUMN: int | str, VALUE: int = 0, MIN: int = 0, MAX: int = 99):
    '''
    setCellWidget -> QSpinBox
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    widget = QSpinBox()
    widget.setValue(VALUE)
    widget.setMinimum(MIN)
    widget.setMaximum(MAX)
    ##
    TABLE.setCellWidget(ROW, COLUMN_INDEX, widget)

def CELL_DATEEDIT(TABLE: QTableWidget, ROW: int, COLUMN: int | str) -> None:
    '''
    setCellWidget -> QDateEdit
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    widget = QDateEdit()
    widget.setSpecialValueText("-")
    widget.setMinimumDate(QDate(2020,1,1))
    widget.setMaximumDate(QDate(2100,1,1))
    widget.setDisplayFormat("yyyy-MM-dd")
    ##
    TABLE.setCellWidget(ROW, COLUMN_INDEX, widget)

def CELL_FONT(TABLE: QTableWidget, ROW: int, COLUMN: int | str, SIZE: int=10, BOLD: bool=True, fontFamily="Consolas"):
    '''
    INCOMPLETE
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    font = QFont()
    font.setFamily(fontFamily)
    font.setPointSize(SIZE)
    font.setBold(BOLD)
    ITEM = TABLE.item(ROW, COLUMN_INDEX)
    # print("ITEM: ", ITEM)
    if ITEM == None: 
        TABLE.setItem(ROW, COLUMN_INDEX, QTableWidgetItem(""))
    ITEM.setFont(font)

def CELL_COLOR(TABLE: QTableWidget, ROW: int, COLUMN: int | str, COLOR: str="GREEN"):
    '''
    Set the backgroung Color of a cel with selected str color:
    - GREEN
    - YELLOW
    - RED

    `DEBUG:`
        - Usar el metodo adecuado para definir los colores con QColor
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    ITEM = TABLE.item(ROW, COLUMN_INDEX)
    CELL = TABLE.cellWidget(ROW, COLUMN_INDEX)
    if CELL == None:
        if ITEM == None:
            CELL_WR(TABLE, ROW, COLUMN_INDEX, "")
        ITEM = TABLE.item(ROW, COLUMN_INDEX)
        if COLOR == "GREEN":
            color = QColor(0, 255, 0)
        elif COLOR == "YELLOW":
            color = QColor(255, 255, 0)
        elif COLOR == "RED":
            color = QColor(255, 0, 0)
        else:
            print(f"CELL_COLOR ERROR / WRONG VALUE COLOR [{COLUMN_INDEX}]")
            return
        ITEM.setBackground(color)
        
def TBL_INIT(TABLE: QTableWidget):
    '''
    Reset the Table, set 0 rowCount
    '''
    TABLE.setEnabled(False)
    TABLE.setRowCount(0)
    TABLE.setColumnCount(0)
    TABLE.setEnabled(True)

def TBL_POP_PANDAS_DF(TABLE: QTableWidget, DATAFRAME: pd.DataFrame, HIDE_COLUMNS: list=[], PROTECTED_COLUMNS: list=[], HEAD_ORDER:bool=True) -> None:
    '''
    Populate QTable with a Pandas DataFrame \n

    `VARIABLES:`
    - HIDE_COLUMNS (list): Hide the list of columns by int (column index) or str (calumn name)
    - PROTECTED_COLUMNS (list): Config the list of columns selected by int (column index) or str (calumn name)
    - HEAD OPRDER (bool): Turn on the "Sort fields by ascending order" function
    
    `DEBUG:` 
        - Al ordenar los datos, hay que releer la tabla, en el caso de que tenga alguna edición, se pierde
        - Problemas con los NaN
        - Some times show: QAbstractItemView::closeEditor called with an editor that does not belong to this view
    '''
    ## INIT TBL
    TABLE.setEnabled(False)
    TABLE.setRowCount(0)
    TABLE.setColumnCount(0)
    ## 
    TABLE.setColumnCount(len(DATAFRAME.columns))
    TABLE.setHorizontalHeaderLabels(DATAFRAME.columns)
    TABLE.setRowCount(len(DATAFRAME.index))

    ## POPULATE TABLE FUNCTION
    def pop_tbl(dtframe):
        TABLE.setEnabled(False)
        row = 0
        for record in list(dtframe.iloc):
            ## WRITE CELL
            for col in list(dtframe.columns):
                col_indx = list(dtframe.columns).index(col)
                CELL_WR(TABLE, row, col_indx, record[col])
            ## PROTECTED COLUMNS
            for prot in PROTECTED_COLUMNS: 
                CELL_READONLY(TABLE, row, prot)
            row += 1
        # TABLE.resizeColumnsToContents()
        TABLE.setEnabled(True)
    
    ## ORDER FUNCTIONS & CONNECTIONS
    # def ext_func(head_index): # Probando para usar funciones externas
    #     # INDEX = head_index
    #     # TBL_ORDER(TABLE, INDEX) # Funcion externa
    #     pass
    def order_tbl(head_index): # logicalIndex es la herencia que pasa la señal
        ## GET DATA
        column = DATAFRAME.columns[head_index]
        dfsorted = DATAFRAME.sort_values(by=column, ascending=True)
        ## POP ROWS
        TABLE.setEnabled(False)
        pop_tbl(dfsorted)
    ## 
    if HEAD_ORDER == True:
        try: TABLE.horizontalHeader().sectionClicked.disconnect()
        except: pass
        TABLE.horizontalHeader().sectionClicked.connect(order_tbl)
        # TABLE.horizontalHeader().sectionClicked.connect(ext_func)
    else:
        try: TABLE.horizontalHeader().sectionClicked.disconnect()
        except: pass
    
    ## HIDE COLUMS
    for col in HIDE_COLUMNS:
        if type(col) == int:
            TABLE.setColumnHidden(col, True)
        elif type(col) == str:
            col_indx = list(DATAFRAME.columns).index(col)
            TABLE.setColumnHidden(col_indx, True)
    
    ## POP ROWS
    pop_tbl(DATAFRAME)
    TABLE.resizeColumnsToContents()

def TBL_GET_HEADERS(TABLE: QTableWidget) -> list:
    '''
    Get a list of headers in the selected Qtable
    '''
    HEADERS = []
    for head in range(TABLE.columnCount()):
        header_text = TABLE.horizontalHeaderItem(head).text()
        if header_text == "" or header_text == None: 
            header_text = str(head)
        HEADERS.append(header_text)
    return HEADERS

def TBL_GET_HEADER_INDEX(TABLE: QTableWidget, COLUMN: int | str) -> int:
    '''
    Get the index value of selected Header

    ** If the header name is not correct return None value, check after function the result in case of error
    '''
    colIndex = COLUMN
    if type(colIndex) == str:
        HEADERS = TBL_GET_HEADERS(TABLE)
        if COLUMN in HEADERS: 
            colIndex = HEADERS.index(COLUMN)
        else:
            print(f"CELL_RD ERROR / WRONG HEADER NAME [{COLUMN}]")
            return None
    return colIndex

def TBL_GET_PANDAS_DF(TABLE: QTableWidget):
    '''
    Create Pandas DataFrame from QTable data \n
    
    `DEBUG:`
        - The name of columns should not be "" or None
    '''
    HEADERS = TBL_GET_HEADERS(TABLE)
    DATAFRAME = {}
    for field in HEADERS: DATAFRAME[field] = []
    for row in range(TABLE.rowCount()):
        for head in HEADERS:
            indx = HEADERS.index(head)
            VALUE = CELL_RD(TABLE, row, indx)
            DATAFRAME[head].append(VALUE)
    DATAFRAME = pd.DataFrame(DATAFRAME)
    return DATAFRAME

def TBL_VHEADER_WIDTH_FIX(TABLE: QTableWidget, COLUMNS: list | tuple = []):
    '''
    Set the selected list as fixed column width \n
    `COLUMNS:` You can specify the column as an int (index) or str (header)
    '''
    for col in COLUMNS:
        COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, col)
        TABLE.horizontalHeader().setSectionResizeMode(COLUMN_INDEX, QHeaderView.ResizeMode.Fixed)


''' INFOBOXES
--------------------------------------------------------
'''

def INFOBOX(TITLE: str = "", TEXT: str = ""):
    '''
    Information Window
    '''
    infobox = QMessageBox()
    # infobox.setWindowIcon()
    infobox.setFont(QFont('Consolas', 10))
    infobox.information(QMainWindow(), str(TITLE), str(TEXT))

def YESNOBOX(TITLE: str = "", TEXT: str = "") -> bool:
    '''
    Question Window with YES/NO Options
    '''
    yesnobox = QMessageBox()
    yesnobox.setFont(QFont('Consolas', 10))
    reply = yesnobox.question(QMainWindow(), str(TITLE), str(TEXT))
    if reply == QMessageBox.StandardButton.Yes:
        return True
    if reply == QMessageBox.StandardButton.No:
        return False

def INPUTBOX(TITLE: str = "", TEXT: str = "", *DEFAULT):
    '''
    INCOMPLETE
    '''
    default = ""
    if DEFAULT:
        default = DEFAULT[0]
    inputbox = QInputDialog()
    text, okPressed = inputbox.getText(QMainWindow(), str(TITLE), str(TEXT), QLineEdit.Normal, default)
    return text, okPressed


''' PyQt FORMS
-------------------------------------------------------- '''

FONT_LABEL = QFont("Roboto Black", pointSize=6, weight=8)
FONT_WIDGET = QFont("Consolas", pointSize=12)
FONT_TABLE = QFont("Consolas", pointSize=10)

from pydeveloptools.forms import PYQT_QLIST_FORM_ui

class QLIST(QDialog, PYQT_QLIST_FORM_ui.Ui_Dialog):
    '''
    '''
    def __init__(self, LIST: list | tuple = [], parent=None, ):
        QDialog.__init__(self, parent)
        
        ''' INIT '''
        self.setupUi(self)
        for item in LIST:
            self.lst_items.addItem(item)
        self.value = [self.lst_items.item(x).text() for x in range(self.lst_items.count())]
        
        ''' CONNECTIONS '''
        self.btn_add.clicked.connect(self.ITEM_ADD)
        self.btn_del.clicked.connect(self.ITEM_DEL)
        self.btn_up.clicked.connect(self.ITEM_UP)
        self.btn_down.clicked.connect(self.ITEM_DOWN)
        
    def ITEM_ADD(self):
        ITEM = self.tx_newitem.text()
        # print("ITEM_ADD", ITEM)
        if ITEM and ITEM != "":
            self.lst_items.addItem(ITEM)
            self.value = [self.lst_items.item(x).text() for x in range(self.lst_items.count())]
            self.tx_newitem.clear()
    
    def ITEM_DEL(self):
        print('currentRow', self.lst_items.currentRow())
        # , self.lst_items.currentItem().text())
        self.value = [self.lst_items.item(x).text() for x in range(self.lst_items.count())]
    
    def ITEM_UP(self):
        print('ITEM_UP')

    def ITEM_DOWN(self):
        print('ITEM_DOWN')
        

class QLIST_FORM(QDialog):
    '''
    List Selection Form
    '''
    def __init__(self, LIST: list | tuple, Window_Title="List", fontFamily="Arial Rounded MT Bold"):
        QDialog.__init__(self)

        ''' INIT '''
        self.LIST = LIST
        self.Window_Title = Window_Title
        self.fontFamily = fontFamily
        self.value: str = None
        self.SETUP_UI()
        self.LIST_LOAD()

        ''' CONNECTIONS '''
        self.lst.doubleClicked.connect(self.DATA_SELECT)
    
    def SETUP_UI(self):
        font = QtGui.QFont()
        font.setFamily(self.fontFamily)
        font.setPointSize(10)
        # 
        self.setObjectName("LIST")
        self.resize(400, 250)
        self.setFont(font)
        self.setToolTip("")
        self.setStatusTip("")
        self.setWhatsThis("")
        self.setAccessibleName("")
        self.setAccessibleDescription("")
        self.setWindowFilePath("")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.lst = QtWidgets.QListWidget(self)
        self.lst.setFont(font)
        self.lst.setToolTip("")
        self.lst.setStatusTip("")
        self.lst.setWhatsThis("")
        self.lst.setAccessibleName("")
        self.lst.setAccessibleDescription("")
        self.lst.setObjectName("lst")
        self.gridLayout.addWidget(self.lst, 0, 0, 1, 1)
        ##
        self.setWindowTitle(self.Window_Title)
    
    def LIST_LOAD(self):
        for e in self.LIST: # self.lst.addItems(self.LIST)
            self.lst.addItem(str(e))
    
    def DATA_SELECT(self):
        item = self.lst.currentItem().text()
        self.value = item
        self.close()

class QTABLE_FORM(QtWidgets.QDialog):
    '''
    Table Form (1 Field: 1 Value)
    CONFIG: list [class configValue]
    '''
    @dataclass
    class configValue():
        '''
        Value object for use in data configuration
        '''
        fieldName: str = ""
        value: str | int | float | bool = ""
        mandatory: bool = False
        info: str = ""

    def __init__(self, CONFIG: list | tuple, Window_Title: str="Table Form", fontFamily: str="Arial Rounded MT Bold", comboBoxEditables: bool=False) -> None:
        QtWidgets.QDialog.__init__(self)
        # 
        self.data: dict = None
        self.CONFIG = CONFIG
        # if self.CONFIG.get('FIRM'): self.CONFIG.pop('FIRM')
        self.Window_Title = Window_Title
        self.fontFamily = fontFamily
        self.comboBoxEditable = comboBoxEditables
        
        ''' INIT '''
        self.setupUi(self)
        self.setWindowTitle(self.Window_Title)
        H_HEADERS = ["DATA", "", "INFO"]
        self.tbl_form.verticalHeader().setVisible(True)
        self.tbl_form.setColumnCount(3)
        self.tbl_form.setHorizontalHeaderLabels(H_HEADERS)
        self.CONNECTIONS()
        self.SETUP_DATA()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 300)
        Dialog.setMinimumSize(QtCore.QSize(450, 300))
        font = QtGui.QFont()
        font.setFamily(self.fontFamily)
        Dialog.setFont(font)
        Dialog.setToolTip("")
        Dialog.setStatusTip("")
        Dialog.setWhatsThis("")
        Dialog.setAccessibleName("")
        Dialog.setAccessibleDescription("")
        Dialog.setWindowFilePath("")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tbl_form = QtWidgets.QTableWidget(Dialog)
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
        self.btn_intro = QtWidgets.QPushButton(Dialog)
        self.btn_intro.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_intro.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily(self.fontFamily)
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
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def CONNECTIONS(self):
        self.btn_intro.clicked.connect(self.DATA_INTRO)

    # class configValue():
    #     r'''
    #     Value object for use in data configuration
    #         >> fieldName: str
    #         >> value: bool / str / list / tuple / int / float
    #         >> mandatory: bool
    #         >> info: str
    #     '''
    #     def __init__(self, 
    #             fieldName: str = "", 
    #             value = "", 
    #             mandatory: bool = False, 
    #             info: str = "") -> None:
    #         self.fieldName = fieldName
    #         self.value = value
    #         self.mandatory = mandatory
    #         self.info = info

    def SETUP_DATA(self):
        TABLE = self.tbl_form
        ## SET CONFIG
        TABLE.setRowCount(len(self.CONFIG))
        row = 0
        self.HEADERS = []
        for field in self.CONFIG:
            row = self.CONFIG.index(field)
            ## NAME
            self.HEADERS.append(field.fieldName)
            ## VALUE
            TYPE = type(field.value)
            if TYPE == bool: CELL_CHECKBOX(TABLE, row, 0, field.value)
            if TYPE == str: CELL_WR(TABLE, row, 0, field.value)
            if TYPE == list: CELL_COMBOBOX(TABLE, row, 0, field.value, self.comboBoxEditable)
            if TYPE == tuple: CELL_COMBOBOX(TABLE, row, 0, field.value, self.comboBoxEditable)
            if TYPE == int: CELL_SPINBOX(TABLE, row, 0, field.value)
            if TYPE == float: CELL_WR(TABLE, row, 0, field.value)
            ## MANDATORY
            if field.mandatory: CELL_WR(TABLE, row, 1, "*")
            CELL_READONLY(TABLE, row, 1)
            ## INFO
            CELL_WR(TABLE, row, 2, field.info)
            CELL_READONLY(TABLE, row, 2)
        ## SET TABLE
        TABLE.setVerticalHeaderLabels(self.HEADERS)
        TABLE.resizeColumnsToContents()
        TABLE.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Fixed)
        TABLE.setColumnWidth(0, 230)

    def DATA_INTRO(self):
        TABLE = self.tbl_form
        self.data = {}
        summary = ""
        for field in self.HEADERS:
            row = self.HEADERS.index(field)
            value = CELL_RD(TABLE, row, 0)
            summary += f"{field}: "
            if value == "" or value == None:
                if CELL_RD(TABLE, row, 1) == "*": 
                    self.data = None
                    INFOBOX("ATTENTION", "PLEASE, FILL ALL THE MANDATORY (*) FIELDS")
                    return
                self.data[field] = None
            else:
                self.data[field] = value
                summary += f"{value}"
            summary += "\n"
        if YESNOBOX("DO YOU WANT SAVE THIS DATA?", summary) == True:
            self.close()
        else:
            self.data = None
            return

class QDICT_FORM(QtWidgets.QDialog):
    '''
    Table Form (1 Field: Value1, Value2...)

    CONFIG (dict) = { "<Field1_Name>": Field1_Value (None/str/int/float/list), "<Field2_Name>": ... } \n
    DATA (dict/datFrame) = { 
        "<Field1_Name>" (dict): {"0": Field1_Value0, "1": Field1_Value1, ...}
        "<Field2_Name>" (dict): ...
        }  \n 

    INCOMPLETE / DEBUG:
        - Valores repetidos
        - Hay que crear un class para definir bien el CONFIG como en QTABLE_FORM
        - Quitar la función dataframe_to_txt
    '''
    data = None
    def __init__(self, CONFIG: dict, DATA={}, Window_Title="Table Form", fontFamily="Arial Rounded MT Bold"):
        QtWidgets.QDialog.__init__(self)

        ''' INIT '''
        self.Window_Title = Window_Title
        self.fontFamily = fontFamily
        self.CONFIG = CONFIG
        self.DATA = DATA

        ''' INIT '''
        self.SETUP_UI()
        self.CREATE_CONNECTIONS()
        self.SETUP_DATA()
        
    def SETUP_UI(self):
        self.setObjectName("Dialog")
        self.resize(500, 400)
        self.setMinimumSize(QtCore.QSize(350, 350))
        font = QtGui.QFont()
        font.setFamily(self.fontFamily)
        self.setFont(font)
        self.setWindowTitle(self.Window_Title)
        self.setToolTip("")
        self.setStatusTip("")
        self.setWhatsThis("")
        self.setAccessibleName("")
        self.setAccessibleDescription("")
        # self.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedKingdom))
        self.setWindowFilePath("")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_row_add = QtWidgets.QPushButton(self)
        self.btn_row_add.setEnabled(True)
        self.btn_row_add.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_row_add.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily(self.fontFamily)
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_row_add.setFont(font)
        self.btn_row_add.setToolTip("")
        self.btn_row_add.setStatusTip("")
        self.btn_row_add.setWhatsThis("")
        self.btn_row_add.setAccessibleName("")
        self.btn_row_add.setAccessibleDescription("")
        self.btn_row_add.setText("ADD ROW")
        self.btn_row_add.setShortcut("")
        self.btn_row_add.setObjectName("btn_row_add")
        self.gridLayout.addWidget(self.btn_row_add, 0, 0, 1, 1)
        self.btn_row_del = QtWidgets.QPushButton(self)
        self.btn_row_del.setEnabled(True)
        self.btn_row_del.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_row_del.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily(self.fontFamily)
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_row_del.setFont(font)
        self.btn_row_del.setToolTip("")
        self.btn_row_del.setStatusTip("")
        self.btn_row_del.setWhatsThis("")
        self.btn_row_del.setAccessibleName("")
        self.btn_row_del.setAccessibleDescription("")
        self.btn_row_del.setText("DEL ROW")
        self.btn_row_del.setShortcut("")
        self.btn_row_del.setObjectName("btn_row_del")
        self.gridLayout.addWidget(self.btn_row_del, 0, 1, 1, 1)
        self.tbl_main = QtWidgets.QTableWidget(self)
        self.tbl_main.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(self.fontFamily)
        font.setPointSize(10)
        self.tbl_main.setFont(font)
        self.tbl_main.setToolTip("")
        self.tbl_main.setStatusTip("")
        self.tbl_main.setWhatsThis("")
        self.tbl_main.setAccessibleName("")
        self.tbl_main.setAccessibleDescription("")
        self.tbl_main.setStyleSheet("background-color: rgb(228, 228, 228);")
        self.tbl_main.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tbl_main.setDragEnabled(False)
        self.tbl_main.setDragDropOverwriteMode(False)
        self.tbl_main.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.NoDragDrop)
        self.tbl_main.setAlternatingRowColors(True)
        self.tbl_main.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_main.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems)
        self.tbl_main.setObjectName("tbl_main")
        self.tbl_main.setColumnCount(0)
        self.tbl_main.setRowCount(0)
        self.tbl_main.horizontalHeader().setDefaultSectionSize(160)
        self.tbl_main.horizontalHeader().setMinimumSectionSize(25)
        self.tbl_main.verticalHeader().setVisible(False)
        self.tbl_main.verticalHeader().setDefaultSectionSize(35)
        self.tbl_main.verticalHeader().setMinimumSectionSize(35)
        self.gridLayout.addWidget(self.tbl_main, 1, 0, 1, 2)
        self.btn_save = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setToolTip("")
        self.btn_save.setStatusTip("")
        self.btn_save.setWhatsThis("")
        self.btn_save.setAccessibleName("")
        self.btn_save.setAccessibleDescription("")
        # self.btn_save.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedKingdom))
        self.btn_save.setText("SAVE DATA")
        self.btn_save.setShortcut("")
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 2, 0, 1, 2)
        ''' WIDGETS '''
        # self.HEADERS = list(self.FIELDS.keys())
        # self.tbl_main.setColumnCount(len(self.HEADERS))
        # self.tbl_main.setHorizontalHeaderLabels(self.HEADERS)
        pass

    def CREATE_CONNECTIONS(self):
        self.btn_row_add.clicked.connect(self.ROW_ADD)
        self.btn_row_del.clicked.connect(self.ROW_DEL)
        self.btn_save.clicked.connect(self.DATA_INTRO)

    def SETUP_DATA(self):
        TABLE = self.tbl_main
        self.HEADERS = []
        for field in self.CONFIG.keys(): self.HEADERS.append(field)
        self.HEADERS.append("INFO")
        TABLE.setColumnCount(len(self.HEADERS))
        TABLE.setHorizontalHeaderLabels(self.HEADERS)
        df = pd.DataFrame(self.DATA)
        for row in df.index:
            self.ROW_ADD()
            for field in self.HEADERS:
                col = self.HEADERS.index(field)
                value = df.loc[row][field]
                CELL = TABLE.cellWidget(int(row), col)
                if CELL == None:
                    CELL_WR(TABLE, int(row), col, value)
                else:
                    WIDGET_WR(CELL, value)

    def ROW_ADD(self):
        TABLE = self.tbl_main
        row = TABLE.rowCount()
        TABLE.insertRow(row)
        col = 0
        for field in self.CONFIG:
            value = self.CONFIG[field]
            typ = type(value)
            if typ == list: CELL_COMBOBOX(TABLE, row, col, value)
            if typ == str: CELL_WR(TABLE, row, col, value)
            if typ == int: CELL_SPINBOX(TABLE, row, col, value)
            if typ == float: CELL_WR(TABLE, row, col, value)
            if typ == bool: CELL_CHECKBOX(TABLE, row, col, value)
            col += 1

    def ROW_DEL(self):
        TABLE = self.tbl_main
        row = TABLE.currentRow()
        if row < 0:
            INFOBOX("ATTENTION", "SELECT A VALID ROW")
        else:
            TABLE.removeRow(row)
        pass

    def dataframe_to_txt(self, DATAFRAME=pd.DataFrame) -> str:
        '''
        '''
        columns = {}
        for col in DATAFRAME.columns:
            columns[col] = 0
            for row in DATAFRAME.index:
                value = len(str(DATAFRAME.loc[row][col]))
                if columns[col] < value: columns[col] = value
        ## Texto
        tx = ""
        for row in DATAFRAME.index:
            lst = []
            for col in DATAFRAME.columns:
                value = DATAFRAME.loc[row][col]
                largo = columns[col]+1
                texto = f'{value: <{largo}}'
                texto = str(value)
                lst.append(texto)
            tx += ", ".join(lst) # chr(9) + "| "
            tx += chr(10) # "\n"
        return tx

    def DATA_INTRO(self):
        TABLE = self.tbl_main
        self.data = {}
        summary = ""
        for field in self.HEADERS: self.data[field] = []
        for row in range(TABLE.rowCount()):
            for field in self.HEADERS: 
                col = self.HEADERS.index(field)
                value = CELL_RD(TABLE, row, col)
                self.data[field].append(value)
        df = pd.DataFrame(self.data)
        self.data = df.to_json()
        # summary = df.to_string()
        summary = self.dataframe_to_txt(df)
        if YESNOBOX("DO YOU WANT SAVE THIS DATA?", summary) == True:
            self.close()
        else:
            self.data = None
            return

class QTEXT_FORM(QtWidgets.QDialog):
    '''
    Plain Text Form

    INCOMPLETE / DEBUG:
        - Hay que crear un class para definir bien el CONFIG como en QTABLE_FORM
    '''
    data = None
    def __init__(self, TEXT: str = "", Window_Title="Plain Text Form", fontFamily="Consolas"):
        QtWidgets.QDialog.__init__(self)
        self.Window_Title = Window_Title
        self.fontFamily = fontFamily
        self.TEXT = TEXT

        ''' INIT '''
        self.setupUi()
        self.tx_dialog.setText(self.TEXT)
        self.btn_exit.clicked.connect(self.exitdialog)

    def setupUi(self):
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily(self.fontFamily)
        self.setFont(font)
        self.setObjectName("Dialog")
        self.resize(600, 160)
        self.setWindowTitle(self.Window_Title)
        self.setToolTip("")
        self.setStatusTip("")
        self.setWhatsThis("")
        self.setAccessibleName("")
        self.setAccessibleDescription("")
        self.setWindowFilePath("")
        # 
        self.tx_dialog = QtWidgets.QTextEdit(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily(self.fontFamily)
        self.tx_dialog.setFont(font)
        self.tx_dialog.setToolTip("")
        self.tx_dialog.setStatusTip("")
        self.tx_dialog.setWhatsThis("")
        self.tx_dialog.setAccessibleName("")
        self.tx_dialog.setAccessibleDescription("")
        # self.tx_dialog.setStyleSheet("background-color: rgb(228, 228, 228);")
        self.tx_dialog.setDocumentTitle("")
        self.tx_dialog.setAcceptRichText(False)
        self.tx_dialog.setPlaceholderText("")
        self.tx_dialog.setObjectName("tx_dialog")
        # 
        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_exit.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily(self.fontFamily)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setToolTip("")
        self.btn_exit.setStatusTip("")
        self.btn_exit.setWhatsThis("")
        self.btn_exit.setAccessibleName("")
        self.btn_exit.setAccessibleDescription("")
        self.btn_exit.setText("SAVE")
        self.btn_exit.setShortcut("")
        self.btn_exit.setObjectName("btn_exit")
        # 
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.tx_dialog)
        self.verticalLayout.addWidget(self.btn_exit)
        QtCore.QMetaObject.connectSlotsByName(self)

    def exitdialog(self):
        self.data = self.tx_dialog.toPlainText()
        if YESNOBOX("DO YOU WANT SAVE THIS DATA?", self.data) == True:
            self.close()
        else:
            self.data = None
            return

class LICENSE(QtWidgets.QMainWindow):
    '''
    INCOMPLETE:
        Añadir info y datos
        Editar logo
    '''

    def __init__(self, TEXT: str="", windowTitle: str="INFO") -> None:
        super(LICENSE, self).__init__()
        self.setupUi(self)
        self.btn_run.clicked.connect(self.close)
        # 
        self.setWindowTitle(windowTitle)
        LICENSE_TEXT = (
            "ESTE SOFTWARE ES UNA VERSION EN FASE DE PRUEBA.",
            "ES NECESARIO ACTUALIZARLO EVITANDO LA DISTRIBUCIÓN DE VERSIONES INCOMPLETAS.",
            "POR FAVOR, CONTACTA CON:",
            "PABLO GONZÁLEZ PILA / pablogonzalezpila@gmail.COM",
            )
        for line in LICENSE_TEXT: self.tx_info.appendPlainText(line)
        self.tx_info.appendPlainText("\n")
        self.tx_info.appendPlainText(TEXT)
        self.tx_info.appendPlainText("\n")
    
    def setupUi(self, MainWindow):
        ## UI File
        # uiFile = r'PYQT_QLICENSE_new.ui'
        # self.ui = uic.loadUi(os.path.join(uiPath, uiFile), self) # Load the .ui file
        
        ## PY File
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 200)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        MainWindow.setFont(font)
        # MainWindow.setWindowTitle("INFO")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("../NMB_v3.0/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        # MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        MainWindow.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setToolTip("")
        self.centralwidget.setStatusTip("")
        self.centralwidget.setWhatsThis("")
        self.centralwidget.setAccessibleName("")
        self.centralwidget.setAccessibleDescription("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.tx_info = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tx_info.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.tx_info.setFont(font)
        self.tx_info.setToolTip("")
        self.tx_info.setStatusTip("")
        self.tx_info.setWhatsThis("")
        self.tx_info.setAccessibleName("")
        self.tx_info.setAccessibleDescription("")
        self.tx_info.setDocumentTitle("")
        self.tx_info.setReadOnly(True)
        # self.tx_info.setPlainText("")
        self.tx_info.setPlaceholderText("")
        self.tx_info.setObjectName("tx_info")
        self.gridLayout.addWidget(self.tx_info, 0, 0, 1, 1)
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_run.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        # font.setFamily("Consolas")
        font.setFamily("Roboto Black")
        font.setPointSize(15)
        self.btn_run.setFont(font)
        self.btn_run.setToolTip("")
        self.btn_run.setStatusTip("")
        self.btn_run.setWhatsThis("")
        self.btn_run.setAccessibleName("")
        self.btn_run.setAccessibleDescription("")
        # self.btn_run.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_run.setObjectName("btn_run")
        self.btn_run.setText("OK")
        self.gridLayout.addWidget(self.btn_run, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


''' TEST
--------------------------------------------------------
'''

# QT.INFOBOX("ATTENTIONS", "OPTION NOT IMPLEMENTED YET")