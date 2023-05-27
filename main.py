# Módulos padrão do Python
from time import time
from math import ceil
from os import path, remove, mkdir
from shutil import copyfile, rmtree
from sys import argv
from time import strftime
from threading import Thread

# Módulos de terceiros
from PyQt6 import QtCore, QtWidgets, QtGui, QtPrintSupport
from PyQt6.QtWidgets import QFileDialog, QApplication, QMainWindow, QLineEdit
from PyQt6.QtPrintSupport import QPrinter
from dotenv import load_dotenv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from requests import get
from smtplib import SMTP
from sqlite3 import connect, Error
from win10toast import ToastNotifier
from pywhatkit import sendwhatmsg_instantly
from pathlib import Path
import locale # Atualiza as labels da interface com os valores atualizados (não utilizado)
import os

# Módulos locais
from login import Ui_MainWindowAcesso
from tela import Ui_MainWindow
from cadastrar import CADASTRAR
from delete import DELETE
from telaCadastro import Ui_Form

dirPath = Path('C:\\Nexo')
NEXO_DIRECTORY = "C:\\Nexo"

if dirPath.exists():
    try:
        rmtree(dirPath)
    except Exception as e:
        print(f"Erro ao remover o diretório: {e}")

if not dirPath.exists():
    try:
        dirPath.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Erro ao criar o diretório: {e}")

usuario = ""
row = 0
row2 = 0
qtdd = 0.0
valor = 0.0

with open("row.txt", "w") as f:
    f.write("0")

#CLASSE TELA LOGIN
class LOGIN(QMainWindow, Ui_MainWindowAcesso):
    def __init__(self) -> None:
        super(LOGIN, self).__init__()
        self.ui = Ui_MainWindowAcesso()
        self.ui.setupUi(self)
        self.switch_window = QtCore.pyqtSignal()
        self.ui.botao_confirmar_acesso.clicked.connect(self.checkLogin)
        self.ui.label_inserir_senha.returnPressed.connect(self.checkLogin)
        self.ui.label_inserir_user.returnPressed.connect(self.checkLogin)
        self.ui.checkBox_visualizar_senha.stateChanged.connect(self.toggle_password_visibility)
        self.log_file = open(f"{NEXO_DIRECTORY}\\log.txt", "w")
        try:
            self.conn = connect("system.db")
            self.cursor = self.conn.cursor()
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
        
    def toggle_password_visibility(self):
        self.obter_check_senha = self.ui.checkBox_visualizar_senha.isChecked()
        if self.obter_check_senha == False:
            # Oculta a senha
            self.ui.label_inserir_senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        elif self.obter_check_senha == True:
            # Mostra a senha
            self.ui.label_inserir_senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)

    def checkLogin(self):
        user = self.ui.label_inserir_user.text()

        global usuario
        usuario = user.capitalize()

        self.log_file.write(str(user))

        password = self.ui.label_inserir_senha.text()
        try:
            self.cursor.execute("SELECT user, password FROM users WHERE user = ?;", (user,))
            result = self.cursor.fetchone()

            if result and result[1] == password:
                self.w = MainWindow()
                self.w.show()
                self.close()
            else:
                self.ui.label_validar_acesso.setText("Login ou senha inválidos!")
        except Error as e:
            print(f"Erro ao consultar o banco de dados: {e}")

    def closeEvent(self, event):
        self.log_file.close()
        self.conn.close()

#CLASSE TELA PRINCIPAL
class MainWindow(QMainWindow, Ui_MainWindow): #tela
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.recebe_dados('prazos', 'prazo', self.ui.comboBox_prazo_vendas)
        self.recebe_dados('produtos', 'produto', self.ui.comboBox_produto_vendas)
        self.recebe_dados('transportadoras', 'tranportadora', self.ui.comboBox_transport_vendas)
        self.recebe_dados('frete', 'fretes', self.ui.comboBox_frete_vendas)
        self.recebe_dados('vendedor', 'vendedores', self.ui.comboBox_vendedor_vendas)
        self.recebe_dados('embalagens', 'emb', self.ui.comboBox_embalagem_vendas)
        self.insertLembrete()
        # Cria uma instância da classe CADASTRAR
        cadastro = CADASTRAR()

        # Cria uma instância da classe DELETE
        exclusao = DELETE()
        
        self.ui.actionProtudo.triggered.connect(self.add)
        self.ui.actionexcluir_item.triggered.connect(self.add2)
        
        self.ui.botao_inserir_pedido_vendas_2.clicked.connect(self.tela_cadastrar)

        self.ui.botao_calcula_dolar.clicked.connect(self.pegar_cotacoes)
        self.ui.botao_ok_fabricacao.clicked.connect(self.inserir_codigo)
        self.ui.botao_ok_dolar.clicked.connect(self.conv_dolar)
        self.ui.botao_inserir_produto_vendas.clicked.connect(self.inserir_tabela)
        self.ui.botao_limpar_pedido_venda.clicked.connect(self.clear_it)
        self.ui.botao_send_email_vendas.clicked.connect(self.enviar_email)
        self.ui.botao_send_whatsapp_vendas.clicked.connect(self.enviar_whatsapp)
        self.ui.botao_baixar_pedido_vendas.clicked.connect(self.baixar_pedido)
        self.ui.botao_atualizar_database.clicked.connect(self.update_database)
        self.ui.botao_limpar_2.clicked.connect(self.calcular_frete)
        self.ui.botao_gravar_lembrete.clicked.connect(self.lembretes)
        self.ui.botao_imprimir_pedido_vendas.clicked.connect(self.imprimir)

        global usuario
        self.ui.label_recebe_user_logado.setText(f"{usuario}")

        self.clear_files()
        
    def tela_cadastrar(self):
        self.janela = QtWidgets.QMainWindow()
        self.cadastra = Ui_Form()
        self.cadastra.setupUi(self.janela)
        self.janela.show()

    def add(self):
        # Chama a tela cadastrar no banco de dados
        self.add = CADASTRAR()
        self.add.show()

    def add2(self):
        # Chama a tela deletar do banco de dados
        self.add = DELETE()
        self.add.show()

    def clear_files(self):
        try:
            files_to_remove = [
                f"{NEXO_DIRECTORY}\\pedido.txt",
                f"{NEXO_DIRECTORY}\\pedido.pdf",
                f"{NEXO_DIRECTORY}\\log.txt"
            ]
            for file_path in files_to_remove:
                if path.exists(file_path):
                    remove(file_path)
        except OSError as e:
            print(f"Erro ao remover arquivos: {e}")

    def pegar_cotacoes(self):
        thread = Thread(target=self._pegar_cotacoes_thread)
        thread.start()

    def _pegar_cotacoes_thread(self):
        try:
            requisicao = get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
            requisicao_dic = requisicao.json()
            cotacao_dolar = requisicao_dic.get('USDBRL', {}).get('bid')
            cotacao_euro = requisicao_dic.get('EURBRL', {}).get('bid')
            if cotacao_dolar and cotacao_euro:
                texto = f'''[ {strftime("%H:%M:%S")} ]
                Dólar: {cotacao_dolar}
                Euro: {cotacao_euro}'''
                self.ui.label_get_dolar.setText(texto)
                self.ui.valordolar = float(cotacao_dolar)
            else:
                print("Erro ao obter cotações")
        except Exception as e:
            print(f"Erro na requisição das cotações: {e}")

    def inserir_codigo(self):
        try:
            # Obter o valor de custo de fabricação do campo de entrada e convertê-lo para float
            custo_fabricacao = float(self.ui.insere_valor_custo.text())
        except ValueError:
            print("Valor de custo de fabricação inválido")
            custo_fabricacao = 0.0

        try:
            # Calcular os valores com base no custo de fabricação
            soma_operacional = custo_fabricacao + (custo_fabricacao * 75 / 100)
            custo_real = soma_operacional / 0.6
            revenda = custo_fabricacao + (custo_fabricacao * 120 / 100)
            lucro_liquido = custo_real - soma_operacional

            # Formatar os resultados para exibição com 2 casas decimais e o prefixo "R$"
            resultado_operacional = f"R$ {soma_operacional:.2f}"
            resultado_real = f"R$ {custo_real:.2f}"
            resultado_revenda = f"R$ {revenda:.2f}"
            resultado_lucro_liquido = f"R$ {lucro_liquido:.2f}"
            
            # Atualizar as labels da interface com os resultados calculados
            self.ui.label_recebe_operacional.setText(resultado_operacional)
            self.ui.label_recebe_ctvenda.setText(resultado_real)
            self.ui.label_recebe_fabrirevenda.setText(resultado_revenda)
            self.ui.label_recebe_lucroliqui.setText(resultado_lucro_liquido)
        except Exception as e:
            print(f"Erro ao calcular valores: {e}")

    def conv_dolar(self):
        try:
            # Obter o valor de conversão em dólar do campo de entrada e convertê-lo para float
            converter_dolar = float(self.ui.insere_valor_dolar.text())
            
            # Realizar a conversão multiplicando o valor de conversão pelo valor do dólar
            valor_convertido = converter_dolar * self.ui.insere_valor_dolar
            
            # Calcular o valor de revenda com base no valor convertido
            valor_revenda = valor_convertido + (valor_convertido * 120 / 100)

            # Formatar os resultados para exibição com 2 casas decimais e o prefixo "R$"
            resultado_convertido = f"R$ {valor_convertido:.2f}"
            resultado_revenda = f"R$ {valor_revenda:.2f}"
            
            # Atualizar as labels da interface com os resultados da conversão
            self.ui.label_dolar_convertido.setText(resultado_convertido)
            self.ui.label_dolar_revenda.setText(resultado_revenda)
        except ValueError:
            print("Valor de conversão inválido")

    def inserir_tabela(self):
        global row
        # =============================================== GUARDANDO VALORES INSERIDO NA TELA PRINCIPAL EM VARIAVEIS
        
        self.obter_cliente = (self.ui.insere_cliente.text())
        self.obter_produto = self.ui.comboBox_produto_vendas.currentText()
        self.obter_trasportadora = self.ui.comboBox_transport_vendas.currentText()
        self.obter_prazo = self.ui.comboBox_prazo_vendas.currentText()
        self.obter_preco = (self.ui.insere_preco_vendas.text())
        self.obter_frete = self.ui.comboBox_frete_vendas.currentText()
        self.obter_num_pedido = (self.ui.insere_num_pedido_vendas.text())
        self.obter_quantide = (self.ui.insere_quantidade_vendas.text())
        self.obter_vendedor = self.ui.comboBox_vendedor_vendas.currentText()
        self.obter_embalagem = self.ui.comboBox_embalagem_vendas.currentText()
        self.obter_unidade = self.ui.comboBox_unidade_vendas.currentText()
        self.obter_Nf = self.ui.checkBox_NF_vendas.isChecked()
        self.obter_Snf = self.ui.checkBox_SNF_vendas.isChecked()
        self.obter_obs = self.ui.observacoes.toPlainText()

        # =============================================== SALVANDO OS VALORES EM UM ARQUIVO DE TEXTO
        
        if self.obter_Nf == "False" or self.obter_Nf == False:
            if self.obter_Snf == "False" or self.obter_Snf == False:
                msg = QtWidgets.QMessageBox()
                msg.setText("Preencha a parte da nota fiscal")
                msg.setWindowIcon(QtGui.QIcon('icons\\footprint.ico'))
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()
                return True
        
        if self.obter_Nf == True:
            self.ui.checkBox_SNF_vendas.setEnabled(False)
        
        if self.obter_Snf == True:
            self.ui.checkBox_NF_vendas.setEnabled(False)
            
        # =============================================== INSERINDO PRECO, QUANTIDADE, PRODUTO E EMBALAGEM NA TABELA "PRODUTOS"
        self.ui.tabela_recebe_produto_vendas.setRowCount(len(self.obter_produto))
        #self.ui.tabela_recebe_produto_vendas.setItem(row, 0, QtWidgets.QTableWidgetItem(self.obter_codigo))
        self.ui.tabela_recebe_produto_vendas.setItem(row, 1, QtWidgets.QTableWidgetItem(self.obter_produto))
        self.ui.tabela_recebe_produto_vendas.setItem(row, 2, QtWidgets.QTableWidgetItem(self.obter_unidade))
        self.ui.tabela_recebe_produto_vendas.setItem(row, 3, QtWidgets.QTableWidgetItem(self.obter_quantide + " kg"))
        self.ui.tabela_recebe_produto_vendas.setItem(row, 4, QtWidgets.QTableWidgetItem(self.obter_embalagem))
        self.ui.tabela_recebe_produto_vendas.setItem(row, 5, QtWidgets.QTableWidgetItem("R$ " + self.obter_preco))
        #self.ui.tabela_recebe_produto_vendas.setItem(row, 6, QtWidgets.QTableWidgetItem(self.obter_CFOP))
        row=row+1

        if path.isdir(fr"{NEXO_DIRECTORY}\\Pedidos"):
             print()
        else:
             mkdir(fr"{NEXO_DIRECTORY}\\Pedidos")

        self.obter_snf_ou_nf = ""
        if self.obter_Nf == True:
            self.obter_snf_ou_nf = "NF: [✔️]"

        if self.obter_Snf == True:
            self.obter_snf_ou_nf = "NF: [✘]"
        
        file_path = fr"{NEXO_DIRECTORY}\\Pedidos\\Pedido_{self.obter_cliente}.txt"

        if os.path.exists(file_path):
            # O arquivo já existe, então apenas adicionamos o novo produto
            with open(file_path, "a", encoding="utf-8") as file:
                file.write(f"|PRODUTO: {self.obter_produto:<20} | QUANTIDADE: {self.obter_quantide:>6} kg | PREÇO: R$ {self.obter_preco:>10}\n")
        else:
            # O arquivo não existe, então criamos um novo e adicionamos todas as informações do pedido
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"\nPEDIDO DE VENDA\n")
                file.write(f"{'=' * 60}\n")
                file.write(f"|Obs: {self.obter_obs}\n")
                file.write(f"|VENDEDOR: {self.obter_vendedor}\n")
                file.write(f"|CLIENTE: {self.obter_cliente}\n")
                file.write(f"|PRAZO: {self.obter_prazo}\n")
                file.write(f"|N°PEDIDO: {self.obter_num_pedido}\n")
                file.write(f"|{self.obter_snf_ou_nf}\n")
                file.write(f"|TRANSPORTADORA: {self.obter_trasportadora}\n")
                file.write(f"|FRETE: {self.obter_frete}\n\n")
                file.write(f"PRODUTOS\n")
                file.write(f"{'-' * 60}\n")
                file.write(f"|PRODUTO: {self.obter_produto:<20} | QUANTIDADE: {self.obter_quantide:>6} kg | PREÇO: R$ {self.obter_preco:>10}\n")


        global qtdd
        global valor

        # Cálculo do peso e quantidade final
        try:
            preco = float(self.obter_preco.replace(',', '.'))
            quantidade = float(self.obter_quantide.replace(',', '.'))

            valor += preco * quantidade
            qtdd += quantidade

            # Definindo a localidade para 'pt_BR'
            locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

            # Formatando o valor de acordo com a localidade
            valor_formatado = locale.format_string('%.2f', valor, grouping=True)

            # Atualizando a label com o valor formatado
            self.ui.recebe_valor_total_vendas.setText(f"R$: {valor_formatado}")
            self.ui.recebe_peso_total_vendas.setText(f"{qtdd:.2f} kg")
        except ValueError:
            print("Valores de preço ou quantidade inválidos")

    def clear_it(self):
        import os
        global valor
        global qtdd
        global row
        row = 0

        # Limpando completamente a tabela de frete
        self.ui.tabela_recebe_produto_2.setRowCount(0)

        # Limpando a primeira linha da tabela de produtos
        if self.ui.tabela_recebe_produto_vendas.rowCount() > 0:
            self.ui.tabela_recebe_produto_vendas.removeRow(0)

            # Atualizando o valor e quantidade total dos itens restantes na tabela
            valor_total = 0.0
            qtdd_total = 0.0
            for row in range(self.ui.tabela_recebe_produto_vendas.rowCount()):
                item_qtdd = self.ui.tabela_recebe_produto_vendas.item(row, 1)
                item_valor = self.ui.tabela_recebe_produto_vendas.item(row, 2)
                if item_qtdd and item_qtdd.text():
                    item_valor_text = item_valor.text().replace('R$ ', '').replace(',', '.')
                    if item_valor_text:
                        valor_total += float(item_valor_text)
            qtdd = qtdd_total
            valor = valor_total

            # Definindo a localidade para 'pt_BR'
            locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

            # Formatando o valor de acordo com a localidade
            valor_formatado = locale.format_string('%.2f', valor, grouping=True)

            # Atualizando a label com o valor formatado
            self.ui.recebe_valor_total_vendas.setText(f"R$: {valor_formatado}")
            self.ui.recebe_peso_total_vendas.setText(f"{qtdd:.2f} kg")
        else:
            # Limpando as labels de valor e quantidade total
            self.ui.recebe_peso_total_vendas.setText("")
            self.ui.recebe_valor_total_vendas.setText("")

        self.ui.checkBox_SNF_vendas.setEnabled(True)
        self.ui.checkBox_NF_vendas.setEnabled(True)

        # Deletando os pedidos salvos em txt
        dir_path = 'C:\\Nexo\\Pedidos'
        with os.scandir(dir_path) as entries:
            for entry in entries:
                if entry.is_file():
                    os.remove(entry.path)

    def enviar_email(self):
        thread = Thread(target=self._enviar_email_thread)
        thread.start()

    def _enviar_email_thread(self):
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()

        # Obtém as informações de configuração do email das variáveis de ambiente
        smtp_host = os.getenv("SMTP_HOST")
        smtp_port = os.getenv("SMTP_PORT")
        email_login = os.getenv("EMAIL_LOGIN")
        email_password = os.getenv("EMAIL_PASSWORD")

        try:
            # Inicia o servidor SMTP
            server = SMTP(smtp_host, smtp_port)
            server.ehlo()
            server.starttls()
            server.login(email_login, email_password)

            # Constrói o email tipo MIME
            corpo = """
            <p>Olá, segue em anexo pedido de venda</p><br>
            <p>Att Tetraquimica Metal</p>
            """

            email_msg = MIMEMultipart()
            email_msg['From'] = email_login
            email_msg['To'] = ', '.join(["finan.tetra@gmail.com"])
            email_msg['Cc'] = ', '.join(["compras@tetraquimicametal.com.br"])
            email_msg['Subject'] = "Pedido de venda"
            email_msg.attach(MIMEText(corpo, 'html'))

            # Abre o arquivo em modo leitura binária
            cam_arquivo = f"{NEXO_DIRECTORY}\\Pedido_{self.obter_cliente}.txt"
            with open(cam_arquivo, 'rb') as attachment:
                # Lê o arquivo no modo binário e codifica em base64
                att = MIMEBase('application', 'octet-stream')
                att.set_payload(attachment.read())
                encoders.encode_base64(att)

                # Adiciona o cabeçalho no tipo anexo de email
                att.add_header('Content-Disposition', 'attachment', filename='pedido.txt')
                email_msg.attach(att)

            # Envia o email
            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
            server.quit()

            # Exibe uma notificação de sucesso
            toaster = ToastNotifier()
            toaster.show_toast("Notificação", "Pedido enviado por e-mail.", threaded=True, icon_path="footprint-dark.ico", duration=8)
        except Exception as e:
            # Exibe uma mensagem de erro
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Nexo")
            msg.setText("Não foi possível enviar seu pedido!")
            msg.setInformativeText("Verifique e tente novamente.")
            msg.setWindowIcon(QtGui.QIcon('icons\\footprint.ico'))
            msg.setWindowTitle("Aviso")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()

    def enviar_whatsapp(self):
        thread = Thread(target=self._enviar_whatsapp_thread)
        thread.start()

    def _enviar_whatsapp_thread(self):
        try:
            mensagem = open(f"{NEXO_DIRECTORY}\\Pedidos\\Pedido_{self.obter_cliente}.txt", "r", encoding="utf-8")
            leia = mensagem.read() 
            sendwhatmsg_instantly("+5517991022015", leia)
            toaster = ToastNotifier()
            toaster.show_toast("Notificação", "Pedido enviado por whatsapp.", threaded=True, icon_path="icons\\footprint.ico", duration=8)
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Nexo")
            msg.setText(f"não foi possivel enviar seu pedido!")
            msg.setInformativeText("Verefique e tente novamente.")
            msg.setWindowIcon(QtGui.QIcon('icons\\footprint.ico'))
            msg.setWindowTitle("Aviso")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()

    def baixar_pedido(self):
        try:
            arquivo = self.ui.comboBox_arquivos_vendas.currentText()
            pedido = (self.ui.insere_cliente.text())

            # Especificando o diretório inicial para o diálogo de seleção de diretório
            initial_dir = f"C:\\Users\\{os.getlogin()}\\Downloads"
            dest = QFileDialog.getExistingDirectory(caption='Selecione onde deseja salvar o pedido', directory=initial_dir)

            src = f'{NEXO_DIRECTORY}\\Pedido_{pedido}.txt'
            src2 = f'C:\\Users\\Public\\Documents\\fispqs\\{arquivo}'

            copyfile(src, dest+f"\Pedido_{pedido}.txt")
            copyfile(src2, dest+f"\{arquivo}")

            toaster = ToastNotifier()
            toaster.show_toast("Notificação", "Download concluído com sucesso!", threaded=True, icon_path="icons\\footprint.ico", duration=8)
        except:
            toaster = ToastNotifier()
            toaster.show_toast("Notificação", "Download concluído com sucesso!\nNenhum arquivo foi selecionado para download.", threaded=True, icon_path="icons\\footprint.ico", duration=5)

    def imprimir(self):
        try:
            filePath, filter = QFileDialog.getOpenFileName(self, 'Open file', '{NEXO_DIRECTORY}', 'Text (*.txt)')
            if not filePath:
                return
            doc = QtGui.QTextDocument()
            try:
                with open(filePath, 'r', encoding="utf-8") as txtFile:
                    doc.setPlainText(txtFile.read())
                printer = QtPrintSupport.QPrinter(QPrinter.PrinterMode.HighResolution)
                
                if not QtPrintSupport.QPrintDialog(printer, self).exec():
                    return
                doc.print(printer)
            except Exception as e:
                print('Error trying to print: {}'.format(e))

        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Nexo")
            msg.setText("Nenhum pedido encontrado!")
            msg.setWindowIcon(QtGui.QIcon('icons\\footprint.ico'))
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()

    def recebe_dados(self, tabela, campo, comboBox):
        banco = connect("system.db")
        cursor = banco.cursor()
        try:
            cursor.execute(f'SELECT {campo} FROM {tabela}')
            dados_lidos = sorted(cursor.fetchall())

            for row in dados_lidos:
                comboBox.addItems(row)
        finally:
            banco.close()

    def update_database(self):
        banco = connect("system.db")
        cursor = banco.cursor()
        cursor.execute('SELECT vendedores FROM vendedor ORDER BY vendedores')
        dados_lidos = cursor.fetchall()

        self.clearAllBox()
        
        self.recebe_dados(tabela='frete', campo='fretes', comboBox=self.ui.comboBox_frete_vendas)
        self.recebe_dados(tabela='transportadoras', campo='tranportadora', comboBox=self.ui.comboBox_transport_vendas)
        self.recebe_dados(tabela='produtos', campo='produto', comboBox=self.ui.comboBox_produto_vendas)
        self.recebe_dados(tabela='prazos', campo='prazo', comboBox=self.ui.comboBox_prazo_vendas)

        itens = [row[0] for row in dados_lidos]
        self.ui.comboBox_vendedor_vendas.addItems(itens)

        banco.close()
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Nexo")
        msg.setText("Dados atualizados com sucesso")
        msg.setWindowIcon(QtGui.QIcon('icons\\footprint.ico'))
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def clearAllBox(self):
        self.ui.comboBox_vendedor_vendas.clear()
        self.ui.comboBox_frete_vendas.clear()
        self.ui.comboBox_transport_vendas.clear()
        self.ui.comboBox_produto_vendas.clear()
        self.ui.comboBox_prazo_vendas.clear()
        self.ui.comboBox_embalagem_vendas.clear()
        self.ui.comboBox_unidade_vendas.clear()

    def calcular_frete(self):
        try:
            # Remover linhas de tabela_recebe_produto_2
            for _ in range(8):
                try:
                    self.ui.tabela_recebe_produto_2.removeRow(0)
                except:
                    pass

            # Calcular valor do frete com base na quantidade
            global valor
            global qtdd
            
            valor_total_nota = valor
            quantidade = qtdd
            
            # Lista de tuplas com limites de quantidade e valores correspondentes de frete_valor
            limites_quantidade = [(0, 0), (20, 78.00), (70, 89.00), (100, 105.00), (150, 126.00), (200, 150.00), (250, 182.00), (300, 209.00)]
            
            # Determinar o valor de frete_valor com base na quantidade
            frete_valor = next((valor for limite, valor in limites_quantidade if quantidade <= limite), 240.00)

            # Calcular pedágio e despacho
            pedagio = 0.09 * quantidade
            despacho = 25
            
            # Calcular resultado SDS
            soma0 = (ceil(valor_total_nota * 0.7 / 100))
            soma1 = soma0 + pedagio
            soma2 = soma1 + despacho + frete_valor
            
            valor_total_frete = f"R$ {soma2:.2f}"
            self.ui.tabela_recebe_produto_2.setRowCount(len(self.obter_produto))
            self.ui.tabela_recebe_produto_2.setItem(0, 0, QtWidgets.QTableWidgetItem("SDS"))
            self.ui.tabela_recebe_produto_2.setItem(0, 1, QtWidgets.QTableWidgetItem(valor_total_frete))

            # Calcular resultado ALFA
            soma9 = (ceil(valor_total_nota * 0.7 / 100))
            soma10 = soma9 + pedagio
            soma11 = soma10 + despacho + frete_valor
            result_alfa = soma11 + (ceil(soma11 * 110 / 100))
            valor_total_frete = f"R$ {result_alfa:.2f}"

            self.ui.tabela_recebe_produto_2.setItem(0, 6, QtWidgets.QTableWidgetItem("ALFA"))
            self.ui.tabela_recebe_produto_2.setItem(0, 7, QtWidgets.QTableWidgetItem(valor_total_frete))

            # Calcular resultado IRACEMA
            custo_kg_iracema = frete_valor

            # Lista de tuplas com limites de quantidade e valores correspondentes de frete_valor para IRACEMA
            limites_quantidade_iracema = [(0, 0), (50, 22.38), (75, 25.10), (100, 27.82), (9999, 150.00), (20000, 413.50)]
            
            # Determinar o valor de frete_valor para IRACEMA com base na quantidade
            frete_valor_iracema = next((valor for limite, valor in limites_quantidade_iracema if quantidade <= limite), 240.00)
            
            depedata = 60
            gris = (ceil(custo_kg_iracema * 0.3 / 100))
            advl = (ceil(custo_kg_iracema * 0.3 / 100))

            iracema = frete_valor_iracema + gris + advl + depedata
            valor_total_frete_iracema = f"R$ {iracema:.2f}"

            self.ui.tabela_recebe_produto_2.setItem(0, 4, QtWidgets.QTableWidgetItem("IRACEMA"))
            self.ui.tabela_recebe_produto_2.setItem(0, 5, QtWidgets.QTableWidgetItem(valor_total_frete_iracema))

            # Calcular resultado BARONI
            custo_por_kg = frete_valor

            # Lista de tuplas com limites de quantidade e valores correspondentes de frete_valor para BARONI
            limites_quantidade_baroni = [(0, 0), (50, 43.00), (100, 49.00), (150, 68.00), (200, 73.00), (300, 85.00), (999999, 209.00)]
            
            # Determinar o valor de frete_valor para BARONI com base na quantidade
            frete_valor_baroni = next((valor for limite, valor in limites_quantidade_baroni if quantidade <= limite), 240.00)
            
            baroni = frete_valor_baroni + 60
            valor_total_frete_baroni = f"R$ {baroni:.2f}"

            self.ui.tabela_recebe_produto_2.setItem(0, 2, QtWidgets.QTableWidgetItem("BARONI"))
            self.ui.tabela_recebe_produto_2.setItem(0, 3, QtWidgets.QTableWidgetItem(valor_total_frete_baroni))
        except:
            pass

    def lembretes(self):
        # Armazena os lembretes em uma lista
        lembretes = [
            self.ui.primeiro_lembrete.toPlainText(),
        ]

        # Salva os lembretes nos arquivos correspondentes
        try:
            for i, lembrete in enumerate(lembretes):
                with open(f"{NEXO_DIRECTORY}\\Lembretes\\lembrete{i + 1}.txt", "w") as arq:
                    arq.write(lembrete)

            toaster = ToastNotifier()
            toaster.show_toast("Notificação", "Lembrete gravado com sucesso.", threaded=True, icon_path="icons\\footprint.ico", duration=5)
        except Exception as e:
            print(f"Ocorreu um erro ao salvar os lembretes: {e}")

    def insertLembrete(self):
        # Verifica se o diretório existe e cria-o se não existir
        directory = f"{NEXO_DIRECTORY}\\Lembretes"
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Lista de codificações comuns para tentar ler os arquivos
        encodings = ["utf-8", "latin-1", "cp1252"]
        conteudos = ["", "", "", ""]
        
        # Lê os lembretes dos arquivos correspondentes
        for i in range(4):
            file_path = f"{directory}\\lembrete{i + 1}.txt"
            if os.path.exists(file_path):
                for encoding in encodings:
                    try:
                        with open(file_path, "r", encoding=encoding) as arq:
                            conteudos[i] = arq.read()
                        break
                    except UnicodeDecodeError:
                        pass
                else:
                    print(f"Ocorreu um erro ao carregar o lembrete {i + 1}: não foi possível decodificar o arquivo com nenhuma das codificações testadas")
            else:
                print(f"O arquivo {file_path} não foi encontrado. Ignorando a leitura do lembrete {i + 1}.")

        # Atualiza a interface do usuário com os lembretes carregados
        self.ui.primeiro_lembrete.setPlainText(conteudos[0])
            
#APLICAÇÃO
if __name__ == "__main__":
    start_time = time()
    app = QApplication(argv)
    Window = LOGIN()
    Window.show()
    end_time = time()
    #print(f"Tempo para abrir a tela de login: {end_time - start_time} segundos")
    app.exec()