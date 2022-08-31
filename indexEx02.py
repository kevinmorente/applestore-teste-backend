import pandas as pd
import json
import sqlite3

#Criando um banco de dados e abilitando um cursor
con2 = sqlite3.connect('bddEXECUÇÃO02.db')
cursor = con2.cursor()

#lendo o csv bruto.
tabela = pd.read_csv(
    "AppleStore.csv",
    encoding = 'utf-8',
)

#Pegando o csv bruto e filtrando na coluna p_genre apenas os Music or Book, depois ordenando de forma decrescente o rating_count_tot.
tabela_out_ex02_flag1 = (tabela[tabela['prime_genre']=='Music'])
tabela_out_ex02_flag2 = (tabela[tabela['prime_genre']=='Book'])
tabela_out_ex02_flag3 = pd.concat([tabela_out_ex02_flag1, tabela_out_ex02_flag2])
tabela_out_ex02_flag3 = (tabela_out_ex02_flag3.sort_values('rating_count_tot', ascending=False).head(10))

#Retirando as colunas que nao foram pedidas e criando um outro arquivo CSV.
#Obs: no arquivo csv nao temos a coluna n_citacoes como pedido no output do test entao o mesmo nao foi colocado.
tabela_out_ex02_flag3[['id', 'track_name', 'size_bytes', 'price', 'prime_genre']].to_csv("EXECUÇÃO-02.csv")
    
#Printando no terminal com a finalidade de ver a saida.
print(tabela_out_ex02_flag3[['id', 'track_name', 'size_bytes', 'price', 'prime_genre']])

#Lendo o csv criado com filtros/orientado e criando um json.
pd.read_csv('EXECUÇÃO-02.csv', encoding = 'utf-8').to_json('EXECUÇÃO-02.json',indent=4, orient='records')

#Criando a tabela no banco de dados para colocar as informacoes, executar apenas uma vez, caso for rodar novamento comentar as 2 linhas abaixo
cursor.execute("CREATE TABLE 'TabelaBddExecucao02' (id NUMERIC, track_name TEXT, size_bytes NUMERIC, price NUMERIC, prime_genre TEXT) ")
con2.commit()

#Lendo a API criada pela execucao-02 do arquivo json
with open("EXECUÇÃO-02.json", encoding = 'utf-8') as ex2_json: dados02 = json.load(ex2_json)

#Colocando os dados no Banco de dados SQL
for i in dados02: 
    t_id = i['id']
    t_track_name = i['track_name']
    t_size_bytes = i['size_bytes']
    t_price = i['price']
    t_prime_genre = i['prime_genre']
    cursor.execute(f"INSERT INTO TabelaBddExecucao02 VALUES ({t_id}, '{t_track_name}', {t_size_bytes}, {t_price}, '{t_prime_genre}')")
    con2.commit()