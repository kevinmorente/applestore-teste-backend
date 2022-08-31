import pandas as pd
import json
import sqlite3

#Criando um banco de dados e abilitando um cursor
con3 = sqlite3.connect('bddEXECUÇÃO03.db')
cursor = con3.cursor()

#lendo o csv da EXECUÇÃO-02, executar o indexEx3 so quando o indexEx2 tiver sido executado.
tabela = pd.read_csv(
    "EXECUÇÃO-02.csv",
    encoding = 'utf-8',
)

#Pegando o CSV da EXECUÇÃO-02 e ordenando de forma crescente o id.
tabela_out_ex03 = (tabela.sort_values('id').head(10))

#Colocando a tabela da EXECUÇÃO-03 reorganizada para CSV
tabela_out_ex03.to_csv("EXECUÇÃO-03.csv")

#Printando no terminal com a finalidade de ver a saida.
print(tabela_out_ex03)

#Lendo o csv criado e criando um json.
pd.read_csv('EXECUÇÃO-03.csv', encoding = 'utf-8').to_json('EXECUÇÃO-03.json',indent=4, orient='records')

#Criando a tabela no banco de dados para colocar as informacoes, executar apenas uma vez, caso for rodar novamento comentar as 2 linhas abaixo
cursor.execute("CREATE TABLE 'TabelaBddExecucao03' (id NUMERIC, track_name TEXT, size_bytes NUMERIC, price NUMERIC, prime_genre TEXT) ")
con3.commit()

#Lendo a API da EXECUÇÃO-03 criada.
with open("EXECUÇÃO-03.json", encoding = 'utf-8') as ex3_json: dados03 = json.load(ex3_json)

#Colocando os dados no Banco de dados SQL
for i in dados03: 
    t_id = i['id']
    t_track_name = i['track_name']
    t_size_bytes = i['size_bytes']
    t_price = i['price']
    t_prime_genre = i['prime_genre']
    cursor.execute(f"INSERT INTO TabelaBddExecucao03 VALUES ({t_id}, '{t_track_name}', {t_size_bytes}, {t_price}, '{t_prime_genre}')")
    con3.commit()