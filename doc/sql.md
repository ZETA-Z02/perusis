# SQL DE BASE DE DATOS PRODUCTOS
CREATE DATABASE STOCK;
USE STOCK;
## tablas
CREATE TABLE `categorias`(
    `idcategoria` INT NOT NULL AUTO_INCREMENT,
    `categoria` VARCHAR(50),
    PRIMARY KEY(`idcategoria`)
);
CREATE TABLE `marcas`(
    `idmarca` INT NOT NULL AUTO_INCREMENT,
    `marca` VARCHAR(50),
    PRIMARY KEY(`idmarca`)
);
CREATE TABLE `productos`(
    `id` INT NOT NULL AUTO_INCREMENT,
    `idcategoria` INT NOT NULL,
    `idmarca` INT NOT NULL,
    `modelo` TEXT NOT NULL,
    `tipoventa` VARCHAR(20) NOT NULL,
    `stock` INT NOT NULL,
    `precio` DOUBLE NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY (`idcategoria`) REFERENCES categorias(`idcategoria`),
    FOREIGN KEY (`idmarca`) REFERENCES marcas(`idmarca`)
);