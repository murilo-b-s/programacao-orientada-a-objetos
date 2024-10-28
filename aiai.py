import mysql.connector

# Conecte ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",  # Usuário padrão do MySQL no XAMPP
    password="",  # Geralmente a senha padrão é vazia
    database="meu_banco"  # Nome do seu banco de dados
)

# Crie um cursor para executar consultas SQL
cursor = conexao.cursor()

# Exemplo de uma consulta SQL para obter dados de uma tabela
cursor.execute("SELECT * FROM sua_tabela")

# Mostre os resultados
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

# Feche a conexão ao finalizar
cursor.close()
conexao.close()