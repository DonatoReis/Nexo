import sqlite3

# Conectar-se ao banco de dados SQLite
conn = sqlite3.connect('meu_banco_de_dados.db')
cursor = conn.cursor()

# Criar a tabela Portador
cursor.execute('''
 CREATE TABLE IF NOT EXISTS Portador (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL
 )
''')

# Criar a tabela Cliente
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        razao_social TEXT NOT NULL,
        nome_fantasia TEXT,
        endereco_comercial TEXT NOT NULL,
        numero TEXT NOT NULL,
        complemento TEXT,
        bairro TEXT NOT NULL,
        cidade TEXT NOT NULL,
        uf TEXT NOT NULL,
        cep TEXT NOT NULL,
        cpf_cnpj TEXT NOT NULL,
        inscricao_estadual TEXT,
        telefone1 TEXT,
        telefone2 TEXT,
        pais TEXT NOT NULL,
        email TEXT NOT NULL,
        inscricao_municipal TEXT,
        observacao TEXT,
        ramo_atividade TEXT NOT NULL,
        condicao_pagamento_id INTEGER NOT NULL,
        vendedor_id INTEGER NOT NULL,
        portador_id INTEGER NOT NULL,
        transportadora_id INTEGER NOT NULL,
        data_criacao TEXT NOT NULL,
        FOREIGN KEY (condicao_pagamento_id) REFERENCES CondicaoPagamento (id),
        FOREIGN KEY (vendedor_id) REFERENCES Vendedor (id),
        FOREIGN KEY (portador_id) REFERENCES Portador (id),
        FOREIGN KEY (transportadora_id) REFERENCES Transportadora (id)
    )
''')

# Criar a tabela Fornecedor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Fornecedor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        razao_social TEXT NOT NULL,
        nome_fantasia TEXT,
        endereco_comercial TEXT NOT NULL,
        numero TEXT NOT NULL,
        complemento TEXT,
        bairro TEXT NOT NULL,
        cidade TEXT NOT NULL,
        uf TEXT NOT NULL,
        cep TEXT NOT NULL,
        cnpj TEXT NOT NULL,
        inscricao_estadual TEXT,
        telefone1 TEXT,
        telefone2 TEXT,
        pais TEXT NOT NULL,
        email TEXT NOT NULL,
        inscricao_municipal TEXT,
        observacao TEXT,
        ramo_atividade TEXT NOT NULL,
        condicao_pagamento_id INTEGER NOT NULL,
        vendedor_id INTEGER NOT NULL,
        portador_id INTEGER NOT NULL,
        transportadora_id INTEGER NOT NULL,
        data_criacao TEXT NOT NULL,
        FOREIGN KEY (condicao_pagamento_id) REFERENCES CondicaoPagamento (id),
        FOREIGN KEY (vendedor_id) REFERENCES Vendedor (id),
        FOREIGN KEY (portador_id) REFERENCES Portador (id),
        FOREIGN KEY (transportadora_id) REFERENCES Transportadora (id)
    )
''')

# Criar a tabela Embalagem
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Embalagem (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL
    )
''')

# Criar a tabela Unidade
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Unidade (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL
    )
''')

# Criar a tabela Produto
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco REAL NOT NULL,
        embalagem_id INTEGER,
        unidade_id INTEGER,
        FOREIGN KEY (embalagem_id) REFERENCES Embalagem (id),
        FOREIGN KEY (unidade_id) REFERENCES Unidade (id)
    )
''')

# Criar a tabela Vendedor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vendedor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        endereco TEXT NOT NULL
    )
''')

# Criar a tabela CondicaoPagamento
cursor.execute('''
    CREATE TABLE IF NOT EXISTS CondicaoPagamento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        parcelas INTEGER NOT NULL,
        dias_entre_parcelas INTEGER NOT NULL
    )
''')

# Criar a tabela Transportadora
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transportadora (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        razao_social TEXT NOT NULL,
        nome_fantasia TEXT,
        endereco_comercial TEXT NOT NULL,
        numero TEXT NOT NULL,
        complemento TEXT,
        bairro TEXT NOT NULL,
        cidade TEXT NOT NULL,
        uf TEXT NOT NULL,
        cep TEXT NOT NULL,
        cnpj TEXT NOT NULL,
        inscricao_estadual TEXT,
        telefone1 TEXT,
        telefone2 TEXT,
        pais TEXT NOT NULL,
        email TEXT NOT NULL,
        inscricao_municipal TEXT,
        observacao TEXT, 
        ramo_atividade TEXT NOT NULL,
        condicao_pagamento_id INTEGER NOT NULL,
        vendedor_id INTEGER NOT NULL,
        portador_id INTEGER NOT NULL,
        data_criacao TEXT NOT NULL,
        FOREIGN KEY (condicao_pagamento_id) REFERENCES CondicaoPagamento (id),
        FOREIGN KEY (vendedor_id) REFERENCES Vendedor (id),
        FOREIGN KEY (portador_id) REFERENCES Portador (id)
    )
''')

# Criar a tabela PedidoVenda
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PedidoVenda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INTEGER NOT NULL,
        data TEXT NOT NULL,
        cliente_id INTEGER NOT NULL,
        vendedor_id INTEGER NOT NULL,
        condicao_pagamento_id INTEGER NOT NULL,
        transportadora_id INTEGER,
        FOREIGN KEY (cliente_id) REFERENCES Cliente (id),
        FOREIGN KEY (vendedor_id) REFERENCES Vendedor (id),
        FOREIGN KEY (condicao_pagamento_id) REFERENCES CondicaoPagamento (id),
        FOREIGN KEY (transportadora_id) REFERENCES Transportadora (id)
    )
''')

# Criar a tabela ItemPedidoVenda
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ItemPedidoVenda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL,
        produto_id INTEGER NOT NULL,
        pedido_venda_id INTEGER NOT NULL,
        FOREIGN KEY (produto_id) REFERENCES Produto (id),
        FOREIGN KEY (pedido_venda_id) REFERENCES PedidoVenda (id)
    )
''')

# Criar a tabela PedidoCompra
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PedidoCompra (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INTEGER NOT NULL,
        data TEXT NOT NULL,
        fornecedor_id INTEGER NOT NULL,
        condicao_pagamento_id INTEGER NOT NULL,
        transportadora_id INTEGER,
        FOREIGN KEY (fornecedor_id) REFERENCES Fornecedor (id),
        FOREIGN KEY (condicao_pagamento_id) REFERENCES CondicaoPagamento (id),
        FOREIGN KEY (transportadora_id) REFERENCES Transportadora (id)
    )
''')

# Criar a tabela ItemPedidoCompra
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ItemPedidoCompra (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL,
        produto_id INTEGER NOT NULL,
        pedido_compra_id INTEGER NOT NULL,
        FOREIGN KEY (produto_id) REFERENCES Produto (id),
        FOREIGN KEY (pedido_compra_id) REFERENCES PedidoCompra (id)
    )
''')

# Fechar a conexão com o banco de dados
conn.commit()
conn.close()
