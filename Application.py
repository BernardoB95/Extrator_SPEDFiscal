# Form implementation generated from reading ui file 'QtApplication.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from EngineGUI import ProcessingEngine
from Utils import scrapper, GUINamespace
from datetime import datetime
from PyQt6 import QtCore, QtGui, QtWidgets


class Worker(QtCore.QThread):
    log = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal()

    def __init__(self, main):
        super().__init__()
        self.main = main

    def run(self):
        start = datetime.now()

        args = GUINamespace()
        args.input_dir = os.path.normpath(self.main.InputText_Field.toPlainText())
        args.output_dir = os.path.normpath(self.main.OutputText_Field.toPlainText())
        args.verbose = True
        args.regs = scrapper() if not self.main.Registers_Checkbox.isChecked() \
            else self.main.Registers_Field.toPlainText().split(" ")

        engine = ProcessingEngine(args, self.log)
        engine.main()

        end = datetime.now()

        # region Time Calculation

        exec_time = (end - start).seconds
        minutes = exec_time // 60
        seconds = exec_time - (minutes * 60)
        self.log.emit('Extraction completed.')
        self.log.emit('Process completed in {0}:{1:02d}'.format(minutes, seconds))

        # endregion

        self.finished.emit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 509)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 361, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.HorizontalInput_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.HorizontalInput_Layout.setContentsMargins(0, 0, 0, 0)
        self.HorizontalInput_Layout.setObjectName("HorizontalInput_Layout")
        self.ReadingDir_Label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ReadingDir_Label.setFont(font)
        self.ReadingDir_Label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.ReadingDir_Label.setObjectName("ReadingDir_Label")
        self.HorizontalInput_Layout.addWidget(self.ReadingDir_Label)
        self.InputButtonContainer_Frame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.InputButtonContainer_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.InputButtonContainer_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.InputButtonContainer_Frame.setObjectName("InputButtonContainer_Frame")
        self.Input_Button = QtWidgets.QPushButton(self.InputButtonContainer_Frame)
        self.Input_Button.setGeometry(QtCore.QRect(25, 5, 93, 28))
        self.Input_Button.setObjectName("Input_Button")
        self.HorizontalInput_Layout.addWidget(self.InputButtonContainer_Frame)
        self.InputText_Field = QtWidgets.QTextBrowser(self.centralwidget)
        self.InputText_Field.setEnabled(False)
        self.InputText_Field.setGeometry(QtCore.QRect(20, 60, 351, 31))
        self.InputText_Field.setObjectName("InputText_Field")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 120, 361, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.HorizontalOutput_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.HorizontalOutput_Layout.setContentsMargins(0, 0, 0, 0)
        self.HorizontalOutput_Layout.setObjectName("HorizontalOutput_Layout")
        self.WritingDir_Label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WritingDir_Label.setFont(font)
        self.WritingDir_Label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.WritingDir_Label.setObjectName("WritingDir_Label")
        self.HorizontalOutput_Layout.addWidget(self.WritingDir_Label)
        self.OutputButtonContainer_Frame = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.OutputButtonContainer_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.OutputButtonContainer_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.OutputButtonContainer_Frame.setObjectName("OutputButtonContainer_Frame")
        self.Output_Button = QtWidgets.QPushButton(self.OutputButtonContainer_Frame)
        self.Output_Button.setGeometry(QtCore.QRect(25, 5, 93, 28))
        self.Output_Button.setObjectName("Output_Button")
        self.HorizontalOutput_Layout.addWidget(self.OutputButtonContainer_Frame)
        self.OutputText_Field = QtWidgets.QTextBrowser(self.centralwidget)
        self.OutputText_Field.setEnabled(False)
        self.OutputText_Field.setGeometry(QtCore.QRect(20, 160, 351, 31))
        self.OutputText_Field.setObjectName("OutputText_Field")
        self.Process_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Process_Button.setEnabled(False)
        self.Process_Button.setGeometry(QtCore.QRect(400, 25, 93, 28))
        self.Process_Button.setObjectName("Process_Button")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(385, 20, 16, 171))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.Close_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Close_Button.setGeometry(QtCore.QRect(400, 60, 93, 28))
        self.Close_Button.setObjectName("Close_Button")
        self.Registers_Checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.Registers_Checkbox.setEnabled(True)
        self.Registers_Checkbox.setGeometry(QtCore.QRect(20, 220, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Registers_Checkbox.setFont(font)
        self.Registers_Checkbox.setObjectName("Registers_Checkbox")
        self.Registers_Field = QtWidgets.QTextEdit(self.centralwidget)
        self.Registers_Field.setEnabled(False)
        self.Registers_Field.setGeometry(QtCore.QRect(20, 250, 471, 31))
        self.Registers_Field.setObjectName("Registers_Field")
        self.LogOutput_Field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.LogOutput_Field.setReadOnly(True)
        self.LogOutput_Field.setStyleSheet('background-color: white; font-size: 11px')
        self.LogOutput_Field.setGeometry(QtCore.QRect(20, 320, 471, 131))
        self.LogOutput_Field.setObjectName("LogOutput_Field")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(70, 295, 421, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 295, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 519, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # region Events
        self.Close_Button.clicked.connect(lambda: MainWindow.close())
        self.Input_Button.clicked.connect(self.click_selecionar_input)
        self.Output_Button.clicked.connect(self.click_selecionar_output)
        self.Registers_Checkbox.toggled.connect(self.selecionar_registros_is_checked)
        self.Registers_Checkbox.toggled.connect(self.processing_prerequisites)
        self.InputText_Field.textChanged.connect(self.processing_prerequisites)
        self.OutputText_Field.textChanged.connect(self.processing_prerequisites)
        self.Registers_Field.textChanged.connect(self.processing_prerequisites)
        self.Process_Button.clicked.connect(self.click_process)
        # endregion

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Extrator SPED Fiscal"))
        self.ReadingDir_Label.setText(_translate("MainWindow", "Selecionar Diretorio de Leitura"))
        self.Input_Button.setText(_translate("MainWindow", "Selecionar"))
        self.WritingDir_Label.setText(_translate("MainWindow", "Selecionar Diretorio de Escrita"))
        self.Output_Button.setText(_translate("MainWindow", "Selecionar"))
        self.Process_Button.setText(_translate("MainWindow", "Process"))
        self.Close_Button.setText(_translate("MainWindow", "Fechar"))
        self.Registers_Checkbox.setText(_translate("MainWindow", "Selecionar Registros"))
        self.label.setText(_translate("MainWindow", "Logger"))

    def click_selecionar_input(self):
        """
        This function will open up a window to select the directory
        :return: Directory Name
        :rtype: str
        """
        __dir = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                           'Selecionar Diretorio de Leitura',
                                                           'C:\\')

        self.InputText_Field.setText(__dir)

    def click_selecionar_output(self):
        """
        This fucntion will open up a window to select the directory
        :return: Directory Name
        :rtype: str
        """
        __dir = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                           'Selecionar Diretorio de Escrita',
                                                           'C:\\')

        self.OutputText_Field.setText(__dir)

    def selecionar_registros_is_checked(self):
        """
        This function will enable or disable the manual input of REGs to be processed.
        :return: None
        """
        state = self.Registers_Checkbox.isChecked()

        self.Registers_Field.setEnabled(state)

    def processing_prerequisites(self):
        """
        This function will check all pre-requisites before processing in order to enable the button.
        :return: None
        """
        register_state = self.Registers_Checkbox.isChecked()

        if self.InputText_Field.toPlainText() != "" and self.OutputText_Field.toPlainText() != "":

            if register_state and self.Registers_Field.toPlainText() != "":
                self.Process_Button.setEnabled(True)
            elif not register_state:
                self.Process_Button.setEnabled(True)
            else:
                self.Process_Button.setEnabled(False)
        else:
            self.Process_Button.setEnabled(False)

    def update_log(self, message):
        """
        This function will update the log when the signal of the thread is emitted.
        :return:
        :rtype:
        """
        self.LogOutput_Field.appendPlainText(message)

    def click_process(self):
        """
        This is the main function that will take as arguments all data inputted on the text fields above
        :return: None
        """
        # TODO implement print function for verbosity

        # Create Worker Thread
        self.worker = Worker(self)

        self.worker.start()
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.log.connect(self.update_log)

        # Safety Lock
        self.Process_Button.setEnabled(False)
        self.worker.finished.connect(lambda: self.Process_Button.setEnabled(True))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
