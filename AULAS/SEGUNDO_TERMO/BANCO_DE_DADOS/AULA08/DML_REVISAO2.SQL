-- Active: 1788267997462@@127.0.0.1@3306@smartcoffee_dml_bruno
USE SMARTCOFFEE_DML_BRUNO;

-- INSERINDO DADOS NO BD
-- DML: INSERTS , UPDATE , DELETE

INSERT INTO cliente (nome,email,telefone,cidade,ativo) VALUES
('Adryan Costa','adryan@email.com','199999901','Limeira',TRUE),
('Ana Francisca','ana@email.com','199999902','Lençois Paulista',TRUE),
('Anna Julia','anaj@email.com','199999903','Limeira',TRUE),
('Beatriz Barros','beatrizb@email.com','199999904','Limeira',TRUE),
('Beatriz Santana','beatrizs@email.com','199999905','Limeira',TRUE),
('Bruno Dias','bruno2@email.com','199999906','Limeira',TRUE),
('Cristopher da Costa','cristopher@email.com','199999907','Mogi Guaçu',TRUE),
('Davi Guerra','davi@email.com',NULL,'Limeira',TRUE),
('Gabriel Lucio','grabiel@email.com','199999908','Limeira',TRUE),
('Gabriela Lima','gabriela2@email.com','199999909','Curitiba',TRUE),
('Giovana Santana','giovana@email.com',NULL,'Juqueropólis',FALSE),
('Gustavo Couto','gustavo@email.com','199999910','Ipatinga',FALSE),
('Isabeli Sousa','isabeli@email.com',NULL,'Limeira',TRUE),
('Jacó de Souza','jaco@email.com','199999911','Limeira',TRUE),
('João Moreira','joao2@email.com','199999912','Limeira',TRUE),
('John Pierre','john@email.com','199999913','cap haitien',TRUE),
('Jonas Dawid','jonas@email.com','199999914','Rio de Janeiro',TRUE),
('Juan Pablo','juan@email.com','199999915','Limeira',TRUE),
('Julia Fernanda','julia@email.com','199999916','Limeira',TRUE);

-- INSERINDO CAMPOS COM CHAVE ESTRANGEIRA
INSERT INTO produto (nome,preco,ativo,id_categoria) VALUES
('Manteiga Giovana',14.00,TRUE,12)

-- INSERINDO VALORES E BUSCANDO O ÚLTIMO VALOR INSERIDO
INSERT INTO pedido (data_pedido,status,valor_total,id_cliente) VALUES
(NOW(),'ABERTO',14.00,118)

SET @pedido = LAST_INSERT_ID();
SELECT @pedido;

-----------------------------------------------------------------------

-- ATUALIZANDO OU MODIFICANDO DADOS NO BD
-- EX 1: ATUALIZANDO INFORMAÇÕS INDIVIDUAIS
UPDATE cliente
SET telefone = '19999888801'
WHERE id_cliente = 20;

UPDATE cliente
SET ativo = TRUE


-- NUNCA, JAMAIS, NEVER ESQUEÇAM DE UTILIZAR O WHERE 

-- REGRA DE OURO
-- PRIMEIRA ETAPA
SELECT * FROM cliente
WHERE id_cliente = 18;

-- SEGUNDA ETAPA
UPDATE cliente
SET ativo = FALSE
WHERE id_cliente = 18;

-- EX 2: ATUALIZANDO MAIS DO QUE UM CAMPO
UPDATE cliente
SET telefone = '1999888016',
    cidade = 'Campinas'
WHERE id_cliente = 18;

-- EX 3: ATUALIZANDO COM CONDICIONAIS
UPDATE produto
SET preco = preco * 2.50
WHERE id_categoria = 1;


-- APAGANDO DADOS
-- EX 1: APAGAR DADOS SEM CONTER INFORMAÇÕES
DELETE FROM cliente;

-- EX 2: APAGAR DADOS COM CONDIÇÕES
DELETE FROM cliente
WHERE id_cliente = 18;

-- EX 3: APAGANDO DADOS DE TODA TABELA
TRUNCATE TABLE cliente;

-- EX 4: APAGAR DE FORMA REPRESENTATIVA OU LÓGICA
UPDATE produto
SET ativo = FALSE
where id_produto = 19;

------------------------------------------------------------------
-- REALIZANDO PASSOS PARA UMA COMPRA NO SMARTCOFFEE
-- PASSO 1: CADASTRAR UM NOVO CLIENTE
INSERT INTO cliente (nome,email,telefone,cidade,ativo) VALUES
('Bruno A','brunoa@email.com','1999123456','Piracicaba',TRUE);
SET @cliente = LAST_INSERT_ID();

-- PASSO 2: CRIAR O PEDIDO
INSERT INTO pedido (data_pedido,status,valor_total,id_cliente) VALUES
(NOW(),'ABERTO',0.00,102);
SET @pedido = LAST_INSERT_ID();

-- PASSO 3: INSERIR ITENS NO PEDIDO
INSERT INTO item_pedido (id_pedido, id_produto,quantidade,preco_unitario) VALUES
(@pedido,4,1,73.13),
(@pedido,11,1,11.25);

-- PASSO 4: ATUALIZAR O TOTAL E STATUS
UPDATE pedido
SET valor_total = 84.38,
    status = 'Preparando'
WHERE id_pedido = @pedido;

-- PASSO 5: REGISTRAR PAGAMENTO
INSERT INTO pagamento (id_pedido, id_forma_pagamento, valor, data_pagamento) VALUES
(@pedido, 1, 84.38, NOW());

delete from pagamento
where id_pagamento = 1;



-- CONSULTAR DADOS EM TABELAS BD
-- CONSULTAR TODA A TABELA
SELECT * FROM pagamento;
-- CONSULTAR INDIVIDUAL POR ID
SELECT * FROM cliente
WHERE id_cliente = 115;