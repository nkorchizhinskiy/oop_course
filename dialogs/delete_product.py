from PyQt5.QtWidgets import QDialog, \
                            QLabel, \
                            QComboBox, \
                            QPushButton
from PyQt5.QtGui import QFont


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
        self.name_label = QLabel("Название продукта", self)
        self.name_combobox = QComboBox(self)

        # Moving.
        self.name_label.move(20, 20)
        self.name_combobox.move(230, 20)

        self.push_button = QPushButton("Продолжить", self)
        self.push_button.move(140, 220)

        # Font.
        self.name_label.setFont(QFont("Montserrat", 12))

    def closeEvent(self, event) -> None:
        """Actions which run when dialog window closed"""
        self.menu_bar.setDisabled(False)


