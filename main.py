import csv
from collections import defaultdict

# NOME DO ARQUIVO CSV ESPERADO NO MESMO DIRETÓRIO DO SCRIPT
NOME_ARQUIVO_CSV = "interacoes_globo.csv"

def carregar_dados_de_arquivo_csv(nome_arquivo):
    """
    Carrega os dados de um arquivo CSV para uma lista de listas.
    A primeira lista retornada é o cabeçalho, e as subsequentes são as linhas de dados.
    Retorna None se o arquivo não for encontrado ou ocorrer um erro.
    """
    dados_com_cabecalho = []
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8', newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            # Adiciona todas as linhas (incluindo o cabeçalho) à lista
            for linha in leitor_csv:
                dados_com_cabecalho.append(linha)

        if not dados_com_cabecalho:
            print(f"Aviso: O arquivo CSV '{nome_arquivo}' está vazio.")
            return None
        return dados_com_cabecalho
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado. Certifique-se de que ele está na mesma pasta do script.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV '{nome_arquivo}': {e}")
        return None

def converter_lista_para_lista_de_dicionarios(dados_em_lista_com_cabecalho):
    """
    Converte uma lista de listas (onde a primeira lista é o cabeçalho)
    para uma lista de dicionários.
    """
    cabecalho = dados_em_lista_com_cabecalho[0]
    dados = dados_em_lista_com_cabecalho[1:]
    lista_de_dicionarios = [dict(zip(cabecalho, linha)) for linha in dados]
    return lista_de_dicionarios

def tratar_campos_inteiros(interacao_bruta, interacao_limpa):
    """
    Trata os campos que devem ser inteiros simples (id_conteudo e id_usuario), convertendo-os e tratando erros.
    Retorna a interacao limpa com os campos convertidos.
    """
    try:
        interacao_limpa['id_conteudo'] = int(interacao_bruta['id_conteudo'])
    except (ValueError, KeyError):
        interacao_limpa['id_conteudo'] = None

    try:
        interacao_limpa['id_usuario'] = int(interacao_bruta['id_usuario'])
    except (ValueError, KeyError):
        interacao_limpa['id_usuario'] = None

    return interacao_limpa

def tratar_watch_duration_seconds(interacao_bruta, interacao_limpa):
    """
    Trata o campo watch_duration_seconds, convertendo-o e tratando erros.
    Se o campo estiver vazio ou ausente, deve ser definido como 0.
    Retorna a interacao limpa com o campo watch_duration_seconds convertido.
    """
    try:
        interacao_limpa['watch_duration_seconds'] = int(interacao_bruta.get('watch_duration_seconds', '') or 0)
    except ValueError:
        interacao_limpa['watch_duration_seconds'] = 0  # Valor padrão
        print("Erro ao converter watch_duration_seconds para inteiro. Valor atribuído como 0.")
    return interacao_limpa

def tratar_campos_texto(interacao_bruta, interacao_limpa):
    """
    Trata os campos de texto, removendo espaços extras e convertendo para string.
    Retorna a interacao limpa com os campos convertidos.
    """
    interacao_limpa['nome_conteudo'] = interacao_bruta['nome_conteudo'].strip().title() if interacao_bruta['nome_conteudo'] else ''
    interacao_limpa['tipo_interacao'] = interacao_bruta['tipo_interacao'].strip()
    interacao_limpa['timestamp_interacao'] = interacao_bruta['timestamp_interacao'].strip()
    interacao_limpa['plataforma'] = interacao_bruta['plataforma'].strip().title()
    interacao_limpa['comment_text'] = interacao_bruta['comment_text'].strip() if interacao_bruta['comment_text'] else ''

    return interacao_limpa

def limpar_e_transformar_dados(lista_interacoes_brutas_dict):
    """
    Limpa e transforma os dados brutos das interações (lista de dicionários).
    Converte tipos de dados, trata valores ausentes e remove espaços.
    Essa função usa as 3 funções acima.
    Retorna a lista de interações limpas (também como lista de dicionários).
    """
    interacoes_limpas = []
    for interacao_bruta in lista_interacoes_brutas_dict:
        interacao_limpa = {}
        interacao_limpa = tratar_campos_inteiros(interacao_bruta, interacao_limpa)
        interacao_limpa = tratar_watch_duration_seconds(interacao_bruta, interacao_limpa)
        interacao_limpa = tratar_campos_texto(interacao_bruta, interacao_limpa)
        interacoes_limpas.append(interacao_limpa)

    return interacoes_limpas

def criar_mapa_conteudos(interacoes_limpas):
    """
    Cria um dicionário que mapeia id_conteudo para nome_conteudo.
    """
    mapa_conteudos = {}
    for interacao in interacoes_limpas:
        id_conteudo = interacao['id_conteudo']
        nome_conteudo = interacao.get('nome_conteudo')
        if id_conteudo not in mapa_conteudos and nome_conteudo:
            mapa_conteudos[id_conteudo] = nome_conteudo
    return mapa_conteudos

def calcular_metricas_por_conteudo(interacoes_limpas, mapa_conteudos):
    """
    Calcula várias métricas de engajamento agrupadas por conteúdo.
    Retorna um dicionário com as métricas calculadas.
    """
    metricas_conteudo = defaultdict(lambda: {
        'nome_conteudo': '',
        'total_interacoes_engajamento': 0,
        'contagem_por_tipo_interacao': defaultdict(int),
        'tempo_total_visualizacao': 0,
        'soma_watch_duration_para_media': 0,
        'contagem_watch_duration_para_media': 0,
        'media_tempo_visualizacao': 0.0,
        'comentarios': []
    })

    tipos_engajamento = {'like', 'share', 'comment'}

    for interacao in interacoes_limpas:
        id_c = interacao['id_conteudo']
        metricas_c = metricas_conteudo[id_c]

        if not metricas_c['nome_conteudo']:
            metricas_c['nome_conteudo'] = mapa_conteudos.get(id_c, "Desconhecido")

        if interacao['tipo_interacao'] in tipos_engajamento:
            metricas_c['total_interacoes_engajamento'] += 1

        metricas_c['contagem_por_tipo_interacao'][interacao['tipo_interacao']] += 1

        metricas_c['tempo_total_visualizacao'] += interacao['watch_duration_seconds']

        if interacao['watch_duration_seconds'] > 0:
            metricas_c['soma_watch_duration_para_media'] += interacao['watch_duration_seconds']
            metricas_c['contagem_watch_duration_para_media'] += 1

        if interacao['tipo_interacao'] == 'comment' and interacao['comment_text']:
            metricas_c['comentarios'].append(interacao['comment_text'])

    for id_c, m in metricas_conteudo.items():
        if m['contagem_watch_duration_para_media'] > 0:
            m['media_tempo_visualizacao'] = round(
                m['soma_watch_duration_para_media'] / m['contagem_watch_duration_para_media'], 2
            )
        del m['soma_watch_duration_para_media']
        del m['contagem_watch_duration_para_media']

    return dict(metricas_conteudo)

def main():
    print("Iniciando Fase 1: Coleta e Estruturação Inicial de Dados de Engajamento Globo\n")

    dados_brutos_lista_de_listas = carregar_dados_de_arquivo_csv(NOME_ARQUIVO_CSV)

    if dados_brutos_lista_de_listas is None:
        print(f"Não foi possível carregar os dados do arquivo '{NOME_ARQUIVO_CSV}'. Encerrando.")
        return

    if len(dados_brutos_lista_de_listas) < 2:
        print(f"O arquivo '{NOME_ARQUIVO_CSV}' não contém dados suficientes (cabeçalho e linhas de dados). Encerrando.")
        return

    print(f"Total de {len(dados_brutos_lista_de_listas) - 1} linhas de dados (mais cabeçalho) carregadas do CSV.\n")

    interacoes_brutas_dict = converter_lista_para_lista_de_dicionarios(dados_brutos_lista_de_listas)

    interacoes_limpas = limpar_e_transformar_dados(interacoes_brutas_dict)
    if not interacoes_limpas:
        print("Nenhuma interação válida encontrada após a limpeza. Encerrando.")
        return
    print(f"Total de {len(interacoes_limpas)} interações válidas após limpeza.\n")

    print("Iniciando a análise de engajamento...\n")

    mapa_conteudos = criar_mapa_conteudos(interacoes_limpas)
    if not mapa_conteudos:
        print("Nenhum conteúdo encontrado. Encerrando.")
        return
    print(f"Total de {len(mapa_conteudos)} conteúdos únicos mapeados.\n")

    for i, (id_c, nome_c) in enumerate(mapa_conteudos.items()):
        print(f"ID: {id_c}, Nome: {nome_c}")

    metricas_conteudo = calcular_metricas_por_conteudo(interacoes_limpas, mapa_conteudos)

    print("\nAnálise de engajamento concluída.\n")
    print("Resultados:")

    for id_c, metricas in metricas_conteudo.items():
        print(f"\nConteúdo ID: {id_c}")
        print(f"Nome: {metricas['nome_conteudo']}")
        print(f"Total de interações de engajamento: {metricas['total_interacoes_engajamento']}")
        print(f"Contagem por tipo de interação: {dict(metricas['contagem_por_tipo_interacao'])}")
        print(f"Tempo total de visualização (s): {metricas['tempo_total_visualizacao']}")
        print(f"Média de tempo de visualização (s): {metricas['media_tempo_visualizacao']}")
        print(f"Comentários: {metricas['comentarios']}")
        print("\n" + "-"*50)
    print("Fim da análise de engajamento.\n")
    print("Obrigado por usar o script de análise de engajamento da Globo!\n")

if __name__ == "__main__":
    main()
