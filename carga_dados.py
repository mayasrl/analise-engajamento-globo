import csv
import mysql.connector
from datetime import datetime
from mysql.connector import Error

def conectar_banco():
    """
    Conecta ao banco de dados MySQL
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='globo_tech',
            user='root',
            password='password'  # Altere conforme necessário
        )
        if connection.is_connected():
            print("Conexão com MySQL estabelecida com sucesso")
            return connection
    except Error as e:
        print(f"Erro ao conectar com MySQL: {e}")
        return None

def obter_id_plataforma(cursor, nome_plataforma):
    """
    Obtém o ID da plataforma pelo nome
    """
    cursor.execute("SELECT id_plataforma FROM plataforma WHERE nome_plataforma = %s", (nome_plataforma,))
    resultado = cursor.fetchone()
    return resultado[0] if resultado else None

def obter_id_tipo_interacao(cursor, tipo_interacao):
    """
    Obtém o ID do tipo de interação pelo nome
    """
    cursor.execute("SELECT id_tipo_interacao FROM tipo_interacao WHERE nome_tipo = %s", (tipo_interacao,))
    resultado = cursor.fetchone()
    return resultado[0] if resultado else None

def carregar_dados_csv(arquivo_csv):
    """
    Carrega dados do CSV para o banco de dados
    """
    connection = conectar_banco()
    if not connection:
        return
    
    cursor = connection.cursor()
    
    try:
        with open(arquivo_csv, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            usuarios_inseridos = set()
            conteudos_inseridos = set()
            
            for row in csv_reader:
                # Inserir usuário se não existir
                id_usuario = int(row['id_usuario'])
                if id_usuario not in usuarios_inseridos:
                    cursor.execute("""
                        INSERT IGNORE INTO usuario (id_usuario, nome_usuario) 
                        VALUES (%s, %s)
                    """, (id_usuario, f"Usuario_{id_usuario}"))
                    usuarios_inseridos.add(id_usuario)
                
                # Inserir conteúdo se não existir
                id_conteudo = int(row['id_conteudo'])
                nome_conteudo = row['nome_conteudo']
                if id_conteudo not in conteudos_inseridos:
                    cursor.execute("""
                        INSERT IGNORE INTO conteudo (id_conteudo, nome_conteudo) 
                        VALUES (%s, %s)
                    """, (id_conteudo, nome_conteudo))
                    conteudos_inseridos.add(id_conteudo)
                
                # Obter IDs das tabelas relacionadas
                id_plataforma = obter_id_plataforma(cursor, row['plataforma'])
                id_tipo_interacao = obter_id_tipo_interacao(cursor, row['tipo_interacao'])
                
                if not id_plataforma:
                    print(f"Plataforma não encontrada: {row['plataforma']}")
                    continue
                    
                if not id_tipo_interacao:
                    print(f"Tipo de interação não encontrado: {row['tipo_interacao']}")
                    continue
                
                # Converter timestamp
                timestamp_str = row['timestamp_interacao']
                timestamp = datetime.fromtimestamp(int(timestamp_str))
                
                # Inserir relação conteúdo-plataforma se não existir
                cursor.execute("""
                    INSERT IGNORE INTO conteudo_plataforma (id_conteudo, id_plataforma)
                    VALUES (%s, %s)
                """, (id_conteudo, id_plataforma))
                
                # Inserir interação
                watch_duration = int(row['watch_duration_seconds']) if row['watch_duration_seconds'] else None
                comment_text = row['comment_text'] if row['comment_text'] else None
                
                cursor.execute("""
                    INSERT INTO interacao 
                    (id_usuario, id_conteudo, id_plataforma, id_tipo_interacao,
                     timestamp_interacao, watch_duration_seconds, comment_text)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (id_usuario, id_conteudo, id_plataforma, id_tipo_interacao,
                      timestamp, watch_duration, comment_text))
        
        connection.commit()
        print("Dados carregados com sucesso!")
        
    except Error as e:
        print(f"Erro ao carregar dados: {e}")
        connection.rollback()
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão com MySQL encerrada")

if __name__ == "__main__":
    # Carregar dados do CSV
    carregar_dados_csv('interacoes_globo.csv')

