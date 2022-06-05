from PyQt5.QtWidgets import QComboBox, \
                            QDialog, \
                            QLabel, \
                            QPushButton
from PyQt5.QtGui import QFont



class AddProductInDepartment(QDialog):

    def __init__(self, menu_bar):
        super().__init__()
        self.menu_bar = menu_bar
        self.menu_bar.setDisabled(True)        
        self.setWindowTitle("Добавить продукт в отдел")
        self.setFixedSize(400, 300)

        self._create_widgets()

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


    def closeEvent(self, event) -> None:
        """Actions which run when dialog window closed"""
        self.menu_bar.setDisabled(False)


