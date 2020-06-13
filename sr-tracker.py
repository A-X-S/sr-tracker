# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import csv

roles = ["tank", "damage", "support"]


def current(role):
    file = "data/" + role + ".csv"
    lines = []
    with open(file, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        try:
            for i in csvreader:
                for j in i:
                    lines.append(int(j))
            return str(lines[-1])
        except IndexError:
            return "XXXX"


def show():
    plt.rcParams['toolbar'] = 'None'
    for role in roles:
        x = []
        y = []
        file = "data/" + role + ".csv"
        with open(file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for i in csvreader:
                for j in i:
                    y.append(int(j))
            x = list(range(1, len(y) + 1))
        plt.plot(x, y, label=role)
    plt.ylabel('SR')
    plt.xlabel('Games')
    plt.legend()
    plt.show()


def clear():
    for role in roles:
        file = "data/" + role + ".csv"
        with open(file, "w") as csvfile:
            csvfile.truncate()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(627, 675)
        MainWindow.setMinimumSize(QtCore.QSize(627, 675))
        MainWindow.setMaximumSize(QtCore.QSize(627, 675))
        self.main_widget = QtWidgets.QWidget(MainWindow)
        self.main_widget.setStyleSheet(
            """
            QWidget {
                color: rgb(250, 156, 30);
                background: black;
            }
            QLabel {
                font: 100pt \"Verdana\";
            }
            QLineEdit {
                color: black;
                font: 10pt \"Verdana\";
                background: white;
                selection-background-color: rgb(250, 156, 30);
                border: none;
                padding: 0 2px;
            }
            QPushButton {
                background-color: rgb(250, 156, 30);
                color: white;
                font: 10pt \"Verdana\";
                border: 2px solid;
                padding: 1 5px;
            }
            QPushButton:pressed {
                background-color: white;
                color: black;
            }
            """
            )
        self.main_widget.setObjectName("main_widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 627, 1153))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setContentsMargins(30, 10, 30, 500)
        self.main_layout.setObjectName("main_layout")

        # T
        self.t_layout = QtWidgets.QHBoxLayout()
        self.t_layout.setContentsMargins(-1, 5, -1, 5)
        self.t_layout.setObjectName("t_layout")
        self.t_icon = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.t_icon.setPixmap(QtGui.QPixmap("icons/t150.png"))
        self.t_icon.setObjectName("t_icon")
        self.t_layout.addWidget(self.t_icon)
        self.t_right = QtWidgets.QVBoxLayout()
        self.t_right.setObjectName("t_right")
        self.t_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.t_number.setAlignment(QtCore.Qt.AlignCenter)
        self.t_number.setObjectName("t_number")
        self.t_right.addWidget(self.t_number)
        self.t_bottom = QtWidgets.QHBoxLayout()
        self.t_bottom.setObjectName("t_bottom")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.t_bottom.addItem(spacerItem)
        self.t_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.t_edit.setMaximumSize(QtCore.QSize(65, 16777215))
        self.t_edit.setObjectName("t_edit")
        self.t_edit.returnPressed.connect(self.t_update)
        self.t_bottom.addWidget(self.t_edit)
        self.t_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.t_button.setMaximumSize(QtCore.QSize(65, 16777215))
        self.t_button.setObjectName("t_button")
        self.t_button.clicked.connect(self.t_update)
        self.t_bottom.addWidget(self.t_button)
        self.t_right.addLayout(self.t_bottom)
        self.t_layout.addLayout(self.t_right)
        self.main_layout.addLayout(self.t_layout)

        self.line_1 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_1.setStyleSheet("border: 2px solid rgb(250, 156, 30);")
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.main_layout.addWidget(self.line_1)

        # D
        self.d_layout = QtWidgets.QHBoxLayout()
        self.d_layout.setContentsMargins(-1, 5, -1, 5)
        self.d_layout.setObjectName("d_layout")
        self.d_icon = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.d_icon.setPixmap(QtGui.QPixmap("icons/d150.png"))
        self.d_icon.setObjectName("d_icon")
        self.d_layout.addWidget(self.d_icon)
        self.d_right = QtWidgets.QVBoxLayout()
        self.d_right.setObjectName("d_right")
        self.d_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.d_number.setAlignment(QtCore.Qt.AlignCenter)
        self.d_number.setObjectName("d_number")
        self.d_right.addWidget(self.d_number)
        self.d_bottom = QtWidgets.QHBoxLayout()
        self.d_bottom.setObjectName("d_bottom")
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.d_bottom.addItem(spacerItem1)
        self.d_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.d_edit.setMaximumSize(QtCore.QSize(65, 16777215))
        self.d_edit.setObjectName("d_edit")
        self.d_edit.returnPressed.connect(self.d_update)
        self.d_bottom.addWidget(self.d_edit)
        self.d_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.d_button.setMaximumSize(QtCore.QSize(65, 16777215))
        self.d_button.setObjectName("d_button")
        self.d_button.clicked.connect(self.d_update)
        self.d_bottom.addWidget(self.d_button)
        self.d_right.addLayout(self.d_bottom)
        self.d_layout.addLayout(self.d_right)
        self.main_layout.addLayout(self.d_layout)

        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setStyleSheet("border: 2px solid rgb(250, 156, 30);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.main_layout.addWidget(self.line_2)

        # S
        self.s_layout = QtWidgets.QHBoxLayout()
        self.s_layout.setContentsMargins(-1, 5, -1, 5)
        self.s_layout.setObjectName("s_layout")
        self.s_icon = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.s_icon.setPixmap(QtGui.QPixmap("icons/s150.png"))
        self.s_icon.setObjectName("s_icon")
        self.s_layout.addWidget(self.s_icon)
        self.s_right = QtWidgets.QVBoxLayout()
        self.s_right.setObjectName("s_right")
        self.s_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.s_number.setAlignment(QtCore.Qt.AlignCenter)
        self.s_number.setObjectName("s_number")
        self.s_right.addWidget(self.s_number)
        self.s_bottom = QtWidgets.QHBoxLayout()
        self.s_bottom.setObjectName("s_bottom")
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.s_bottom.addItem(spacerItem2)
        self.s_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.s_edit.setMaximumSize(QtCore.QSize(65, 16777215))
        self.s_edit.setObjectName("s_edit")
        self.s_edit.returnPressed.connect(self.s_update)
        self.s_bottom.addWidget(self.s_edit)
        self.s_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.s_button.setMaximumSize(QtCore.QSize(65, 16777215))
        self.s_button.setObjectName("s_button")
        self.s_button.clicked.connect(self.s_update)
        self.s_bottom.addWidget(self.s_button)
        self.s_right.addLayout(self.s_bottom)
        self.s_layout.addLayout(self.s_right)
        self.main_layout.addLayout(self.s_layout)
        MainWindow.setCentralWidget(self.main_widget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 627, 21))
        self.menuBar.setStyleSheet(
            """
            QMenuBar {
                background-color: white;
            }
            QMenuBar::item {
                font: 10pt \"Verdana\";
            }
            QMenuBar::item:selected {
                background: rgb(250, 156, 30);
                }
            """
        )

        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)

        self.actionShow_graphs = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/chart-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShow_graphs.setIcon(icon)
        self.actionShow_graphs.setObjectName("actionShow_graphs")
        self.actionShow_graphs.triggered.connect(show)

        self.actionClear_all_data = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/database-delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear_all_data.setIcon(icon1)
        self.actionClear_all_data.setObjectName("actionClear_all_data")
        self.actionClear_all_data.triggered.connect(clear)

        self.menuFile.addAction(self.actionShow_graphs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClear_all_data)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SR TRACKER"))
        tank = current("tank")
        self.t_number.setText(_translate("MainWindow", tank))
        self.t_button.setText(_translate("MainWindow", "UPDATE"))
        damage = current("damage")
        self.d_number.setText(_translate("MainWindow", damage))
        self.d_button.setText(_translate("MainWindow", "UPDATE"))
        support = current("support")
        self.s_number.setText(_translate("MainWindow", support))
        self.s_button.setText(_translate("MainWindow", "UPDATE"))
        self.menuFile.setTitle(_translate("MainWindow", "Menu"))
        self.actionShow_graphs.setText(_translate("MainWindow", "Show graphs"))
        self.actionClear_all_data.setText(_translate("MainWindow", "Clear all data"))

    def t_update(self):
        file = "data/tank.csv"
        with open(file, "a") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow({self.t_edit.text()})
        self.t_number.setText(self.t_edit.text())
        self.t_edit.clear()

    def d_update(self):
        file = "data/damage.csv"
        with open(file, "a") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow({self.d_edit.text()})
        self.d_number.setText(self.d_edit.text())
        self.d_edit.clear()

    def s_update(self):
        file = "data/support.csv"
        with open(file, "a") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow({self.s_edit.text()})
        self.s_number.setText(self.s_edit.text())
        self.s_edit.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
