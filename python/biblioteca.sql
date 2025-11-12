DROP DATABASE arte_foco;

CREATE DATABASE arte_foco;

use arte_foco;

CREATE Table usuarios(
    id int PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    senha VARCHAR(100)
);

INSERT INTO usuarios(nome, senha) VALUES(
    'Ryan','Adivinha2005#'
);

ALTER Table usuarios add COLUMN codigo_secreto;





