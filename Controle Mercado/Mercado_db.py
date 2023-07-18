import mysql.connector
con =  mysql.connector.connect(host='localhost',database='db_teste',user='root',password='123456!')
cursor = con.cursor()
print('Bem vindo ao Supermercado Takanado')
x = input('Deseja cadastrar novos produtos ?[S/N]').lower()

while x == 's':
    nome_prod = input('Digite o nome do Produto: ')
    valor = int(input('Digite o Valor do produto: '))
    comando = f'INSERT INTO  vendas (nome_prod, valor) VALUES ("{nome_prod}", {valor})'
    cursor.execute(comando)
    con.commit()
    x = input('Deseja continuar ?[S/N]').lower()

comando = f'SELECT*FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
for i in resultado:
    print (i)
input('Pressione Enter para sair')
