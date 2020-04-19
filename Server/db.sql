CREATE DATABASE dclean;
use dclean;

create table carros
(
    `id` INT(12) NOT NULL,
    `placa` VARCHAR(12) NOT NULL
)ENGINE = InnoDB;

create table carros_satisfactions
(
    `id` INT(12) NOT NULL,
    `carro` INT(12) NOT NULL,
    `satisfaction` INT NOT NULL,
    `comentario` TEXT
)ENGINE = InnoDB;

create table objetos
(
    `id` INT(12) PRIMARY KEY NOT NULL,
    `nome` VARCHAR(12) NOT NULL
)ENGINE = InnoDB;

create table limpezas
(   
    `id` INT(12) PRIMARY KEY NOT NULL,
    `carro` INT(12) NOT NULL,
    `date` DATE NOT NULL,
    `nascimento` INT(12) NOT NULL,
    `km` VARCHAR(11) NOT NULL,
    `tipo` VARCHAR(8) NOT NULL,
    `objetos` INT(12) NOT NULL
)ENGINE = InnoDB;

create table nascimentos
(
    `id` INT(12) PRIMARY KEY NOT NULL,
    `nome` VARCHAR(12) NOT NULL
)ENGINE = InnoDB;

create table limpezas_geral
(
    `id` INT(12) PRIMARY KEY NOT NULL,
    `tipo` INT(12) NOT NULL,
    `date` DATE NOT NULL,
    `date_future` DATE NOT NULL
)ENGINE = InnoDB;

create table limpezas_geral_tipos
(
    `id` INT(12) PRIMARY KEY NOT NULL,
    `nome` VARCHAR(12) NOT NULL
)ENGINE = InnoDB;

create table notificacoes_recusas
(
    `id` INT(12) PRIMARY KEY NOT NULL,
    `carro` INT(12) NOT NULL,
    `date` DATE NOT NULL,
    `km` VARCHAR(11)
)ENGINE = InnoDB;
