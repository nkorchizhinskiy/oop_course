from PyQt5.QtWidgets import QMainWindow, \
                            QMenuBar, \
                            QMenu, \
                            QAction, \
                            QTableWidget, QTableWidgetItem
                            
from SETTINGS import *
import database_output
from json.decoder import JSONDecodeError
from typing import Literal




class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        self.current_window = "department"
        self.create_default_condition()


    def create_default_condition(self) -> None:
        """Create widgets and set defaul settings"""
        self.setWindowTitle(WINDOW_TITLE)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self._create_widgets()
        self._set_signals()


    def _create_widgets(self) -> None:
        """Create widgets and set menubar"""
        self._create_menubar()
        self._create_table()


    def _create_menubar(self) -> None:
        """Create menubar"""
        self.menu_bar = QMenuBar(self)
        self.open_table = QMenu("Открыть таблицу", self)

        self.table_department = QAction("Отдел", self)
        self.table_products = QAction("Продукты", self)
        self.table_product_in_department = QAction("Продукты в отделе", self)

        self.open_table.addActions([
            self.table_department,
            self.table_products,
            self.table_product_in_department,
            ])

        self.menu_bar.addMenu(self.open_table)
        self.setMenuBar(self.menu_bar)

    
    def _create_table(self) -> None:
        """Create table, which display information from database"""
        self.table = QTableWidget(self)
        self.table.setFixedSize(600, 500)
        self.table.setColumnCount(5)
        self.table.move(70, 50)
        self._set_table(self.current_window)
        # TODO Сделать метод upgrade
        
        
    def _set_signals(self) -> None:
        """Set signal to widgets"""
        self.table_department.triggered.connect(lambda: self._set_table("department"))
        self.table_products.triggered.connect(lambda: self._set_table("products"))
        self.table_product_in_department.triggered.connect(lambda: self._set_table("product_in_department"))

    
    def _set_table(self, db_id: str) -> None|Literal["Файл пустой"]:
        """Set table on main window"""
        try:
            db_out = database_output.output_database(db_id)
        except JSONDecodeError:
            return "Файл пустой"
       
        self.table.setRowCount(len(db_out))
        row = 0
        for key, value in db_out.items():
            self.table.setItem(row, 0, QTableWidgetItem(key))
            self.table.setItem(row, 1, QTableWidgetItem(value[0]))
            self.table.setItem(row, 2, QTableWidgetItem(value[1]))
            self.table.setItem(row, 3, QTableWidgetItem(value[2]))
            self.table.setItem(row, 4, QTableWidgetItem(value[3]))
            row += 1
        

