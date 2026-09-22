-- Active: 1788267997462@@127.0.0.1@3306@smartcoffee_dml_bruno
-- SMARTCOFFEE BASE DE DADOS - DML 
-- EXECUTE SEMPRE QUE QUISER RESTAURAR A AULA

DROP DATABASE IF EXISTS SMARTCOFFEE_DML_BRUNO;
CREATE DATABASE SMARTCOFFEE_DML_BRUNO;
USE SMARTCOFFEE_DML_BRUNO;

-- TABELAS
CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE,
    telefone VARCHAR(20),
    cidade VARCHAR(60) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE categoria (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE produto (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    id_categoria INT NOT NULL,
    CONSTRAINT fk_produto_categoria FOREIGN KEY (id_categoria)
        REFERENCES categoria(id_categoria)
);

CREATE TABLE pedido (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    data_pedido DATETIME NOT NULL,
    status ENUM('ABERTO','PREPARANDO','FINALIZADO','CANCELADO') NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    id_cliente INT NOT NULL,
    CONSTRAINT fk_pedido_cliente FOREIGN KEY (id_cliente)
        REFERENCES cliente(id_cliente)
);

CREATE TABLE item_pedido (
    id_item INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    observacao VARCHAR(150),
    CONSTRAINT fk_item_pedido FOREIGN KEY (id_pedido)
        REFERENCES pedido(id_pedido),
    CONSTRAINT fk_item_produto FOREIGN KEY (id_produto)
        REFERENCES produto(id_produto)
);

CREATE TABLE forma_pagamento (
    id_forma_pagamento INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE pagamento (
    id_pagamento INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_forma_pagamento INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    data_pagamento DATETIME,
    CONSTRAINT fk_pagamento_pedido FOREIGN KEY (id_pedido)
        REFERENCES pedido(id_pedido),
    CONSTRAINT fk_pagamento_forma FOREIGN KEY (id_forma_pagamento)
        REFERENCES forma_pagamento(id_forma_pagamento)
);

-- DADOS INICIAIS
INSERT INTO cliente (nome, email, telefone, cidade, ativo) VALUES
('Ana Silva', 'ana@email.com', '19999990001', 'Limeira', TRUE),
('Bruno Souza', 'bruno@email.com', '19999990002', 'Limeira', TRUE),
('Carla Mendes', 'carla@email.com', NULL, 'Americana', TRUE),
('Diego Santos', 'diego@email.com', '19999990004', 'Campinas', TRUE),
('Elisa Rocha', 'elisa@email.com', NULL, 'Limeira', TRUE),
('Felipe Lima', 'felipe@email.com', '19999990006', 'Americana', TRUE),
('Gabriela Alves', 'gabriela@email.com', '19999990007', 'Piracicaba', TRUE),
('Henrique Costa', 'henrique@email.com', NULL, 'Limeira', FALSE),
('Isabela Martins', 'isabela@email.com', '19999990009', 'Campinas', TRUE),
('João Pereira', 'joao@email.com', '19999990010', 'Limeira', TRUE);

INSERT INTO categoria (nome) VALUES
('Cafés'), ('Bebidas Geladas'), ('Doces'), ('Salgados'), ('Combos');

SELECT * FROM categoria

INSERT INTO produto (nome, preco, ativo, id_categoria) VALUES
('Café Espresso', 7.00, TRUE, 1), ('Café Duplo', 10.00, TRUE, 1),
('Café com Leite', 9.50, TRUE, 1), ('Cappuccino', 13.00, TRUE, 1),
('Mocha Chocolate', 15.50, TRUE, 1), ('Cold Brew', 14.00, TRUE, 2),
('Frappé de Chocolate', 18.00, TRUE, 2), ('Suco de Laranja', 11.00, TRUE, 2),
('Brownie', 9.00, TRUE, 3), ('Cheesecake', 14.50, TRUE, 3),
('Cookie de Chocolate', 7.50, TRUE, 3), ('Pão de Queijo', 6.50, TRUE, 4),
('Croissant', 12.00, TRUE, 4), ('Sanduíche Natural', 16.00, TRUE, 4),
('Combo Café + Pão de Queijo', 12.50, TRUE, 5),
('Combo Cappuccino + Brownie', 20.00, TRUE, 5), ('Torta Especial', 22.00, FALSE, 3);

INSERT INTO pedido (data_pedido, status, valor_total, id_cliente) VALUES
('2026-09-01 08:15:00', 'FINALIZADO', 16.00, 1),
('2026-09-01 09:30:00', 'FINALIZADO', 26.00, 2),
('2026-09-02 10:20:00', 'CANCELADO', 18.00, 3),
('2026-09-03 14:10:00', 'FINALIZADO', 35.50, 1),
('2026-09-04 16:40:00', 'FINALIZADO', 20.00, 4),
('2026-09-05 11:05:00', 'PREPARANDO', 31.50, 5),
('2026-09-06 08:50:00', 'FINALIZADO', 28.00, 6),
('2026-09-07 17:25:00', 'FINALIZADO', 44.00, 2),
('2026-09-08 13:15:00', 'ABERTO', 13.00, 7),
('2026-09-09 09:45:00', 'FINALIZADO', 39.00, 1),
(NOW(), 'ABERTO', 0.00, 8);

SET @PEDIDO = LAST_INSERT_ID();
SELECT @PEDIDO;

INSERT INTO item_pedido (id_pedido, id_produto, quantidade, preco_unitario, observacao) VALUES
(1,1,1,7.00,NULL),(1,9,1,9.00,NULL),(2,4,2,13.00,'Sem canela'),
(3,7,1,18.00,NULL),(4,5,1,15.50,NULL),(4,16,1,20.00,NULL),
(5,16,1,20.00,NULL),(6,4,1,13.00,NULL),(6,7,1,18.00,NULL),
(7,6,2,14.00,NULL),(8,14,2,16.00,NULL),(8,12,2,6.00,NULL),
(9,4,1,13.00,NULL),(10,3,2,9.50,NULL),(10,16,1,20.00,NULL);

INSERT INTO forma_pagamento (descricao) VALUES
('Dinheiro'), ('PIX'), ('Cartão de Crédito'), ('Cartão de Débito');

INSERT INTO pagamento (id_pedido, id_forma_pagamento, valor, data_pagamento) VALUES
(1,2,16.00,'2026-09-01 08:20:00'),(2,4,26.00,'2026-09-01 09:40:00'),
(4,3,35.50,'2026-09-03 14:20:00'),(5,2,20.00,'2026-09-04 16:45:00'),
(7,1,28.00,'2026-09-06 09:00:00'),(8,3,30.00,'2026-09-07 17:30:00'),
(8,2,14.00,'2026-09-07 17:31:00'),(10,2,39.00,'2026-09-09 09:50:00');

-- EX 1 : UPDATE OU ATUALIZAÇÕES DE DADOS
UPDATE cliente
SET telefone = '19999990210'
WHERE ID_CLIENTE = 3;
-- DETERMINAR O COMANDO WHERE SEMPRE :)

-- EX 2: ATUALIZANDO VÁRIOS CAMPOS
UPDATE cliente
SET telefone = '199999981213',
    cidade = 'Piracicaba'
WHERE id_cliente = 4;

-- EX 3 : ATUALIZANDO VÁRIOS REGISTROS
UPDATE produto
SET preco = preco * 1.05
WHERE id_categoria = 1;

-- EX 4 : ATUALIZANDO SEM WHERE
-- UPDATE produto
-- SET preco = 1.00;
-- CUIDADO AO UTILIZAR ESSA LINHA

-- EX 5 : ATUALIZANDO CONDICIONAIS
UPDATE produto
SET preco = CASE 
    WHEN preco < 10 THEN preco * 1.10
    ELSE preco * 1.05
END
WHERE ativo = TRUE;

-- EX 6 : ATUALIZANDO PARA NULL
UPDATE cliente
SET telefone = NULL
WHERE id_cliente = 5;
-- TUDO ATUALIZAÇÕES OU MODIFICAÇÃO DE DADOS

-- EX 1 : EXCLUIR REGISTROS OU DADOS
DELETE FROM cliente
WHERE id_cliente = 10;

-- EX 2: EXCLUIR REGISTROS COM ESTRUTURA LÓGICA
UPDATE produto
SET ativo = FALSE
WHERE id_produto = 17;

UPDATE cliente
set ativo = FALSE
WHERE id_cliente = 8;


-- LIMPAR TABELA OU REMOVER TODOS OS REGISTROS
TRUNCATE TABLE cliente;




-- CONSULTAR INFORMAÇÕES NO BD
SELECT * FROM cliente;
-- CONSULTA POR ID
SELECT * FROM produto
WHERE id_categoria = 1;




-- MENSAGEM DE SUCESSO
SELECT 'BANCO DE DADOS SMARTCOFFEE_DML_BRUNO CRIADO COM SUCESSO!' AS mensagem;