# 📈 Análise de Engajamento de Mídias Globo

Um **pipeline em Python puro** para simular a coleta, limpeza, estruturação e análise de dados de engajamento do público com conteúdos da Globo.

---

## 🧐 Visão Geral

- **Python 3.6+**: apenas módulos nativos (`csv`, `collections.defaultdict`).
- **Dados**: `interações_globo.csv` com interações simuladas de views, likes, shares e comments.
- **Arquitetura**: funções independentes para cada etapa do pipeline.
- **Robustez**: `try/except` em todas as conversões de tipo.
- **Saída**: relatório formatado, com contagens padronizadas e comentários numerados.

---

## 🚀 Funcionalidades

1. **Carregar CSV**
   Valida existência e não-vazio do arquivo, retorna lista de listas.

2. **Converter para Dicionários**
   Cada linha vira um `dict[cabeçalho → valor]`.

3. **Limpeza de Campos**
   - IDs (`int` ou `None`)
   - `watch_duration_seconds` (`int` ou `0`)
   - Strings `.strip()` + `.title()`

4. **Cálculo de Métricas**
   - Total de engajamentos (`like`, `share`, `comment`)
   - Contagem individual por tipo
   - Tempo total e média de visualização
   - Comentários listados e numerados

5. **Relatório Formatado**
   Prints organizados por conteúdo, com ordem fixa de tipos e emojis para destaque.

---

## 📷 Exemplo de Saída

```console
Iniciando Fase 1: Coleta e Estruturação Inicial de Dados de Engajamento Globo

Total de 150 linhas de dados (mais cabeçalho) carregadas.

Conteúdo ID: 1
Nome: Jornal Nacional – Edição de 20/10/2024
Total de engajamentos: 120

Contagem por tipo de interação:
  • view_start :  30
  • like       :  50
  • share      :  20
  • comment    :  20

Tempo total de visualização: 45000 s  
Média de tempo de visualização: 1500.0 s  

Comentários:
   1. Parabéns pela reportagem!  
   2. Muito informativo.  
   3. Gostei!  

Top 5 por tempo de visualização:
 1. Jornal Nacional – Edição de 20/10/2024: 45000 s  
 2. Novela Renascer – Capítulo 15:        30000 s  
 3. Podcast “Papo de Segunda”:           15000 s  
 4. Compacto Brasileirão:                12000 s  
 5. Receita de Bolo de Cenoura:          8000 s  
```

**Fim da análise de engajamento.**

---

## 👥 Integrantes do Grupo

*   mayasrl
*   Pierre
*   Beatriz
*   Fernando

---

<p align="center"> Desenvolvido durante o curso <strong>Academia Globotech</strong> da Ada em parceria com a Globo, com 💛 por <strong>@mayasrl e equipe</strong></p> 

