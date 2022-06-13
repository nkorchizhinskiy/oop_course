from PyQt5.QtWidgets import QMainWindow, \
                            QMenuBar, \
                            QMenu, \
                            QAction, QMessageBox, \
                            QTableWidget, QTableWidgetItem
                            
from SETTINGS import *
from json.decoder import JSONDecodeError
from typing import Literal

# Dialog windows.
from dialogs import add_department 
from dialogs import add_product
from dialogs import delete_product
from dialogs import add_product_in_department
from dialogs import delete_product_in_department

import database_actions



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
            db_out = database_actions.output_database(db_id)
        except JSONDecodeError:
            return "Файл пустой"
       
        self.table.setRowCount(len(db_out))
        self.table.verticalHeader().hide()
        row = 0
        if db_id != "product_in_department":
            for key, value in db_out.items():

                self.table.setItem(row, 0, QTableWidgetItem(key))
                self.table.setItem(row, 1, QTableWidgetItem(value[0]))
                self.table.setItem(row, 2, QTableWidgetItem(value[1]))
                self.table.setItem(row, 3, QTableWidgetItem(value[2]))
                self.table.setItem(row, 4, QTableWidgetItem(value[3]))
                row += 1


        match db_id:
            case "department":
                self.table.setHorizontalHeaderLabels([
                                                      "Индекс",
                                                      "Название",
                                                      "Заведующий",
                                                      "Время открытия", 
                                                      "Время закрытия",
                                                        ])
            case "products":
                self.table.setHorizontalHeaderLabels([
                                                      "Индекс",
                                                      "Название",
                                                      "Артикул", 
                                                      "Цена оптовая", 
                                                      "Цена розничная",
                                                        ])
            case "product_in_department":
                self.table.setHorizontalHeaderLabels([
                                                      "Индекс",
                                                      "Индекс отдела",
                                                      "Индекс товара", 
                                                      "Количество", 
                                                      "Дата поступления",
                                                        ])
                for key, value in db_out.items():
                    department = database_actions.output_database("department")
                    product = database_actions.output_database("products")

                    self.table.setItem(row, 0, QTableWidgetItem(key))
                    self.table.setItem(row, 1, QTableWidgetItem(f"{department[value[0]][0]} - ({value[0]})"))
                    self.table.setItem(row, 2, QTableWidgetItem(f"{product[value[1]][0]} - ({value[1]})"))
                    self.table.setItem(row, 3, QTableWidgetItem(value[2]))
                    self.table.setItem(row, 4, QTableWidgetItem(value[3]))
                    row += 1

        
    
    def on_clicked_add_department(self) -> None:
        """Function which add department on signal from menubar"""
        self.add_department_dialog = add_department.AddDepartment(self.menu_bar)
        self.add_department_dialog.push_button.clicked.connect(lambda: self.get_values("add department"))


    def on_clicked_add_product(self) -> None:
        """Function which add product on signal from menubar"""
        self.add_product_dialog = add_product.AddProduct(self.menu_bar)
        self.add_product_dialog.push_button.clicked.connect(lambda: self.get_values("add product"))


    def on_clicked_delete_product(self) -> None:
        """Function which delete product on signal from menubar"""
        try:
            self.delete_product_dialog = delete_product.DeleteProduct(self.menu_bar)
            self.delete_product_dialog.push_button.clicked.connect(lambda: self.get_values("delete product"))
        except TypeError:
            QMessageBox.warning(self, "Ошибка!", "У вас нет товаров.")
            self.menu_bar.setDisabled(False)


    def on_clicked_add_product_in_department(self) -> None:
        """Function which add product in department on signal from menubar"""
        self.add_product_in_department_dialog = add_product_in_department.AddProductInDepartment(self.menu_bar)
        self.add_product_in_department_dialog.push_button.clicked.connect(lambda: self.get_values("add product in department"))


    def on_clicked_delete_product_in_department(self) -> None:
        """Function which delete product in department on signal from menubar"""
        self.delete_product_in_department_dialog = delete_product_in_department.DeleteProductInDepartment(self.menu_bar)
        self.delete_product_in_department_dialog.push_button.clicked.connect(lambda: self.get_values("delete product in department"))


    def get_values(self, value: str) -> None:
        """Get value from dialog window"""
        match value: 
            case "add department":
                values = [
                            self.add_department_dialog.name_field.text(),
                            self.add_department_dialog.name_chief_field.text(),
                            self.add_department_dialog.time_start_field.text(),
                            self.add_department_dialog.time_end_field.text(),
                        ]
                result = database_actions.database_add_department(values) 
                self.add_department_dialog.close()
                if result == 1:
                    QMessageBox.warning(self, "Ошибка!", "Такой отдел уже есть.")

            case "add product":
                values = [
                            self.add_product_dialog.name_field.text(),
                            self.add_product_dialog.code_field.text(),
                            self.add_product_dialog.cost_whilesale_field.text(),
                            self.add_product_dialog.cost_retail_field.text(),
                        ]
                result = database_actions.database_add_product(values)
                self.add_product_dialog.close()
                if result == 1:
                    QMessageBox.warning(self, "Ошибка!", "Такой товар уже есть.")
            case "delete product":
                database_actions.delete_products_in_department_after_delete_product(
                        [
                            self.delete_product_dialog.name_combobox.currentText(),
                            self.delete_product_dialog.name_combobox.currentData()[0]
                            ])
                values = [
                            self.delete_product_dialog.name_combobox.currentText(),
                            self.delete_product_dialog.name_combobox.currentData()[0],
                            self.delete_product_dialog.name_combobox.currentData()[1],
                            self.delete_product_dialog.name_combobox.currentData()[2],
                        ]
                database_actions.database_delete_product(values)
                self.delete_product_dialog.close()
            case "add product in department":
                values = [
                            self.add_product_in_department_dialog.department_name_field.currentText(),
                            self.add_product_in_department_dialog.product_name_field.currentText(),
                            self.add_product_in_department_dialog.count_field.text(),
                            self.add_product_in_department_dialog.receipt_date_field.text(),
                            self.add_product_in_department_dialog.product_name_field.currentData()[0]
                        ]
                database_actions.database_add_product_in_department(values)
                self.add_product_in_department_dialog.close()
            case "delete product in department":
                values = [
                            self.delete_product_in_department_dialog.department_name_field.currentText(),
                            self.delete_product_in_department_dialog.product_name_field.currentText(),
                            self.delete_product_in_department_dialog.product_name_field.currentData()[0]

                        ]
                database_actions.database_delete_product_in_department(values)
                self.delete_product_in_department_dialog.close()
