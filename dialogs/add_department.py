from PyQt5.QtWidgets import QDialog, \
                            QLabel, \
                            QLineEdit, QMessageBox, \
                            QTimeEdit, \
                            QPushButton
from PyQt5.QtGui import QFont
                            



class AddDepartment(QDialog):

    def __init__(self, menu_bar):
        super().__init__()
        self.menu_bar = menu_bar
        self.menu_bar.setDisabled(True)        

        self.setWindowTitle("Добавить отдел")
        self.setFixedSize(400, 300)

        self._create_widgets()
        self._set_signals()

        self.show()
    
    def _create_widgets(self) -> None:
        """Create widgets in dialog window"""
        self.name_label = QLabel("Название отдела", self)
        self.name_field = QLineEdit(self)

        self.name_chief_label = QLabel("Заведующий", self)
        self.name_chief_field = QLineEdit(self)

        self.time_start_label = QLabel("Время начала работы", self)
        self.time_start_field = QTimeEdit(self)

        self.time_end_label = QLabel("Время окончания работы", self)
        self.time_end_field = QTimeEdit(self)

        self.push_button = QPushButton("Продолжить", self)
        self.push_button.setDisabled(True)
        self.push_button.move(140, 220)

        # Moving.
        self.name_label.move(20, 20)
        self.name_field.move(230, 20)
        self.name_chief_label.move(20, 60)
        self.name_chief_field.move(230, 60)
        self.time_start_label.move(20, 110)
        self.time_start_field.move(230, 110)
        self.time_end_label.move(20, 160)
        self.time_end_field.move(230, 160)

        # Font.
        self.name_label.setFont(QFont("Montserrat", 12))
        self.name_chief_label.setFont(QFont("Montserrat", 12))
        self.time_start_label.setFont(QFont("Montserrat", 12))
        self.time_end_label.setFont(QFont("Montserrat", 12))


    def closeEvent(self, event) -> None:
        """Actions which run when dialog window closed"""
        self.menu_bar.setDisabled(False)


    def _set_signals(self) -> None:
        """Set signal to widgets"""
        self.name_field.textEdited.connect(lambda: self.check_value("name"))
        self.name_chief_field.textEdited.connect(lambda: self.check_value("name_chief"))

    
    def check_value(self, value: str) -> None:
        """Check value in text edited"""
        match value:
            case "name":
                for symbol in self.name_field.text():
                    if symbol.isnumeric():
                        QMessageBox.warning(self, "Ошибка!", "Вы вводите число.")
                        self.name_field.setText("")
                        self.push_button.setDisabled(True)
                        return
            case "name_chief":
                for symbol in self.name_chief_field.text():
                    if symbol.isnumeric():
                        QMessageBox.warning(self, "Ошибка!", "Вы вводите число.")
                        self.name_chief_field.setText("")
                        self.push_button.setDisabled(True)
                        return
        if self.name_field.text() not in(None, '') and self.name_chief_field.text() not in (None, ''):
            self.push_button.setDisabled(False)
        else:
            self.push_button.setDisabled(True)



