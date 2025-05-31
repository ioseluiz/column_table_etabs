from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout,QTableWidget, QTableWidgetItem,
    QScrollArea, QFrame,QLabel
)
from PyQt5.QtCore import pyqtSignal

class InfoGridLinesScreen(QWidget):
    datos_para_renombrar = pyqtSignal(dict)
    def __init__(self, gridlines ,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Gridlines Data")
        self.resize(500, 350)
        
        
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(10,10,10,10)
        self.main_layout.setSpacing(10)
        
        self.title_label = QLabel("Stories Info")
        self.main_layout.addWidget(self.title_label)
        
        self.table_gridlines_info = QTableWidget(len(gridlines),4) # Modify with len of stories list
        self.table_gridlines_info.setHorizontalHeaderLabels(["GridLine", "Pos X", "Pos Y", "New GridLine Name"])
        
        # Configure QTable
        
        for gridline_idx, gridline in enumerate(gridlines):
            # Col 0: Gridline
            item_name = QTableWidgetItem(str(gridline['GridLine']))
            self.table_gridlines_info.setItem(gridline_idx, 0, item_name)
            
            # Col 1: Pos X
            item_pos_x = QTableWidgetItem(str(gridline['pos_x']))
            self.table_gridlines_info.setItem(gridline_idx, 1, item_pos_x)
            
            # Col 2: Pos Y
            item_pos_y = QTableWidgetItem(str(gridline['pos_y']))
            self.table_gridlines_info.setItem(gridline_idx, 2, item_pos_y)
            
        self.table_gridlines_info.resizeColumnsToContents()
        
        self.btn_modificar_gridlines = QPushButton("Modificar Gridlines")
        
        # Add to main layout
        self.main_layout.addWidget(self.table_gridlines_info)
        self.main_layout.addWidget(self.btn_modificar_gridlines)
        
        # Conectar el click del boton a la funcion que emite la senal
        self.btn_modificar_gridlines.clicked.connect(self._emitir_datos_mapeo)
        
    def _emitir_datos_mapeo(self):
        print('modificar nombres GriLines')
        mapa = {}
        for fila in range(self.table_gridlines_info.rowCount()):
            item_original = self.table_gridlines_info.item(fila, 0)
            item_nuevo = self.table_gridlines_info.item(fila,3)
            
            # Asegurarse de que ambas celdas tengan texto
            if item_original and item_original.text() and item_nuevo and item_nuevo.text():
                valor_original = item_original.text().strip()
                valor_nuevo = item_nuevo.text().strip()
                if valor_original:
                    mapa[valor_original] = valor_nuevo
            
        # Emitir la senal con el diccionario como payload
        self.datos_para_renombrar.emit(mapa)
            
        