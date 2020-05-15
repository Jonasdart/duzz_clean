CREATE DATABASE dclean;
use dclean;
--
create table carros
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `placa` VARCHAR(12) NOT NULL,
    `locais` TEXT NOT NULL 
)ENGINE = InnoDB;
--
create table dispersores
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `carro` INT(12) NOT NULL,
    `local` INT(12) NOT NULL,
)ENGINE = InnoDB;
--
create table locais
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `nome` VARCHAR(12) NOT NULL
)ENGINE = InnoDB;
--
create table carros_satisfactions
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `carro` INT(12) NOT NULL,
    `satisfaction` INT NOT NULL,
    `comentario` TEXT
)ENGINE = InnoDB;
--
create table limpezas
(   
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `carro` INT(12) NOT NULL,
    `date` DATE NOT NULL,
    `km` VARCHAR(11) NOT NULL,
    `nascimento` INT(12) NOT NULL,
    `tipo` VARCHAR(8) NOT NULL,
    `dispersores` TEXT NOT NULL
)ENGINE = InnoDB;
--
create table nascimentos
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `nome` VARCHAR(12) NOT NULL
)ENGINE = InnoDB;
--
create table limpezas_geral
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `tipo` INT(12) NOT NULL,
    `date` DATE NOT NULL,
    `date_future` DATE NOT NULL
)ENGINE = InnoDB;
--
create table limpezas_geral_tipos
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `nome` VARCHAR(12) NOT NULL
)ENGINE = InnoDB;
--
create table notificacoes_recusas
(
    `id` INT(12) PRIMARY KEY AUTO_INCREMENT,
    `carro` INT(12) NOT NULL,
    `date` DATE NOT NULL,
    `km` VARCHAR(11)
)ENGINE = InnoDB;
--
ALTER TABLE carros_satisfacoes
ADD CONSTRAINT fk_carro FOREIGN KEY (carro) REFERENCES carros(id);
--
ALTER TABLE limpezas 
ADD CONSTRAINT fk_carro2 FOREIGN KEY (carro) REFERENCES carros(id), 
ADD CONSTRAINT fk_nascimento FOREIGN KEY (nascimento) REFERENCES nascimentos(id);
--
ALTER TABLE notificacoes_recusas 
ADD CONSTRAINT fk_carro3 FOREIGN KEY (carro) REFERENCES carros(id);
--
ALTER TABLE dispersores 
ADD CONSTRAINT fk_carro4 FOREIGN KEY (carro) REFERENCES carros(id),
ADD CONSTRAINT fk_local FOREIGN KEY (local) REFERENCES locais(id);