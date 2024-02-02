# ------------------------------------------------------------- #
#  Name: TextEditor.py #######################################  #
#  Version: 1.0.0 ############################################  #
#  Author: Pedro Gartner #####################################  #
# ############################################################  #
#  Last Updated: 31th January, 2024 ##########################  #
# ------------------------------------------------------------- #
# ############################################################  #
# ------------------------------------------------------------- #
#  USAGE: ####################################################  #
# ############################################################  #
#  - Create a Panel to use as a Text Editor, can be used to ##  #
#    write notes or even open and save new files. ############# #
# ------------------------------------------------------------- #

import nuke
import nukescripts

import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtWidgets
from PySide2.QtGui import QIcon

from PySide2.QtWidgets import QApplication, QWidget

class TextEditorWidget(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super(TextEditorWidget, self).__init__(parent)

        self.setWindowTitle("To do List")

        self.text_title = QtWidgets.QLabel("What do I have to do:", self)
        self.text_edit = QtWidgets.QTextEdit(self)
        self.save_button = QtWidgets.QPushButton("Save", self)
        self.clear_button = QtWidgets.QPushButton("Clear", self)
        self.open_button = QtWidgets.QPushButton("Open", self)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.text_title)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.save_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.open_button)

        font = self.text_title.font()
        font.setPointSize(10)
        self.text_title.setFont(font)
        #self.text_title = Qt.AlignCenter

        self.save_button.clicked.connect(self.save)

        self.clear_button.clicked.connect(self.clear)

        self.open_button.clicked.connect(self.open)

    def save(self):        
        contents = self.text_edit.toPlainText()

        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File")
        if path:
            with open("text.txt", "w") as f:
                f.write(contents)

    def clear(self):
        self.text_edit.clear()

    def open(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")
        if filename:
            with open(filename, "r") as f:
                contents = f.read()
            self.text_edit.setPlainText(contents)

#widget = TextEditorWidget()

#panel = nuke.Panel("Text Editor")
#widget.show()