-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS globo_tech;
USE globo_tech;

-- DROP TABLES NA ORDEM CERTA (devido às foreign keys)
DROP TABLE IF EXISTS interacao;
DROP TABLE IF EXISTS conteudo_plataforma;
DROP TABLE IF EXISTS conteudo;
DROP TABLE IF EXISTS usuario;
DROP TABLE IF EXISTS plataforma;
DROP TABLE IF EXISTS tipo_interacao;

-- TABELA DE PLATAFORMAS
CREATE TABLE plataforma (
    id_plataforma INT AUTO_INCREMENT PRIMARY KEY,
    nome_plataforma VARCHAR(255) UNIQUE NOT NULL
);

-- TABELA DE USUÁRIOS
CREATE TABLE usuario (
    id_usuario INT PRIMARY KEY,
    nome_usuario VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE
);

-- TABELA DE TIPOS DE INTERAÇÃO
CREATE TABLE tipo_interacao (
    id_tipo_interacao INT AUTO_INCREMENT PRIMARY KEY,
    nome_tipo VARCHAR(50) UNIQUE NOT NULL
);

-- TABELA DE CONTEÚDOS
CREATE TABLE conteudo (
    id_conteudo INT PRIMARY KEY,
    nome_conteudo VARCHAR(255) NOT NULL,
    tipo_conteudo VARCHAR(50)
);

-- TABELA DE RELAÇÃO N:N ENTRE CONTEÚDO E PLATAFORMA
CREATE TABLE conteudo_plataforma (
    id_conteudo INT,
    id_plataforma INT,
    PRIMARY KEY (id_conteudo, id_plataforma),
    FOREIGN KEY (id_conteudo) REFERENCES conteudo(id_conteudo),
    FOREIGN KEY (id_plataforma) REFERENCES plataforma(id_plataforma)
);

-- TABELA DE INTERAÇÕES
CREATE TABLE interacao (
    id_interacao INT AUTO_INCREMENT PRIMARY KEY,
    id_conteudo INT NOT NULL,
    id_usuario INT NOT NULL,
    id_plataforma INT NOT NULL,
    id_tipo_interacao INT NOT NULL,
    timestamp_interacao DATETIME NOT NULL,
    watch_duration_seconds INT,
    comment_text TEXT,
    FOREIGN KEY (id_conteudo) REFERENCES conteudo(id_conteudo),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_plataforma) REFERENCES plataforma(id_plataforma),
    FOREIGN KEY (id_tipo_interacao) REFERENCES tipo_interacao(id_tipo_interacao)
);

-- Inserir tipos de interação
INSERT INTO tipo_interacao (nome_tipo) VALUES 
('view_start'),
('like'),
('share'),
('comment');

-- Inserir plataformas
INSERT INTO plataforma (nome_plataforma) VALUES 
('Globoplay'),
('TV Globo'),
('GE Globo'),
('Sportv Play'),
('Receitas Gshow'),
('Premiere');


