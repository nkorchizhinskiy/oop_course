from PyQt5.QtWidgets import QDialog, \
                            QLabel, \
                            QComboBox, \
                            QPushButton
from PyQt5.QtGui import QFont
from database_actions import database_get_products


class DeleteProduct(QDialog):

    def __init__(self, menu_bar):
        super().__init__()
        self.menu_bar = menu_bar
        self.menu_bar.setDisabled(True)        
        self.setWindowTitle("Удалить продукт")
        self.setFixedSize(400, 300)

        self._create_widgets()

        self.show()


    def _create_widgets(self) -> None:
        """Create widgets in dialog window"""
        # Labels.
        self.name_label = QLabel("Название продукта", self)
        self.name_combobox = QComboBox(self)

        # Moving.
        self.name_label.move(20, 20)
        self.name_combobox.move(20, 50)

        self.push_button = QPushButton("Продолжить", self)
        self.push_button.move(140, 220)

        # Font.
        self.name_label.setFont(QFont("Montserrat", 12))

        # Combobox.
        combobox_values = database_get_products()
        for products in combobox_values:
            self.name_combobox.addItem(products[0], [products[1], products[2], products[3]])

        self.name_info_label = QLabel(f"Aртикул - {self.name_combobox.currentData()[0]}\n" +
                                         f"Оптовая цена - {self.name_combobox.currentData()[1]}\n" +
                                         f"Розничная цена - {self.name_combobox.currentData()[2]}", 
                                      self)
        self.name_info_label.move(100, 100)
        self.name_info_label.setFont(QFont("Montserrat", 12))
        
        self._set_signals()

    def closeEvent(self, event) -> None:
        """Actions which run when dialog window closed"""
        self.menu_bar.setDisabled(False)

    
    def _set_signals(self) -> None:
        """Set signal to combobox/widgets"""
        self.name_combobox.currentIndexChanged.connect(self.change_text)

    def change_text(self) -> None:
        """Change text in label for signal"""
        self.name_info_label.setText(f"Aртикул - {self.name_combobox.currentData()[0]}\n" +
                                     f"Оптовая цена - {self.name_combobox.currentData()[1]}\n" +
                                     f"Розничная цена - {self.name_combobox.currentData()[2]}")

