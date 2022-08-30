from turtle import delay
import pandas as pd
import json
import sqlite3
import time

#Criando um banco de dados e abilitando um cursor
con = sqlite3.connect('bddEXECUÇÃO01.db')
cursor = con.cursor()

#lendo o csv bruto.
tabela = pd.read_csv(
    "AppleStore.csv",
    encoding = 'utf-8',
)

#Pegando o csv bruto e filtrando na coluna p_genre apenas os news, depois ordenando de forma decrescente o rating_count_tot.
tabela_out = (tabela[tabela['prime_genre']=='News'].sort_values('rating_count_tot', ascending=False).head(1))

#Retirando as colunas que nao foram pedidas e criando um outro arquivo CSV.
#Obs: no arquivo csv nao temos a coluna n_citacoes como pedido no output do test entao o mesmo nao foi colocado.
tabela_out[['id', 'track_name', 'size_bytes', 'price', 'prime_genre']].to_csv("EXECUÇÃO-01.csv")

#Printando no terminal com a finalidade de ver a saida.
print(tabela_out[['id', 'track_name', 'size_bytes', 'price', 'prime_genre']])

#Lendo o csv criado com filtros/orientado e criando um json.
pd.read_csv('EXECUÇÃO-01.csv', encoding = 'utf-8').to_json('EXECUÇÃO-01.json',indent=4, orient='records')

#Criando a tabela no banco de dados para colocar as informacoes, executar apenas uma vez, caso for rodar novamento comentar as 2 linhas abaixo
cursor.execute("CREATE TABLE 'TabelaBddExecucao01' (id NUMERIC, track_name TEXT, size_bytes NUMERIC, price NUMERIC, prime_genre TEXT) ")
con.commit()

#Lendo a API criada pela execucao-01 do arquivo json
with open("EXECUÇÃO-01.json", encoding = 'utf-8') as ex1_json: dados01 = json.load(ex1_json)


for i in dados01: 
    t_id = i['id']
    t_track_name = i['track_name']
    t_size_bytes = i['size_bytes']
    t_price = i['price']
    t_prime_genre = i['prime_genre']

    cursor.execute(f"INSERT INTO TabelaBddExecucao01 VALUES ({t_id}, '{t_track_name}', {t_size_bytes}, {t_price}, '{t_prime_genre}')")
    con.commit()

    

print(t_id, t_track_name)




#with open ("EXECUÇÃO-01", "r") as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print (row)


#tabela_out_json = json.loads(tabela_out)
#print(tabela_out_json)

#tabela_json_load={"id":tabela_out.id}
#tabela_json=json.loads(tabela_json_load)

#print(tabela_json['id'])