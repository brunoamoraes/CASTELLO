USE smartcoffee_dml_bruno;

-- 1
INSERT INTO cliente (nome,email,telefone,cidade) VALUES
('Luana Prado','luana.a09@email.com','19980000001','Limeira'),
('Mateus Reis','mateus.a09@email.com','19980000002','Americana');

-- 2
INSERT INTO categoria (nome) VALUES ('Especiais da Casa');

-- 3
SELECT id_categoria,nome FROM categoria WHERE nome='Especiais da Casa';
SET @categoria_especial = (SELECT id_categoria FROM categoria WHERE nome='Especiais da Casa');
INSERT INTO produto (nome,preco,id_categoria) VALUES
('Latte Caramelo',17.00,@categoria_especial),
('Chocolate da Casa',16.50,@categoria_especial),
('Croissant Especial',18.00,@categoria_especial);

-- 4
INSERT INTO cliente (nome,email,telefone,cidade)
VALUES ('Nathalia Luz','nathalia.a09@email.com',NULL,'Campinas');

-- 5 e 6
SET @cliente_atividade = (SELECT id_cliente FROM cliente WHERE email='luana.a09@email.com');
INSERT INTO pedido (data_pedido,status,valor_total,id_cliente)
VALUES (NOW(),'ABERTO',0.00,@cliente_atividade);
SET @pedido_atividade = LAST_INSERT_ID();
INSERT INTO item_pedido (id_pedido,id_produto,quantidade,preco_unitario) VALUES
(@pedido_atividade,4,1,13.00),
(@pedido_atividade,9,2,9.00);

-- 7
SELECT * FROM cliente WHERE email='luana.a09@email.com';
UPDATE cliente SET telefone='19981111111' WHERE email='luana.a09@email.com';
SELECT * FROM cliente WHERE email='luana.a09@email.com';

-- 8
SELECT * FROM cliente WHERE email='mateus.a09@email.com';
UPDATE cliente SET cidade='Limeira',telefone='19982222222'
WHERE email='mateus.a09@email.com';
SELECT * FROM cliente WHERE email='mateus.a09@email.com';

-- 9
SELECT id_produto,nome,preco FROM produto WHERE id_categoria=@categoria_especial;
UPDATE produto SET preco=ROUND(preco*1.08,2) WHERE id_categoria=@categoria_especial;
SELECT id_produto,nome,preco FROM produto WHERE id_categoria=@categoria_especial;

-- 10
SELECT * FROM pedido WHERE id_pedido=@pedido_atividade;
UPDATE pedido SET status='PREPARANDO' WHERE id_pedido=@pedido_atividade;
SELECT * FROM pedido WHERE id_pedido=@pedido_atividade;

-- 11
SELECT SUM(quantidade*preco_unitario) AS total
FROM item_pedido WHERE id_pedido=@pedido_atividade;
UPDATE pedido
SET valor_total=(SELECT SUM(quantidade*preco_unitario)
                 FROM item_pedido WHERE id_pedido=@pedido_atividade)
WHERE id_pedido=@pedido_atividade;
SELECT * FROM pedido WHERE id_pedido=@pedido_atividade;

-- 12
SELECT * FROM produto WHERE nome='Croissant Especial';
UPDATE produto SET ativo=FALSE WHERE nome='Croissant Especial';
SELECT * FROM produto WHERE nome='Croissant Especial';

-- 13
INSERT INTO cliente (nome,email,cidade)
VALUES ('Cliente Temporário','temporario.a09@email.com','Limeira');
SELECT * FROM cliente WHERE email='temporario.a09@email.com';
DELETE FROM cliente WHERE email='temporario.a09@email.com';
SELECT * FROM cliente WHERE email='temporario.a09@email.com';

-- 14: o comando abaixo gera erro de FK, pois id_cliente=1 possui pedidos.
-- DELETE FROM cliente WHERE id_cliente=1;

-- 15
-- A FK pedido.id_cliente -> cliente.id_cliente impede deixar pedidos órfãos.

-- 16
INSERT INTO categoria (nome) VALUES ('Excluir Depois');
SELECT * FROM categoria WHERE nome='Excluir Depois';
DELETE FROM categoria WHERE nome='Excluir Depois';
SELECT * FROM categoria WHERE nome='Excluir Depois';

-- 17: erro de FOREIGN KEY
-- INSERT INTO produto (nome,preco,id_categoria) VALUES ('Inválido',10.00,9999);

-- 18: erro de UNIQUE
-- INSERT INTO cliente (nome,email,cidade) VALUES ('Duplicado','ana@email.com','Limeira');

-- 19: erro de FOREIGN KEY
-- INSERT INTO pedido (data_pedido,status,valor_total,id_cliente)
-- VALUES (NOW(),'ABERTO',0.00,9999);

-- 20
-- 17 e 19 violam integridade referencial (FK). 18 viola unicidade do e-mail.

-- 21 a 24
START TRANSACTION;
INSERT INTO cliente (nome,email,cidade)
VALUES ('Rollback Teste','rollback.a09@email.com','Limeira');
SET @cliente_rb=LAST_INSERT_ID();
INSERT INTO pedido (data_pedido,status,valor_total,id_cliente)
VALUES (NOW(),'ABERTO',20.00,@cliente_rb);
SET @pedido_rb=LAST_INSERT_ID();
INSERT INTO item_pedido (id_pedido,id_produto,quantidade,preco_unitario) VALUES
(@pedido_rb,1,1,7.00),(@pedido_rb,4,1,13.00);
SELECT c.nome,p.id_pedido,p.valor_total
FROM cliente c JOIN pedido p ON p.id_cliente=c.id_cliente
WHERE c.email='rollback.a09@email.com';
ROLLBACK;
SELECT * FROM cliente WHERE email='rollback.a09@email.com';

-- 25
START TRANSACTION;
INSERT INTO cliente (nome,email,cidade)
VALUES ('Commit Teste','commit.a09@email.com','Limeira');
SET @cliente_commit=LAST_INSERT_ID();
INSERT INTO pedido (data_pedido,status,valor_total,id_cliente)
VALUES (NOW(),'PREPARANDO',22.00,@cliente_commit);
SET @pedido_commit=LAST_INSERT_ID();
INSERT INTO item_pedido (id_pedido,id_produto,quantidade,preco_unitario) VALUES
(@pedido_commit,4,1,13.00),(@pedido_commit,9,1,9.00);
COMMIT;
SELECT c.nome,p.id_pedido,p.status,p.valor_total
FROM cliente c JOIN pedido p ON p.id_cliente=c.id_cliente
WHERE c.email='commit.a09@email.com';