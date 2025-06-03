# LanchoneteBD

CREATE DATABASE lanchonete;

USE lanchonete;

CREATE TABLE IF NOT EXISTS Pessoa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    celular VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Cliente (
    rg VARCHAR(20) PRIMARY KEY,
    id_pessoa INT NOT NULL,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Funcionario (
    rg VARCHAR(20) PRIMARY KEY,
    cargo VARCHAR(50) NOT NULL,
    id_pessoa INT NOT NULL,
    supervisor_rg VARCHAR(20) NULL,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id) ON DELETE CASCADE,
    FOREIGN KEY (supervisor_rg) REFERENCES Funcionario(rg) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Dependente (
    id INT AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    parentesco VARCHAR(50),
    funcionario_rg VARCHAR(20) NOT NULL,
    PRIMARY KEY (id, funcionario_rg),
    FOREIGN KEY (funcionario_rg) REFERENCES Funcionario(rg) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Fornecedor (
    cnpj VARCHAR(20) PRIMARY KEY,
    id_pessoa INT NOT NULL,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS Produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2) NOT NULL,
    id_fornecedor VARCHAR(20),
    FOREIGN KEY (id_fornecedor) REFERENCES Fornecedor(cnpj)
);

CREATE TABLE IF NOT EXISTS ProdutoCategoria (
    id_produto INT,
    id_categoria INT,
    PRIMARY KEY (id_produto, id_categoria),
    FOREIGN KEY (id_produto) REFERENCES Produto(id) ON DELETE CASCADE,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_cliente VARCHAR(20) NOT NULL,
    id_funcionario VARCHAR(20) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(rg),
    FOREIGN KEY (id_funcionario) REFERENCES Funcionario(rg)
);

CREATE TABLE IF NOT EXISTS ItemPedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL DEFAULT 1,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id) ON DELETE CASCADE,
    FOREIGN KEY (id_produto) REFERENCES Produto(id)
);

CREATE TABLE IF NOT EXISTS Caixa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT UNIQUE,
    valor_a_receber DECIMAL(10, 2),
    valor_a_pagar DECIMAL(10, 2),
    id_cliente VARCHAR(20),
    id_fornecedor VARCHAR(20),
    data_operacao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(rg),
    FOREIGN KEY (id_fornecedor) REFERENCES Fornecedor(cnpj)
);

CREATE INDEX idx_pessoa_nome ON Pessoa(nome);
CREATE INDEX idx_pedido_data ON Pedido(data);
CREATE INDEX idx_caixa_data ON Caixa(data_operacao);
CREATE INDEX idx_funcionario_supervisor ON Funcionario(supervisor_rg);
CREATE INDEX idx_dependente_funcionario ON Dependente(funcionario_rg);

ALTER TABLE Pessoa COMMENT 'Armazena dados básicos de todas as pessoas relacionadas à lanchonete';
ALTER TABLE Cliente COMMENT 'Armazena dados específicos dos clientes da lanchonete';
ALTER TABLE Funcionario COMMENT 'Armazena dados específicos dos funcionários da lanchonete, incluindo auto-relacionamento de supervisão';
ALTER TABLE Dependente COMMENT 'Entidade fraca que representa dependentes de funcionários';
ALTER TABLE Fornecedor COMMENT 'Armazena dados específicos dos fornecedores da lanchonete';
ALTER TABLE Categoria COMMENT 'Categorias de produtos disponíveis';
ALTER TABLE Produto COMMENT 'Armazena informações sobre os produtos disponíveis na lanchonete';
ALTER TABLE ProdutoCategoria COMMENT 'Relacionamento muitos-para-muitos entre produtos e categorias';
ALTER TABLE Pedido COMMENT 'Registra os pedidos realizados pelos clientes';
ALTER TABLE ItemPedido COMMENT 'Detalha os itens incluídos em cada pedido';
ALTER TABLE Caixa COMMENT 'Registra as operações financeiras da lanchonete';

INSERT INTO Pessoa (nome, celular) VALUES 
('João Silva', '(14) 99999-1111'),
('Maria Oliveira', '(14) 99999-2222'),
('Pedro Santos', '(14) 99999-3333'),
('Ana Costa', '(14) 99999-4444'),
('Carlos Ferreira', '(14) 99999-5555'),
('Lucia Pereira', '(14) 99999-6666'),
('Roberto Almeida', '(14) 99999-7777'),
('Fernanda Lima', '(14) 99999-8888'),
('Ricardo Souza', '(14) 99999-9999'),
('Juliana Martins', '(14) 99999-0000');

INSERT INTO Cliente (rg, id_pessoa) VALUES 
('12345678-9', 1),
('23456789-0', 2),
('34567890-1', 3);

INSERT INTO Funcionario (rg, cargo, id_pessoa, supervisor_rg) VALUES 
('45678901-2', 'Gerente', 4, NULL),
('56789012-3', 'Atendente', 5, '45678901-2'),
('67890123-4', 'Cozinheiro', 6, '45678901-2'),
('78901234-5', 'Caixa', 7, '45678901-2');

INSERT INTO Dependente (nome, data_nascimento, parentesco, funcionario_rg) VALUES 
('Miguel Silva', '2010-05-15', 'Filho', '45678901-2'),
('Sofia Oliveira', '2012-08-20', 'Filha', '45678901-2'),
('Lucas Ferreira', '2015-03-10', 'Filho', '56789012-3'),
('Julia Pereira', '2018-11-25', 'Filha', '67890123-4');

INSERT INTO Fornecedor (cnpj, id_pessoa) VALUES 
('12.345.678/0001-90', 8),
('23.456.789/0001-01', 9),
('34.567.890/0001-12', 10);

INSERT INTO Categoria (nome, descricao) VALUES 
('Lanches', 'Sanduíches, hambúrgueres e outros lanches rápidos'),
('Bebidas', 'Refrigerantes, sucos e outras bebidas'),
('Sobremesas', 'Doces, bolos e outras sobremesas'),
('Combos', 'Combinações de lanches, bebidas e acompanhamentos');

INSERT INTO Produto (nome, descricao, preco, id_fornecedor) VALUES 
('Hambúrguer Simples', 'Pão, carne, alface, tomate e maionese', 15.90, '12.345.678/0001-90'),
('Hambúrguer Duplo', 'Pão, duas carnes, queijo, alface, tomate e maionese', 22.90, '12.345.678/0001-90'),
('Refrigerante Cola', 'Refrigerante sabor cola 350ml', 5.50, '23.456.789/0001-01'),
('Suco de Laranja', 'Suco natural de laranja 300ml', 7.90, '23.456.789/0001-01'),
('Batata Frita', 'Porção de batata frita crocante', 9.90, '12.345.678/0001-90'),
('Sorvete', 'Sorvete de creme com calda de chocolate', 8.50, '34.567.890/0001-12'),
('Combo 1', 'Hambúrguer simples, batata frita e refrigerante', 25.90, NULL),
('Combo 2', 'Hambúrguer duplo, batata frita e refrigerante', 32.90, NULL);

INSERT INTO ProdutoCategoria (id_produto, id_categoria) VALUES 
(1, 1), -- Hambúrguer Simples é um Lanche
(2, 1), -- Hambúrguer Duplo é um Lanche
(3, 2), -- Refrigerante Cola é uma Bebida
(4, 2), -- Suco de Laranja é uma Bebida
(5, 1), -- Batata Frita é um Lanche
(6, 3), -- Sorvete é uma Sobremesa
(7, 4), -- Combo 1 é um Combo
(7, 1), -- Combo 1 também é considerado Lanche
(8, 4), -- Combo 2 é um Combo
(8, 1); -- Combo 2 também é considerado Lanche

INSERT INTO Pedido (data, id_cliente, id_funcionario) VALUES 
('2025-05-25 12:30:00', '12345678-9', '56789012-3'),
('2025-05-25 13:45:00', '23456789-0', '56789012-3'),
('2025-05-26 19:20:00', '34567890-1', '56789012-3'),
('2025-05-27 20:15:00', '12345678-9', '56789012-3');

INSERT INTO ItemPedido (id_pedido, id_produto, quantidade, preco_unitario) VALUES 
(1, 1, 2, 15.90), -- 2 Hambúrgueres Simples
(1, 3, 2, 5.50),  -- 2 Refrigerantes Cola
(1, 5, 1, 9.90),  -- 1 Batata Frita
(2, 7, 1, 25.90), -- 1 Combo 1
(3, 2, 1, 22.90), -- 1 Hambúrguer Duplo
(3, 4, 1, 7.90),  -- 1 Suco de Laranja
(3, 6, 1, 8.50),  -- 1 Sorvete
(4, 8, 2, 32.90); -- 2 Combos 2

INSERT INTO Caixa (id_pedido, valor_a_receber, valor_a_pagar, id_cliente, id_fornecedor, data_operacao) VALUES 
(1, 52.70, NULL, '12345678-9', NULL, '2025-05-25 12:45:00'),
(2, 25.90, NULL, '23456789-0', NULL, '2025-05-25 14:00:00'),
(3, 39.30, NULL, '34567890-1', NULL, '2025-05-26 19:35:00'),
(4, 65.80, NULL, '12345678-9', NULL, '2025-05-27 20:30:00'),
(NULL, NULL, 1500.00, NULL, '12.345.678/0001-90', '2025-05-28 10:00:00'),
(NULL, NULL, 800.00, NULL, '23.456.789/0001-01', '2025-05-28 11:30:00');

SELECT p.nome, p.celular, c.rg
FROM pessoa p
JOIN cliente c ON p.id = c.id_pessoa
WHERE p.nome LIKE '%Silva%'
ORDER BY p.nome;

SELECT p.nome AS cliente, COUNT(pe.id) AS total_pedidos, 
       SUM(ip.quantidade * ip.preco_unitario) AS valor_total
FROM pessoa p
INNER JOIN cliente c ON p.id = c.id_pessoa
INNER JOIN pedido pe ON c.rg = pe.id_cliente
INNER JOIN item_pedido ip ON pe.id = ip.id_pedido
GROUP BY p.nome
ORDER BY valor_total DESC;

SELECT c.nome AS categoria, p.nome AS produto, p.preco
FROM categoria c
LEFT JOIN produto_categoria pc ON c.id = pc.id_categoria
LEFT JOIN produto p ON pc.id_produto = p.id
ORDER BY c.nome, p.nome;

SELECT p.nome AS fornecedor, pr.nome AS produto, pr.preco
FROM produto pr
RIGHT JOIN fornecedor f ON pr.id_fornecedor = f.cnpj
RIGHT JOIN pessoa p ON f.id_pessoa = p.id
ORDER BY p.nome, pr.nome;

SELECT p.nome AS funcionario, f.cargo, 
       COUNT(pe.id) AS total_pedidos,
       SUM(ip.quantidade * ip.preco_unitario) AS valor_total
FROM pessoa p
JOIN funcionario f ON p.id = f.id_pessoa
JOIN pedido pe ON f.rg = pe.id_funcionario
JOIN item_pedido ip ON pe.id = ip.id_pedido
GROUP BY p.nome, f.cargo
HAVING COUNT(pe.id) > 0
ORDER BY valor_total DESC;

SELECT p.nome AS funcionario, f.cargo, 
       s.nome AS supervisor,
       COUNT(d.id) AS total_dependentes
FROM pessoa p
JOIN funcionario f ON p.id = f.id_pessoa
LEFT JOIN funcionario sup ON f.supervisor_rg = sup.rg
LEFT JOIN pessoa s ON sup.id_pessoa = s.id
LEFT JOIN dependente d ON f.rg = d.funcionario_rg
GROUP BY p.nome, f.cargo, s.nome
ORDER BY p.nome;

SELECT p.nome AS produto, p.preco, c.nome AS categoria
FROM produto p
LEFT JOIN item_pedido ip ON p.id = ip.id_produto
LEFT JOIN produto_categoria pc ON p.id = pc.id_produto
LEFT JOIN categoria c ON pc.id_categoria = c.id
WHERE ip.id IS NULL
ORDER BY p.nome;

SELECT 'Recebimentos' AS tipo, SUM(valor_a_receber) AS valor
FROM caixa
WHERE valor_a_receber IS NOT NULL
UNION
SELECT 'Pagamentos' AS tipo, SUM(valor_a_pagar) AS valor
FROM caixa
WHERE valor_a_pagar IS NOT NULL
ORDER BY tipo;

SHOW TABLES;

DESCRIBE Pessoa;
DESCRIBE Funcionario;
DESCRIBE Dependente;
DESCRIBE ProdutoCategoria;

SHOW CREATE TABLE Funcionario;
SHOW CREATE TABLE Dependente;
SHOW CREATE TABLE ProdutoCategoria;

SELECT * FROM Pessoa;
SELECT * FROM Funcionario;
SELECT * FROM Dependente;
SELECT * FROM Produto;
SELECT * FROM ProdutoCategoria;
