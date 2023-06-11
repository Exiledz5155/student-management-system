from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, \
    QGridLayout, QLineEdit, QPushButton, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")



app = QApplication(sys.argv)
hold = MainWindow()
hold.show()
sys.exit(app.exec())