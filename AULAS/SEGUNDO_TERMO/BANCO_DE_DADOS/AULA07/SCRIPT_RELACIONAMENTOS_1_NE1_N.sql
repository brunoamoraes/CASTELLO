-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE Fornecedores (
Id_Fornecedor Int Auto_Increment Primary Key PRIMARY KEY,
Razao_Social varchar(100) not null
)

CREATE TABLE Produtos (
Id_Produto Int Auto_Increment Primary Key PRIMARY KEY,
Nome_Produto varchar(100) not null
)

CREATE TABLE Item_Produto (
Id_Produto Int Unique,
Id_Fornecedor Int Unique,
Qtde Int not null,
Observacao text(300),
Id_Item Int Auto_Increment Primary Key PRIMARY KEY,
FOREIGN KEY(Id_Produto) REFERENCES Produtos (Id_Produto)
)

