import pandas as pd
import json

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





#with open ("EXECUÇÃO-01", "r") as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print (row)


#tabela_out_json = json.loads(tabela_out)
#print(tabela_out_json)

#tabela_json_load={"id":tabela_out.id}
#tabela_json=json.loads(tabela_json_load)

#print(tabela_json['id'])