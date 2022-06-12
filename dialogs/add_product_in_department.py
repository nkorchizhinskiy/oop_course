from PyQt5.QtWidgets import QComboBox, QDateEdit, \
                            QDialog, \
                            QLabel, \
                            QPushButton, \
                            QSpinBox, \
                            QAbstractSpinBox
from PyQt5.QtGui import QFont

from database_actions import database_add_product_in_department, \
                             database_get_departments_and_products



class AddProductInDepartment(QDialog):

    def __init__(self, menu_bar):
        super().__init__()
        self.menu_bar = menu_bar
        self.menu_bar.setDisabled(True)        
        self.setWindowTitle("Добавить продукт в отдел")
        self.setFixedSize(400, 300)

        self._create_widgets()
        self.add_product()
        self.set_signals()

        self.show()


    def _create_widgets(self) -> None:
        """Create widgets in dialog window"""
        self.department_name_label = QLabel("Название отдела", self)
        self.department_name_field = QComboBox(self)

        self.product_name_label = QLabel("Название продукта", self)
        self.product_name_field = QComboBox(self)

        self.count_label = QLabel("Количество", self)
        self.count_field = QSpinBox(self)
        self.count_field.setMinimum(1)
        self.count_field.setMaximum(999999)
        self.count_field.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.receipt_date_label = QLabel("Дата поступления", self)
        self.receipt_date_field = QDateEdit(self)


        self.push_button = QPushButton("Продолжить", self)
        self.push_button.move(40, 220)
 
        # Moving.
        self.department_name_label.move(20, 20)
        self.department_name_field.move(230, 20)
        self.product_name_label.move(20, 60)
        self.product_name_field.move(230, 60)
        self.count_label.move(20, 100)
        self.count_field.move(230, 100)
        self.receipt_date_field.move(230, 140)
        self.receipt_date_label.move(20, 140)

        # Font.
        self.department_name_label.setFont(QFont("Montserrat", 12))
        self.product_name_label.setFont(QFont("Montserrat", 12))
        self.count_label.setFont(QFont("Montserrat", 12))
        self.receipt_date_label.setFont(QFont("Montserrat", 12))


    def add_product(self) -> None:
        """Ready values for add in department"""
        departments, products = database_get_departments_and_products()

        for product in products:
            self.product_name_field.addItem(product[0], [
                                                         product[1],
                                                         product[2],
                                                         product[3]
                                                         ])

        self.department_name_field.addItems(departments)

        self.product_info_label = QLabel(
                    f"Артикул - {self.product_name_field.currentData()[0]}\n" +
                    f"Цена оптовая - {self.product_name_field.currentData()[1]}\n" +  
                    f"Цена розничная - {self.product_name_field.currentData()[2]}",
                    self)

        self.product_info_label.move(160, 200)
        self.product_info_label.setFont(QFont("Montserrat", 12))
    

    def set_signals(self) -> None:
        """Set signal to widget"""
        self.product_name_field.currentTextChanged.connect(lambda:
                self.product_info_label.setText(
                    f"Артикул - {self.product_name_field.currentData()[0]}\n" +
                    f"Цена оптовая - {self.product_name_field.currentData()[1]}\n" +  
                    f"Цена розничная - {self.product_name_field.currentData()[2]}"
                    ))


    def closeEvent(self, event) -> None:
        """Actions which run when dialog window closed"""
        self.menu_bar.setDisabled(False)


