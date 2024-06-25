import sys
from gui.mainWindow import Ui_MainWindow
from PyQt5 import QtWidgets

def main():

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(main_window)
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

    # import os
    # import sys
    #
    # from py2puml.py2puml import py2puml
    #
    # #sys.path.append(os.path.join(os.path.dirname(__file__)))
    #
    # from pathlib import Path
    #
    # file_path = Path(os.getcwd() + "\\..\\py2puml\\class_diagram.puml")
    #
    # print(''.join(py2puml(domain_path='.',
    #                     domain_module='app')))
    #
    # # writes the PlantUML content in a file
    # with open(file_path, 'w') as puml_file:
    #     puml_file.writelines(py2puml(domain_path='.',
    #                                  domain_module='app'))
    #
