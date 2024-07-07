from PyQt5.QtWidgets import * 
from PyQt5.Qt import *
from PyQt5.Qsci import * 
from PyQt5.QtGui import *

from pathlib import Path
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.init_ui()

        self.current_file = None
    
    def init_ui(self):
        # Body 
        self.setWindowTitle("Nebula Editor")
        self.resize(1300, 900)

        self.setStyleSheet(open("./src/css/style.qss", "r").read())

        # alternative Consolas font
        self.window_font = QFont("Fire Code")
        self.window_font.setPointSize(12)
        self.setFont(self.window_font)

        self.set_up_menu()
        self.set_up_body()


        self.show()

    def set_up_menu(self):
        menu_bar = self.menuBar()

        # file menu 
        file_menu = menu_bar.addMenu("File")

        new_file = file_menu.addAction("New")
        new_file.setShortcut("Ctrl+N")
        new_file.triggered.connect(self.new_file)

        open_file = file_menu.addAction("Open File")
        open_file.setShortcut("Ctrl+Q")
        open_file.triggered.connect(self.open_file)

        open_folder = file_menu.addAction("Open Folder")
        open_folder.setShortcut("Ctrl+K")
        open_folder.triggered.connect(self.open_folder)

        # Edit Menu
        edit_menu = menu_bar.addMenu("Edit")

        copy_action = edit_menu.addAction("Copy")
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.copy)
        

    def new_file(self):
        ... 
    
    def open_file(self):
        ...

    def open_folder(self):
        ... 
    
    def copy(self):
        ...

    def get_editor(self) -> QsciScintilla:
        pass

    def set_up_body(self):
        pass 



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())

    