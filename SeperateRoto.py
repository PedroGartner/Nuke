# ------------------------------------------------------------- #
#  Name: SeperateRoto.py #####################################  #
#  Version: 1.0.0 ############################################  #
#  Author: Pedro Gartner #####################################  #
# ############################################################  #
#  Last Updated: 31th January, 2024 ##########################  #
# ------------------------------------------------------------- #
# ############################################################  #
# ------------------------------------------------------------- #
#  USAGE: ####################################################  #
# ############################################################  #
#  - Seperate the shapes in a roto node ######################  #
# ------------------------------------------------------------- #


import nuke
from PySide2 import QtWidgets, QtGui


class RotoSeparationPanel(QtWidgets.QWidget):
    def __init__(self):
        super(RotoSeparationPanel, self).__init__()

        self.setWindowTitle("Roto Separation")
        self.setGeometry(200, 200, 300, 100)

        layout = QtWidgets.QVBoxLayout(self)

        self.info_label = QtWidgets.QLabel(
            "Please select a Roto node"
        )
        layout.addWidget(self.info_label)

        self.separate_button = QtWidgets.QPushButton("Separate Shapes")
        layout.addWidget(self.separate_button)

        self.separate_button.clicked.connect(self.separate_shapes)

    def separate_shapes(self):
        selected_node = nuke.selectedNode()

        if selected_node and selected_node.Class() == "Roto":
            self.info_label.setText("Separating shapes. Please wait...")

            separate_shapes(selected_node)

            self.info_label.setText("Shapes separated successfully.")
        else:
            self.info_label.setText("Please select a valid Roto node.")


def separate_shapes(roto_node):
    layers = roto_node["curves"].rootLayer


    for layer in layers:
        layer_name = layer.name

        new_roto_node = nuke.createNode("Roto")


        new_roto_node["name"].setValue(layer_name)


        new_roto_node["curves"].rootLayer.append(layer.clone())

panel = RotoSeparationPanel()
panel.show()