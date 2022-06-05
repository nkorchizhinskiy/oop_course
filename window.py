from PyQt5.QtWidgets import QMainWindow, \
                            QMenuBar, \
                            QMenu, \
                            QAction, \
                            QTableWidget, QTableWidgetItem
                            
from SETTINGS import *
import database_output
from json.decoder import JSONDecodeError
from typing import Literal

# Dialog windows.
from dialogs import add_department, \
                    add_product, \
                    delete_product, \
                    add_product_in_department, \
                    delete_product_in_department 




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
        self.actions_with_table = QMenu("Действия в таблице", self)

        self.table_department = QAction("Отдел", self)
        self.table_products = QAction("Продукты", self)
        self.table_product_in_department = QAction("Продукты в отделе", self)

        self.open_table.addActions([
            self.table_department,
            self.table_products,
            self.table_product_in_department,
            ])

        self.add_department = QAction("Добавить отдел", self)
        self.add_product = QAction("Добавить новый товар в реестр", self)
        self.delete_product = QAction("Удалить товар из реестра", self)
        self.add_product_in_department = QAction("Добавить новый товар в отдел", self)
        self.delete_product_in_department = QAction("Удалить товар из отдела", self)

        self.actions_with_table.addActions([
            self.add_department,
            self.add_product,
            self.delete_product,
            self.add_product_in_department,
            self.delete_product_in_department,
            ])

        self.menu_bar.addMenu(self.open_table)
        self.menu_bar.addMenu(self.actions_with_table)
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

        # Table actions.
        self.add_department.triggered.connect(self.on_clicked_add_department)
        self.add_product.triggered.connect(self.on_clicked_add_product)
        self.delete_product.triggered.connect(self.on_clicked_delete_product)
        self.add_product_in_department.triggered.connect(self.on_clicked_add_product_in_department)
        self.delete_product_in_department.triggered.connect(self.on_clicked_delete_product_in_department)

    
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
        
    
    def on_clicked_add_department(self) -> None:
        """Function which add department on signal from menubar"""
        self.add_department_dialog = add_department.AddDepartment(self.menu_bar)


    def on_clicked_add_product(self) -> None:
        """Function which add product on signal from menubar"""
        self.add_products = add_product.AddProduct(self.menu_bar)


    def on_clicked_delete_product(self) -> None:
        """Function which delete product on signal from menubar"""
        self.delete_product = delete_product.DeleteProduct(self.menu_bar)


    def on_clicked_add_product_in_department(self) -> None:
        """Function which add product in department on signal from menubar"""
        self.add_product_in_department = add_product_in_department.AddProductInDepartment(self.menu_bar)


    def on_clicked_delete_product_in_department(self) -> None:
        """Function which delete product in department on signal from menubar"""
        self.delete_product_in_department = delete_product_in_department.DeleteProductInDepartment(self.menu_bar)
