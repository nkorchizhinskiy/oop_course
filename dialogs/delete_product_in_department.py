from PyQt5.QtWidgets import QDialog, \
                            QComboBox, \
                            QLabel, \
                            QPushButton
                            
from PyQt5.QtGui import QFont
from database_actions import database_get_department, database_get_product_from_department, database_get_products



class DeleteProductInDepartment(QDialog):

    def __init__(self, menu_bar):
        super().__init__()
        self.menu_bar = menu_bar
        self.menu_bar.setDisabled(True)        
        self.setWindowTitle("Удалить продукт из отдела")
        self.setFixedSize(400, 300)

        self._create_widgets()
        self.add_info()
        self.set_signals()

        self.show()


    def _create_widgets(self) -> None:
        """Create widgets in dialog window"""
        self.department_name_label = QLabel("Название отдела", self)
        self.department_name_field = QComboBox(self)

        self.product_name_label = QLabel("Название продукта", self)
        self.product_name_field = QComboBox(self)

        self.push_button = QPushButton("Продолжить", self)
        self.push_button.move(140, 220)

        # Moving.
        self.department_name_label.move(20, 20)
        self.department_name_field.move(230, 20)

        self.product_name_label.move(20, 60)
        self.product_name_field.move(230, 60)

        # Font.
        self.department_name_label.setFont(QFont("Montserrat", 12))
        self.product_name_label.setFont(QFont("Montserrat", 12))

    
    def add_info(self) -> None:
        """Add info into combobox"""
        departments = database_get_department()
        self.department_name_field.addItems(departments)
        products = database_get_product_from_department(self.department_name_field.currentText())
        for index, product in enumerate(products[0]):
            self.product_name_field.addItem(product, [products[1][index], products[2][index]])
        self.product_info_label = QLabel(f"Артикул - {self.product_name_field.currentData()[0]}\n"+
                                         f"Дата поставки - {self.product_name_field.currentData()[1]}",
                                         self)
        self.product_info_label.move(20, 100)
        
    
    def set_signals(self) -> None:
        """Set signals to combobox"""
        self.department_name_field.currentTextChanged.connect(self.change_product_list)
        self.product_name_field.currentTextChanged.connect(self.change_product_list_2)


    def closeEvent(self, event) -> None:
        """Actions which run when dialog window closed"""
        self.menu_bar.setDisabled(False)

    
    def change_product_list(self) -> None:
        """Change combobox list with signal"""
        products = database_get_product_from_department(self.department_name_field.currentText())
        self.product_name_field.clear()
        for index, product in enumerate(products[0]):
            if products[1][index] is None:
                continue
            self.product_name_field.addItem(product, [products[1][index]])
        if self.product_name_field.currentData() != None:
            self.product_info_label.setText(f"Артикул - {self.product_name_field.currentData()[0]}\n" +
                                         f"Дата поставки - {self.product_name_field.currentData()[1]}")
    
    def change_product_list_2(self) -> None:
        """Change combobox list with signal"""
#        products = database_get_product_from_department(self.department_name_field.currentText())
#        self.product_name_field.clear()
#        for index, product in enumerate(products[0]):
#            if products[1][index] is None:
#                continue
#            self.product_name_field.addItem(product, [products[1][index]])
        if self.product_name_field.currentData() != None:
            self.product_info_label.setText(
                    f"Артикул - {self.product_name_field.currentData()[0]}\n" +
                    f"Дата поставки - {self.product_name_field.currentData()[1]}")
