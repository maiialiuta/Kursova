# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# import metrics ui
from app.gui.calculationsWindow import Ui_metricsWindow
from app.gui.metricsManualWindow import Ui_Dialog
from app.src.metrics.calculator.metrics_calculator import MetricsCalculator
from app.src.entities.the_project import Project
from app.src.generator.generate_ast import AstGenerator
from app.src.visitors.init_visitor import InitCommonsNodeVisitor


class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        self.window = MainWindow
        self.file_name = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        # set the size of window as fixed
        MainWindow.setFixedSize(569, 386)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:#224562;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calculateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calculateBtn.setGeometry(QtCore.QRect(120, 290, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.calculateBtn.setFont(font)
        self.calculateBtn.setStyleSheet("color:white;\n"
                                        "font-weight: bold;\n"
                                        "background-color: #B68F05;")
        self.calculateBtn.setObjectName("calculateBtn")
        self.openFolderButton = QtWidgets.QToolButton(self.centralwidget)
        self.openFolderButton.setGeometry(QtCore.QRect(320, 190, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.openFolderButton.setFont(font)
        self.openFolderButton.setStyleSheet("color:white;\n"
                                            "font-weight: bold;\n"
                                            "background-color: #B68F05;")
        self.openFolderButton.setObjectName("openFolderButton")
        self.nameLbl = QtWidgets.QLabel(self.centralwidget)
        self.nameLbl.setGeometry(QtCore.QRect(60, 30, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.nameLbl.setFont(font)
        self.nameLbl.setStyleSheet("color: #FFD43B;\n"
                                   "")
        self.nameLbl.setObjectName("nameLbl")
        self.pythonProjectLbl = QtWidgets.QLabel(self.centralwidget)
        self.pythonProjectLbl.setGeometry(QtCore.QRect(60, 90, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pythonProjectLbl.setFont(font)
        self.pythonProjectLbl.setStyleSheet("color: #FFD43B;")
        self.pythonProjectLbl.setObjectName("pythonProjectLbl")
        self.selectProjectLbl = QtWidgets.QLabel(self.centralwidget)
        self.selectProjectLbl.setGeometry(QtCore.QRect(120, 180, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectProjectLbl.setFont(font)
        self.selectProjectLbl.setStyleSheet("color:#C69C07;")
        self.selectProjectLbl.setObjectName("selectProjectLbl")
        self.helpBtn = QtWidgets.QToolButton(self.centralwidget)
        self.helpBtn.setGeometry(QtCore.QRect(510, 330, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.helpBtn.setFont(font)
        self.helpBtn.setStyleSheet("color:white;\n"
                                   "font-weight: bold;\n"
                                   "background-color: #B68F05;")
        self.helpBtn.setObjectName("helpBtn")
        self.selectedProjectLbl = QtWidgets.QLabel(self.centralwidget)
        self.selectedProjectLbl.setGeometry(QtCore.QRect(320, 240, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.selectedProjectLbl.setFont(font)
        self.selectedProjectLbl.setStyleSheet("color:#C69C07;")
        self.selectedProjectLbl.setObjectName("selectedProjectLbl")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 90, 181, 71))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

       # set click listeners
        self.openFolderButton.clicked.connect(self.openFiles)
        self.calculateBtn.clicked.connect(self.calcMetrics)
        self.helpBtn.clicked.connect(self.openManual)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # set title
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Metrics Calculator"))
        # set favicon
        import os
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        #MainWindow.setWindowIcon(QtGui.QIcon(scriptDir + '\\resources\images\\favicons\\favicon.png'))
        self.calculateBtn.setText(_translate("MainWindow", "START CALCULATING..."))
        self.openFolderButton.setText(_translate("MainWindow", "Open Folder"))
        self.nameLbl.setText(_translate("MainWindow", "Metrics Calculator"))
        #self.pythonProjectLbl.setText(_translate("MainWindow", "For Python Projects"))
        self.selectProjectLbl.setText(_translate("MainWindow", "Select your project:"))
        self.helpBtn.setText(_translate("MainWindow", "?"))
        self.selectedProjectLbl.setText(_translate("MainWindow", "selected _project"))

    # method that opens file dialog
    def openFiles(self):
        self.file_name = QtWidgets.QFileDialog.getExistingDirectory()

        if (self.file_name):
            self.selectedProjectLbl.setText(self.file_name.split('/')[-1])

    # method that calculates metrics
    def calcMetrics(self):
        if self.file_name != '':
            test_project_name = self.file_name.split('/')[-1]
            project = Project(self.file_name, test_project_name)
            AstGenerator(project).start_parsing()

            # Init existing classes for each .py file of the project
            for python_file_obj in project.get_files():
                InitCommonsNodeVisitor(python_file_obj).visit_Module(python_file_obj.get_generated_ast())

            # Calculate Metrics for each class
            for python_file_obj in project.get_files():
                for class_obj in python_file_obj.get_file_classes():
                    MetricsCalculator(class_obj)

            self.calculationsWindow = QtWidgets.QDialog()
            self.ui = Ui_metricsWindow()
            self.ui.setupUi(self.calculationsWindow, project, self.window)
            self.calculationsWindow.show()
            self.window.close()
        elif self.file_name == '':
            self.selectedProjectLbl.setText("You must select a Project")

    def openManual(self):
        self.manualWindow = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.manualWindow, self.window)
        self.manualWindow.show()
        self.window.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
