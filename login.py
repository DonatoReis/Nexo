# Form implementation generated from reading ui file '.\Ui\pagelogin.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindowAcesso(object):
    def setupUi(self, MainWindowAcesso):
        MainWindowAcesso.setObjectName("MainWindowAcesso")
        MainWindowAcesso.resize(251, 299)
        MainWindowAcesso.setMinimumSize(QtCore.QSize(251, 299))
        MainWindowAcesso.setMaximumSize(QtCore.QSize(251, 299))
        MainWindowAcesso.setStyleSheet("background-color: rgb(28, 35, 49);")
        self.centralacesso = QtWidgets.QWidget(parent=MainWindowAcesso)
        self.centralacesso.setObjectName("centralacesso")
        self.label_23 = QtWidgets.QLabel(parent=self.centralacesso)
        self.label_23.setGeometry(QtCore.QRect(31, 100, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.centralacesso)
        self.label_24.setGeometry(QtCore.QRect(31, 167, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_24.setObjectName("label_24")
        self.label_inserir_user = QtWidgets.QLineEdit(parent=self.centralacesso)
        self.label_inserir_user.setGeometry(QtCore.QRect(4, 120, 241, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_inserir_user.setFont(font)
        self.label_inserir_user.setStyleSheet("background-color: rgb(28, 35, 49);\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_inserir_user.setText("")
        self.label_inserir_user.setClearButtonEnabled(True)
        self.label_inserir_user.setObjectName("label_inserir_user")
        self.widget = QtWidgets.QWidget(parent=self.centralacesso)
        self.widget.setGeometry(QtCore.QRect(4, 150, 241, 2))
        self.widget.setStyleSheet("background-color: rgb(48, 75, 127);")
        self.widget.setObjectName("widget")
        self.label_inserir_senha = QtWidgets.QLineEdit(parent=self.centralacesso)
        self.label_inserir_senha.setGeometry(QtCore.QRect(4, 187, 241, 31))
        self.label_inserir_senha.setStyleSheet("background-color: rgb(28, 35, 49);\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.label_inserir_senha.setText("")
        self.label_inserir_senha.setMaxLength(16)
        self.label_inserir_senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.label_inserir_senha.setDragEnabled(False)
        self.label_inserir_senha.setReadOnly(False)
        self.label_inserir_senha.setPlaceholderText("")
        self.label_inserir_senha.setClearButtonEnabled(True)
        self.label_inserir_senha.setObjectName("label_inserir_senha")
        self.widget_2 = QtWidgets.QWidget(parent=self.centralacesso)
        self.widget_2.setGeometry(QtCore.QRect(4, 217, 241, 2))
        self.widget_2.setStyleSheet("background-color: rgb(48, 75, 127);")
        self.widget_2.setObjectName("widget_2")
        self.botao_confirmar_acesso = QtWidgets.QPushButton(parent=self.centralacesso)
        self.botao_confirmar_acesso.setGeometry(QtCore.QRect(83, 243, 75, 24))
        self.botao_confirmar_acesso.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(186, 195, 204);\n"
"    border: 3px solid rgb(186, 195, 204);\n"
"    color: rgb(28, 35, 49);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"   color: rgb(32, 32, 35);\n"
"   border-radius: 5px;\n"
"   background-color: rgb(233, 244, 255);\n"
"}")
        self.botao_confirmar_acesso.setObjectName("botao_confirmar_acesso")
        self.label_validar_acesso = QtWidgets.QLabel(parent=self.centralacesso)
        self.label_validar_acesso.setGeometry(QtCore.QRect(7, 279, 131, 20))
        self.label_validar_acesso.setStyleSheet("color: rgb(234, 234, 234);")
        self.label_validar_acesso.setObjectName("label_validar_acesso")
        self.logo_acesso = QtWidgets.QLabel(parent=self.centralacesso)
        self.logo_acesso.setGeometry(QtCore.QRect(94, 20, 61, 61))
        self.logo_acesso.setText("")
        self.logo_acesso.setPixmap(QtGui.QPixmap(".\\Ui\\../Imagens/nexo.png"))
        self.logo_acesso.setScaledContents(True)
        self.logo_acesso.setObjectName("logo_acesso")
        self.label = QtWidgets.QLabel(parent=self.centralacesso)
        self.label.setGeometry(QtCore.QRect(4, 100, 21, 21))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\Ui\\../icons/iconuser.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralacesso)
        self.label_2.setGeometry(QtCore.QRect(6, 168, 18, 18))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".\\Ui\\../icons/iconpass.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.checkBox_visualizar_senha = QtWidgets.QCheckBox(parent=self.centralacesso)
        self.checkBox_visualizar_senha.setGeometry(QtCore.QRect(194, 220, 51, 20))
        self.checkBox_visualizar_senha.setStyleSheet("color: rgb(233, 244, 255);")
        self.checkBox_visualizar_senha.setObjectName("checkBox_visualizar_senha")
        self.spinner_label = QtWidgets.QLabel(parent=self.centralacesso)
        self.spinner_label.setGeometry(QtCore.QRect(100, 223, 47, 13))
        self.spinner_label.setText("")
        self.spinner_label.setObjectName("spinner_label")
        MainWindowAcesso.setCentralWidget(self.centralacesso)

        self.retranslateUi(MainWindowAcesso)
        QtCore.QMetaObject.connectSlotsByName(MainWindowAcesso)

    def retranslateUi(self, MainWindowAcesso):
        _translate = QtCore.QCoreApplication.translate
        MainWindowAcesso.setWindowTitle(_translate("MainWindowAcesso", "Login"))
        self.label_23.setText(_translate("MainWindowAcesso", "Username"))
        self.label_24.setText(_translate("MainWindowAcesso", "Password"))
        self.botao_confirmar_acesso.setText(_translate("MainWindowAcesso", "Login"))
        self.label_validar_acesso.setText(_translate("MainWindowAcesso", ""))
        self.checkBox_visualizar_senha.setText(_translate("MainWindowAcesso", "Exibir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowAcesso = QtWidgets.QMainWindow()
    ui = Ui_MainWindowAcesso()
    ui.setupUi(MainWindowAcesso)
    MainWindowAcesso.show()
    sys.exit(app.exec())