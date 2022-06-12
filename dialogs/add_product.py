from PyQt5.QtWidgets import QAbstractSpinBox, QDialog, \
                            QLabel, \
                            QDoubleSpinBox, \
                            QSpinBox, \
                            QLineEdit, \
                            QPushButton, \
                            QMessageBox
from PyQt5.QtGui import QFont




class AddProduct(QDialog):

    def __init__(self, menu_bar) -> None:
        super().__init__()
        self.menu_bar = menu_bar
        self.menu_bar.setDisabled(True)        
        self.setWindowTitle("Добавить продукт")
        self.setFixedSize(400, 300)

        self._create_widgets()
        self._set_signals()

        self.show()

    def _create_widgets(self) -> None:
        """Create widgets in dialog window"""
        self.name_label = QLabel("Название товара", self)
        self.name_field = QLineEdit(self)

        self.code_label = QLabel("Артикул", self)
        self.code_field = QSpinBox(self)
        self.code_field.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.code_field.setMinimum(1)
        self.code_field.setMaximum(999999)

        self.cost_whilesale_label = QLabel("Цена оптовая", self)
        self.cost_whilesale_field = QDoubleSpinBox(self)
        self.cost_whilesale_field.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.cost_whilesale_field.setMinimum(1)
        self.cost_whilesale_field.setMaximum(999999)

        self.cost_retail_label = QLabel("Цена розничная", self)
        self.cost_retail_field = QDoubleSpinBox(self)
        self.cost_retail_field.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.cost_retail_field.setMinimum(1)
        self.cost_retail_field.setMaximum(999999)

        self.push_button = QPushButton("Продолжить", self)
        self.push_button.setDisabled(True)
        self.push_button.move(140, 220)

        # Moving.
        self.name_label.move(20, 20)
        self.name_field.move(230, 20)
        self.code_label.move(20, 60)
        self.code_field.move(230, 60)
        self.cost_whilesale_label.move(20, 110)
        self.cost_whilesale_field.move(230, 110)
        self.cost_retail_label.move(20, 160)
        self.cost_retail_field.move(230, 160)

        # Font.
        self.name_label.setFont(QFont("Montserrat", 12))
        self.code_label.setFont(QFont("Montserrat", 12))
        self.cost_whilesale_label.setFont(QFont("Montserrat", 12))
        self.cost_retail_label.setFont(QFont("Montserrat", 12))

    def closeEvent(self, event) -> None:
        """Actions which run when dialog window closed"""
        self.menu_bar.setDisabled(False)


    def _set_signals(self) -> None:
        """Set signal to widgets"""
        self.name_field.textEdited.connect(self.check_value)

    
    def check_value(self) -> None:
        """Check value in text edited"""
        for symbol in self.name_field.text():
            if symbol.isnumeric():
                QMessageBox.warning(self, "Ошибка!", "Вы вводите число.")
                self.name_field.setText("")
                self.push_button.setDisabled(True)
                return

        if self.name_field.text() not in (None, ''):
            self.push_button.setDisabled(False)
        else:
            self.push_button.setDisabled(True)
    
