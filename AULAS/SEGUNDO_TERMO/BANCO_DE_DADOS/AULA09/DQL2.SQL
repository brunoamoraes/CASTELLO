-- Active: 1788267997462@@127.0.0.1@3306@smartcoffee_dml_bruno
INSERT INTO cliente (nome,email,telefone,cidade,ativo) VALUES
('Edson Wladimir','edson@email.com','19999888244','Paris',TRUE);

-- Exemplo de estrutura simples de SELECT
-- SELECT coluna
-- FROM tabela;

-- EX 1: SELECT PARA CONSULTAR TODAS AS COLUNAS
SELECT * FROM cliente;

-- EX 2: CONSULTANDO POR COLUNAS
SELECT nome, email FROM cliente;

-- EX 3: INSERINDO APELIDO NAS COLUNAS -- ALIAS
SELECT nome AS Cliente
FROM cliente;
SELECT nome AS Cliente, telefone AS Contato, ativo AS Status
FROM cliente;
SELECT nome, preco, preco * 0.90 AS Preço_Promocional
FROM produto;

-- EX 4: DISTINCT - ELIMINAR REPETIÇÕES
SELECT cidade FROM cliente;

SELECT DISTINCT cidade
FROM cliente;
-- SEM DISTINCT O ITEM IRÁ APARECER VÁRIAS VEZES
-- COM DISTINCT O ITEM IRÁ APARECER APENAS UMA VEZ

-- EX 5: FILTRO EM REGISTROS
SELECT nome, preco
FROM produto
WHERE preco > 10;
-- RETORNA VALORES ACIMA DE 10 REAIS EM SEUS PREÇOS

SELECT nome, preco
FROM cliente
WHERE ativo = TRUE;
-- RETORNA PRODUTOS ATIVOS

SELECT id_pedido, data_pedido, valor_total
FROM pedido
WHERE valor_total >= 25.00;
-- RETORNA PEDIDOS ACIMA DE DETERMINADO VALOR

-- OPERADORES DE COMPARAÇÃO
-- = IGUAL
-- <> ou != DIFERENTE
-- > MAIOR QUE
-- >= MAIOR OU IGUAL
-- < MENOR QUE
-- <= MENOR OU IGUAL

-- EX 6: USO DE AND, OR E NOT
-- AND - TODAS AS CONDIÇÕES PRECISAM SER VERDADEIRAS
SELECT nome, preco
FROM produto
WHERE preco >= 8.00 AND preco <= 20.00;

-- OR - PELO MENOS UMA CONDIÇÃO VERDADEIRA
SELECT nome, cidade
FROM cliente
WHERE cidade = 'Limeira' OR cidade = 'Piracicaba';

-- NOT - NEGAR NÃO TRAZER RESULTADO QUE FOI APRESENTADO
SELECT nome, cidade
FROM cliente
WHERE NOT cidade = 'Limeira';

-- JUNTOS - AND E OR SEMPRE UTILIZAR OS ()
SELECT nome, cidade, ativo AS Status
FROM cliente
WHERE ativo = TRUE
AND (cidade = 'Limeira' OR cidade = 'Americana');

-- EX 7: PESQUISANDO POR INTERVALOS - BETWEEN
SELECT nome, preco
FROM produto
WHERE preco BETWEEN 8.00 AND 15.00;

SELECT id_pedido, data_pedido, valor_total
FROM pedido
WHERE data_pedido BETWEEN '2026-09-01 00:00:00' AND '2026-09-30 23:59:59';

-- EX 8: IN COM VÁRIAS POSSIBILIDADES
SELECT nome, cidade
FROM cliente
WHERE cidade IN ('Limeira','Americana','Piracicaba');

SELECT nome, cidade
FROM cliente
WHERE cidade NOT IN ('Limeira','Campinas');

-- EX 9: EXEMPLO COM TEXTOS OU PESQUISAR POR TEXTOS - LIKE
-- CORINGAS
-- % VÁRIOS CARACTERES
-- _ EXATAMENTE UM CARACTER

SELECT nome
FROM produto
WHERE nome LIKE 'Café%';
-- RETORNAR PRODUTOS QUE POSSUEM A PALAVRA CAFÉ E QUE COMEÇAM COM ELA

SELECT nome
FROM produto
WHERE nome LIKE '%chocolate%';
-- RETORNAR PRODUTOS QUE POSSUEM A PALAVRA CHOCOLATE

SELECT nome
FROM produto
WHERE nome LIKE '%Silva';
-- RETORNAR NOMES QUE TERMINAM COM SILVA

SELECT nome
FROM produto
WHERE nome LIKE '_afé%';

-- EX 10: NULL - AUSÊNCIA DE VALOR
SELECT nome, telefone
FROM cliente
WHERE telefone IS NULL;

SELECT nome, telefone
FROM cliente
WHERE telefone IS NOT NULL;

-- EX 11: ORDER BY - ORDENAR RESULTADOS
-- ASC SIGNIFICA CRESCENTE
-- DESC SIGNIFICA DECRESCENTE
SELECT nome, preco
FROM produto
ORDER BY preco ASC;

SELECT nome, preco
FROM produto
ORDER BY preco DESC;

SELECT cidade, nome
FROM cliente
ORDER BY cidade ASC, nome DESC;

-- EX 12: LIMIT - LIMITANDO A QUANTIDADE DE LINHA
SELECT nome, preco
FROM produto
ORDER BY preco DESC
LIMIT 5;

SELECT nome, preco
FROM produto
ORDER BY nome DESC
LIMIT 5 OFFSET 5;

-- EX 13: CÁLCULO DE COLUNAS E VALORES PROJETÁVEIS
SELECT nome, preco, preco * 2.00 AS preco_atualizado
FROM produto;

SELECT id_item, quantidade, preco_unitario, quantidade * preco_unitario AS Total_Compra
FROM item_pedido;

-- EX 14: FUNÇÕES PARA CONSULTA
-- TEXTOS
SELECT UPPER(nome) AS Nome_Cliente, LOWER(email) AS Email
FROM cliente;

SELECT CONCAT(nome, ' -- ', cidade) AS Cliente_Cidade
FROM cliente;

-- NÚMEROS
SELECT nome, preco, ROUND(preco * 1.90, 2) AS Preço_Desconto
FROM produto;

-- DATAS
SELECT id_pedido, data_pedido, DATE(data_pedido) AS DATAS, DAY(data_pedido) AS DIA, MONTH(data_pedido) AS MÊS, YEAR(data_pedido) AS ANO
FROM pedido;

-- SUBSTITUINDO O NULL NO RESULTADO - COALESCE
SELECT nome, COALESCE(telefone, 'Não Informado') AS Contato
FROM cliente;

























