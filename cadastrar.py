# Arquivo cadastrar.py
from sqlite3 import connect
from telaCadastro import Ui_Form
from PyQt6.QtWidgets import QMainWindow

class CADASTRAR(QMainWindow, Ui_Form):
    def __init__(self) -> None:
        super(CADASTRAR, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.botao_gravar_cadastro.clicked.connect(self.salvar_dados_cliente)

    def salvar_dados_cliente(self):
        # Conecte-se ao banco de dados
        conn = connect('clientes.db')
        c = conn.cursor()

        # Crie a tabela clientes se não existir
        c.execute('''CREATE TABLE IF NOT EXISTS clientes
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      razao_social TEXT,
                      nome_fantasia TEXT,
                      vendedor TEXT,
                      prazo_pagamento TEXT,
                      transportadora TEXT,
                      endereco_comercial TEXT,
                      cod_ibge TEXT,
                      numero TEXT,
                      complemento TEXT,
                      bairro TEXT,
                      cidade TEXT,
                      uf TEXT,
                      cep TEXT,
                      cnpj_cpf TEXT,
                      inscricao_estadual TEXT,
                      telefone1 TEXT,
                      telefone2 TEXT,
                      pais TEXT,
                      email TEXT,
                      endereco_entrega TEXT,
                      numero_entrega TEXT,
                      complemento_entrega TEXT,
                      bairro_entrega TEXT,
                      cidade_entrega TEXT,
                      uf_entrega TEXT,
                      cep_entrega TEXT,
                      pais_entrega TEXT)''')

        # Crie a tabela fornecedores se não existir
        c.execute('''CREATE TABLE IF NOT EXISTS fornecedores
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      razao_social TEXT,
                      nome_fantasia TEXT,
                      vendedor TEXT,
                      prazo_pagamento TEXT,
                      transportadora TEXT,
                      endereco_comercial TEXT,
                      cod_ibge TEXT,
                      numero TEXT,
                      complemento TEXT,
                      bairro TEXT,
                      cidade TEXT,
                      uf TEXT,
                      cep TEXT,
                      cnpj_cpf TEXT,
                      inscricao_estadual TEXT,
                      telefone1 TEXT,
                      telefone2 TEXT,
                      pais TEXT,
                      email TEXT,
                      endereco_entrega TEXT,
                      numero_entrega TEXT,
                      complemento_entrega TEXT,
                      bairro_entrega TEXT,
                      cidade_entrega TEXT,
                      uf_entrega TEXT,
                      cep_entrega TEXT,
                      pais_entrega TEXT)''')

        # Colete os valores inseridos pelo usuário
        razao_social = self.ui.insere_razao_social.text()
        nome_fantasia = self.ui.insere_nome_fantasia.text()
        vendedor = self.ui.comboBox_vendedor_cadastro.currentText()
        prazo_pagamento = self.ui.comboBox_prazo_cadastro.currentText()
        transportadora = self.ui.comboBox_transport_cadastro.currentText()
        endereco_comercial = self.ui.insere_endereco_comercial.text()
        cod_ibge = self.ui.insere_Cod_IBGE.text()
        numero = self.ui.insere_numero.text()
        complemento = self.ui.insere_complemento.text()
        bairro = self.ui.insere_bairro.text()
        cidade = self.ui.insere_cidade.text()
        uf = self.ui.insere_UF.text()
        cep = self.ui.insere_CEP.text()
        cnpj_cpf = self.ui.insere_cnpj_cpf.text()
        inscricao_estadual = self.ui.insere_inscricao_estadual.text()
        telefone1 = self.ui.insere_telefone1.text()
        telefone2 = self.ui.insere_telefone2.text()
        pais = self.ui.insere_pais.text()
        email = self.ui.insere_email.text()
        endereco_entrega = self.ui.insere_endereco_entrega.text()
        numero_entrega = self.ui.insere_numero_entrega.text()
        complemento_entrega = self.ui.insere_complemento_entrega.text()
        bairro_entrega = self.ui.insere_bairro_entrega.text()
        cidade_entrega = self.ui.insere_cidade_entrega.text()
        uf_entrega = self.ui.insere_UF_entrega.text()
        cep_entrega = self.ui.insere_CEP_entrega.text()
        pais_entrega = self.ui.insere_pais_entrega.text()

        if self.ui.checkBox_cliente.isChecked():
            # Salve os dados na tabela clientes
            c.execute('''INSERT INTO clientes (razao_social, nome_fantasia, vendedor, prazo_pagamento, transportadora,
                         endereco_comercial, cod_ibge, numero, complemento, bairro, cidade, uf, cep, cnpj_cpf,
                         inscricao_estadual, telefone1, telefone2, pais, email, endereco_entrega, numero_entrega,
                         complemento_entrega, bairro_entrega, cidade_entrega, uf_entrega, cep_entrega, pais_entrega)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                         (razao_social, nome_fantasia, vendedor, prazo_pagamento, transportadora, endereco_comercial,
                          cod_ibge, numero, complemento, bairro, cidade, uf, cep, cnpj_cpf, inscricao_estadual,
                          telefone1, telefone2, pais, email, endereco_entrega, numero_entrega, complemento_entrega,
                          bairro_entrega, cidade_entrega, uf_entrega, cep_entrega, pais_entrega))
        
        elif self.ui.checkBox_fornecedor.isChecked():
            # Salve os dados na tabela fornecedores
            c.execute('''INSERT INTO fornecedores (razao_social, nome_fantasia, vendedor, prazo_pagamento, transportadora,
                         endereco_comercial, cod_ibge, numero, complemento, bairro, cidade, uf, cep, cnpj_cpf,
                         inscricao_estadual, telefone1, telefone2, pais, email, endereco_entrega, numero_entrega,
                         complemento_entrega, bairro_entrega, cidade_entrega, uf_entrega, cep_entrega, pais_entrega)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                         (razao_social, nome_fantasia, vendedor, prazo_pagamento, transportadora, endereco_comercial,
                          cod_ibge, numero, complemento, bairro, cidade, uf, cep, cnpj_cpf, inscricao_estadual,
                          telefone1, telefone2, pais, email, endereco_entrega, numero_entrega, complemento_entrega,
                          bairro_entrega, cidade_entrega, uf_entrega, cep_entrega, pais_entrega))
        
        if self.ui.checkBox_transportadora.isChecked():
            # Salve os dados na tabela transportadora
            c.execute("INSERT INTO transportadora (razao_social, nome_fantasia, vendedor, prazo_pagamento, transportadora, endereco_comercial, cod_ibge, numero, complemento, bairro, cidade, uf, cep, cnpj_cpf, inscricao_estadual, telefone1, telefone2, pais, email, endereco_entrega, numero_entrega, complemento_entrega, bairro_entrega, cidade_entrega, uf_entrega, cep_entrega, pais_entrega) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (razao_social, nome_fantasia, vendedor, prazo_pagamento, 'Transportadora', endereco_comercial, cod_ibge, numero, complemento, bairro, cidade, uf, cep, cnpj_cpf, inscricao_estadual, telefone1, telefone2, pais, email, endereco_entrega, numero_entrega, complemento_entrega, bairro_entrega, cidade_entrega, uf_entrega, cep_entrega, pais_entrega))
        else:
            # Salve os dados na tabela clientes
            c.execute("INSERT INTO clientes (razao_social, nome_fantasia, vendedor, prazo_pagamento, transportadora, endereco_comercial, cod_ibge, numero, complemento, bairro, cidade, uf, cep, cnpj_cpf, inscricao_estadual, telefone1, telefone2, pais, email, endereco_entrega, numero_entrega, complemento_entrega, bairro_entrega, cidade_entrega, uf_entrega, cep_entrega, pais_entrega) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (razao_social, nome_fantasia, vendedor, prazo_pagamento, '', endereco_comercial, cod_ibge, numero, complemento, bairro, cidade, uf, cep, cnpj_cpf, inscricao_estadual, telefone1, telefone2, pais, email, endereco_entrega, numero_entrega, complemento_entrega, bairro_entrega, cidade_entrega, uf_entrega, cep_entrega, pais_entrega))


        # Salve as alterações e feche a conexão com o banco de dados
        conn.commit()
        conn.close()
