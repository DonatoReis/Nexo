from PyQt6 import QtWidgets, QtGui
from sqlite3 import connect, Error
from deletitem import Ui_MainWindowDeleteBox
from PyQt6.QtWidgets import QMainWindow

class DELETE(QMainWindow, Ui_MainWindowDeleteBox):
    def __init__(self) -> None:
        super(DELETE, self).__init__()
        self.ui = Ui_MainWindowDeleteBox()
        self.ui.setupUi(self)
        self.recebe_dados('prazos', 'prazo')
        self.recebe_dados('produtos', 'produto')
        self.recebe_dados('transportadoras', 'tranportadora')
        self.recebe_dados('frete', 'fretes')
        self.recebe_dados('vendedor', 'vendedores')

        self.ui.botao_excluir_produto.clicked.connect(lambda: self.deletaritem('produtos', 'produto'))
        self.ui.botao_excluir_frete.clicked.connect(lambda: self.deletaritem('frete', 'fretes'))
        self.ui.botao_excluir_prazo.clicked.connect(lambda: self.deletaritem('prazos', 'prazo'))
        self.ui.botao_excluir_transporte.clicked.connect(lambda: self.deletaritem('transportadoras', 'tranportadora'))
        self.ui.botao_excluir_vendedor.clicked.connect(lambda: self.deletaritem('vendedor', 'vendedores'))

    def deletaritem(self, table, column):
        dados = self.ui.comboBox_item_delete.currentText()
        try:
            banco = connect("system.db")
            cursor = banco.cursor()
            cursor.execute(f"DELETE FROM {table} WHERE {column}=?", (dados,))
            banco.commit()
            cursor.close()
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("PIE")
            msg.setText(f"{dados} excluido com sucesso em {table}")
            msg.setInformativeText("Atualize o banco de dados")
            msg.setWindowIcon(QtGui.QIcon('icons\\footprint.ico'))
            msg.setWindowTitle("Aviso")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        except Error as erro:
            print("Erro", erro)

    def recebe_dados(self, table, column):
        banco = connect("system.db")
        cursor = banco.cursor()
        cursor.execute(f'SELECT {column} FROM {table}')
        dados_lidos = sorted(cursor.fetchall())
        for row in dados_lidos:
            self.ui.comboBox_item_delete.addItems(row)
        cursor.close()
        banco.close()
