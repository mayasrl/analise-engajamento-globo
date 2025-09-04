# Projeto Unificado - Fase 4: Persistência e Análise de Engajamento com Banco de Dados Relacional

## Objetivo

Nesta fase do projeto, o objetivo é evoluir o sistema de análise de engajamento para utilizar um banco de dados relacional (MySQL) para persistência dos dados. Isso torna a solução mais robusta, escalável e alinhada com as práticas de mercado.

## Modelagem de Dados

Foi realizada a modelagem do banco de dados com base nas classes existentes no projeto. O Modelo Entidade-Relacionamento (MER) e o Diagrama de Entidade-Relacionamento (DER) foram criados para representar a estrutura do banco.

### Diagrama MER

![Diagrama MER](https://private-us-east-1.manuscdn.com/sessionFile/tdeVnIrxISuVbn5qvhTw0P/sandbox/rwCVZHZnQa0wtRZAvG4bSg-images_1756994975056_na1fn_L2hvbWUvdWJ1bnR1L21lcg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvdGRlVm5JcnhJU3VWYm41cXZoVHcwUC9zYW5kYm94L3J3Q1ZaSFpuUWEwd3RSWkF2RzRiU2ctaW1hZ2VzXzE3NTY5OTQ5NzUwNTZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyMWxjZy5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=nzm2zxU8qiBwNnK8OqH6rBJxln2j3Xnh4xCBs7cQnMfLCpyH3o2pNYTqasqHqoAuR4d8tyU7vHme8RS7TRaBvNDfSlCQM8i2GtNRMCXbt4hzAzzJNbAUx9IP-64xZddbwBWm3UN~LJiXibrBHvp9xuuGJcP-q9fKKi65vVfDyaldvIEZ103hIwDCj4o7ByqQyLKp~Qd0eI0mX5~HTTXUob066QNow27UbIRkFqbRGX32gcuRuh3ktM2Zsv1xZp04mtB3JIBiEkJPC~Uyha0tm7d7jY7nxmv~HOWh-g6HbhcO9SI~yqHCaUcUNhQbY9IMXSBXHF6WJUjNYgcClEHFVw__)

## Estrutura do Banco de Dados

O script `schema.sql` contém os comandos DDL para criar o banco de dados `globo_tech` e as tabelas `Usuario`, `Conteudo`, `Plataforma` e `Interacao`.

## Carga de Dados

O script `carga_dados.py` é responsável por ler o arquivo `interacoes_globo.csv`, se conectar ao banco de dados MySQL e popular as tabelas com os dados das interações.

## Consultas SQL

O arquivo `queries.sql` contém as consultas SQL (DQL) para gerar os relatórios de análise de engajamento, como o ranking de conteúdos mais consumidos, a plataforma com maior engajamento e os conteúdos mais comentados.

## Como Executar

1.  **Configurar o banco de dados:**
    *   Crie um banco de dados MySQL chamado `globo_tech`.
    *   Execute o script `schema.sql` para criar as tabelas.

2.  **Instalar dependências:**
    ```bash
    pip install mysql-connector-python
    ```

3.  **Executar a carga de dados:**
    *   Certifique-se de que o arquivo `interacoes_globo.csv` está no mesmo diretório.
    *   Execute o script `carga_dados.py`:
    ```bash
    python carga_dados.py
    ```

4.  **Executar as consultas:**
    *   Utilize as consultas do arquivo `queries.sql` em um cliente MySQL para obter os relatórios.


