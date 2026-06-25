-- database: ./banco.db

INSERT INTO produto (codigo, descricao, valor) VALUES (3, 'Monitor', 1000);

CREATE TABLE cliente (
    id INT,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(50), 
    uf VARCHAR(2), 
    pontos INT,
    PRIMARY KEY (id)
);

INSERT INTO cliente (id, nome) VALUES (1, 'Jose');

INSERT INTO produto VALUES (7, 'Ergonomico Mouse', 200);

SELECT * FROM cliente;
SELECT 
  * 
FROM 
  produto 
WHERE
  descricao LIKE '%a%';

SELECT * FROM produto;  

DELETE FROM produto WHERE codigo = 1;

UPDATE produto
SET
  descricao = 'Monitor AOC', 
  valor = 1500
WHERE 
  codigo = 2;