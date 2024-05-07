import sys
from PyQt6.QtWidgets import QApplication, QWidget
from MainWindow import Ui_MainWindow


class Login(QWidget):
    def __init__(self):
        super().__init__()

        # use the Ui_login_form
        self.ui = Ui_MainWindow()       
        self.ui.setupUi(self)       
        
        # show the login window
        self.show()
    


app = QApplication(sys.argv)
login_window = Login()
sys.exit(app.exec())


