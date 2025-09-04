-- Consultas SQL para Relatórios de Análise de Engajamento
USE globo_tech;

-- 1. Ranking de conteúdos mais consumidos (ordenados por tempo total de consumo)
SELECT 
    c.nome_conteudo,
    SUM(i.watch_duration_seconds) AS total_consumo_segundos,
    ROUND(SUM(i.watch_duration_seconds) / 60, 2) AS total_consumo_minutos
FROM interacao i
JOIN conteudo c ON i.id_conteudo = c.id_conteudo
JOIN tipo_interacao ti ON i.id_tipo_interacao = ti.id_tipo_interacao
WHERE i.watch_duration_seconds IS NOT NULL 
  AND ti.nome_tipo = 'view_start'
GROUP BY c.id_conteudo, c.nome_conteudo
ORDER BY total_consumo_segundos DESC;

-- 2. Plataforma com maior engajamento (total de interações like, share, comment)
SELECT
    p.nome_plataforma,
    COUNT(i.id_interacao) AS total_engajamento
FROM interacao i
JOIN plataforma p ON i.id_plataforma = p.id_plataforma
JOIN tipo_interacao ti ON i.id_tipo_interacao = ti.id_tipo_interacao
WHERE ti.nome_tipo IN ('like', 'share', 'comment')
GROUP BY p.id_plataforma, p.nome_plataforma
ORDER BY total_engajamento DESC;

-- 3. Conteúdos mais comentados
SELECT
    c.nome_conteudo,
    COUNT(i.id_interacao) AS total_comentarios
FROM interacao i
JOIN conteudo c ON i.id_conteudo = c.id_conteudo
JOIN tipo_interacao ti ON i.id_tipo_interacao = ti.id_tipo_interacao
WHERE ti.nome_tipo = 'comment'
GROUP BY c.id_conteudo, c.nome_conteudo
ORDER BY total_comentarios DESC;

-- 4. Usuários com maior tempo total de consumo
SELECT 
    u.nome_usuario,
    SUM(i.watch_duration_seconds) AS total_consumo_segundos,
    ROUND(SUM(i.watch_duration_seconds) / 60, 2) AS total_consumo_minutos
FROM interacao i
JOIN usuario u ON i.id_usuario = u.id_usuario
JOIN tipo_interacao ti ON i.id_tipo_interacao = ti.id_tipo_interacao
WHERE i.watch_duration_seconds IS NOT NULL 
  AND ti.nome_tipo = 'view_start'
GROUP BY u.id_usuario, u.nome_usuario
ORDER BY total_consumo_segundos DESC;

-- 5. Total de interações por tipo de conteúdo
SELECT
    c.tipo_conteudo,
    COUNT(i.id_interacao) AS total_interacoes
FROM interacao i
JOIN conteudo c ON i.id_conteudo = c.id_conteudo
WHERE c.tipo_conteudo IS NOT NULL
GROUP BY c.tipo_conteudo
ORDER BY total_interacoes DESC;

-- 6. Tempo médio de consumo por plataforma
SELECT
    p.nome_plataforma,
    ROUND(AVG(i.watch_duration_seconds), 2) AS tempo_medio_segundos,
    ROUND(AVG(i.watch_duration_seconds) / 60, 2) AS tempo_medio_minutos
FROM interacao i
JOIN plataforma p ON i.id_plataforma = p.id_plataforma
JOIN tipo_interacao ti ON i.id_tipo_interacao = ti.id_tipo_interacao
WHERE i.watch_duration_seconds IS NOT NULL 
  AND ti.nome_tipo = 'view_start'
GROUP BY p.id_plataforma, p.nome_plataforma
ORDER BY tempo_medio_segundos DESC;

-- 7. Quantidade de comentários por conteúdo (com texto do comentário)
SELECT
    c.nome_conteudo,
    COUNT(i.id_interacao) AS quantidade_comentarios,
    GROUP_CONCAT(SUBSTRING(i.comment_text, 1, 50) SEPARATOR '; ') AS exemplos_comentarios
FROM interacao i
JOIN conteudo c ON i.id_conteudo = c.id_conteudo
JOIN tipo_interacao ti ON i.id_tipo_interacao = ti.id_tipo_interacao
WHERE ti.nome_tipo = 'comment' 
  AND i.comment_text IS NOT NULL
GROUP BY c.id_conteudo, c.nome_conteudo
ORDER BY quantidade_comentarios DESC;


