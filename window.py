from PyQt5.QtWidgets import QMainWindow, \
                            QMenuBar, \
                            QMenu, \
                            QAction, \
                            QTableWidget
                            
from SETTINGS import *



class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        self.current_window = "Department"
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
        self.table.move(30, 50)

        match self.current_window:
            case "Department":
                pass
            case "Products":
                pass
            case "Products in department":
                pass
        
        
    def _set_signals(self) -> None:
        """Set signal to widgets"""
        self.table_department.triggered.connect(lambda: print('1'))
        self.table_products.triggered.connect(lambda: print('2'))
        self.table_product_in_department.triggered.connect(lambda: print('3'))

