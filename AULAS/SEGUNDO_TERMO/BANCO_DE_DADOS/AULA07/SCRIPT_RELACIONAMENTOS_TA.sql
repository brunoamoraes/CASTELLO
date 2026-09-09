-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE Clientes (
Id_Cliente Int Auto_Increment Primary Key PRIMARY KEY,
Nome_Cliente varchar(60) not null
)

CREATE TABLE Pedidos (
Id_Pedido Int Auto_Increment Primary Key PRIMARY KEY,
Quantidade Int Not Null,
Id_Cliente Int Auto_Increment Primary Key,
FOREIGN KEY(Id_Cliente) REFERENCES Clientes (Id_Cliente)
)

CREATE TABLE Produtos+Estoques (
Id_Produto Int Auto_Increment Primary Key,
Nome_Produto varchar(100),
Id_Estoque Int Auto_Increment Primary Key,
Valor Decimal(10,2),
PRIMARY KEY(Id_Produto,Id_Estoque)
)

CREATE TABLE Fornecedores (
Id_Fornecedor Int Auto_Increment Primary Key PRIMARY KEY,
Razao_Social varchar(100) not null
)

CREATE TABLE Produtos (
Id_Produto Int Auto_Increment Primary Key PRIMARY KEY,
Nome_Produto varchar(100)
)

CREATE TABLE Item_Produto (
Id_Produto Int,
Id_Fornecedor Int,
Id_Item Int Auto_Increment Primary Key PRIMARY KEY,
Quantidade Int
)

