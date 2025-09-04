-- Arquivo de inserções de dados para o banco globo_tech
USE globo_tech;

-- Inserir alguns usuários de exemplo
INSERT IGNORE INTO usuario (id_usuario, nome_usuario, email) VALUES 
(101, 'Usuario_101', 'usuario101@email.com'),
(102, 'Usuario_102', 'usuario102@email.com'),
(103, 'Usuario_103', 'usuario103@email.com'),
(104, 'Usuario_104', 'usuario104@email.com'),
(105, 'Usuario_105', 'usuario105@email.com');

-- Inserir alguns conteúdos de exemplo
INSERT IGNORE INTO conteudo (id_conteudo, nome_conteudo, tipo_conteudo) VALUES 
(1, 'Jornal Nacional', 'Jornalismo'),
(2, 'Novela das 9', 'Novela'),
(3, 'Podcast Papo de Segunda', 'Podcast'),
(4, 'Jogo do Brasileirão Série A', 'Esporte'),
(5, 'The Voice Brasil', 'Reality Show'),
(6, 'Mais Você', 'Programa de Variedades'),
(7, 'Podcast GE Tabelando', 'Podcast'),
(8, 'Sessão da Tarde Clássicos', 'Filme'),
(9, 'Show da Virada', 'Show'),
(10, 'Documentário Amazônia Viva', 'Documentário');

-- Inserir relações conteúdo-plataforma
INSERT IGNORE INTO conteudo_plataforma (id_conteudo, id_plataforma) VALUES 
(1, 1), (1, 2), -- Jornal Nacional no Globoplay e TV Globo
(2, 1), (2, 2), -- Novela das 9 no Globoplay e TV Globo
(3, 1), -- Podcast Papo de Segunda no Globoplay
(4, 3), (4, 4), -- Jogo do Brasileirão no GE Globo e Sportv Play
(5, 1), (5, 2), -- The Voice Brasil no Globoplay e TV Globo
(6, 1), (6, 2), -- Mais Você no Globoplay e TV Globo
(7, 3), -- Podcast GE Tabelando no GE Globo
(8, 1), (8, 2), -- Sessão da Tarde no Globoplay e TV Globo
(9, 1), (9, 2), -- Show da Virada no Globoplay e TV Globo
(10, 1); -- Documentário Amazônia Viva no Globoplay

-- Nota: As interações serão inseridas via script Python lendo o CSV

