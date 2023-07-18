import mysql.connector
con =  mysql.connector.connect(host='localhost',database='db_teste',user='root',password='F1l1c10!')
cursor = con.cursor()
dec = 's'
id_prod = input('Digite o código do produto:')
while dec == 's':
    comando = f'SELECT nome_prod FROM vendas WHERE id_prod =({id_prod})'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print (resultado)
    dec = input('Deseja continuar?[S/N] ').lower()
    
