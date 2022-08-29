import pandas as pd
import json

tabela = pd.read_csv(
    "AppleStore.csv",
    encoding = 'utf-8',
)

#print(tabela[1:2])

tabela_out = (tabela[tabela['prime_genre']=='News'].sort_values('rating_count_tot', ascending=False).head(1))

#Obs: no arquivo csv não temos a coluna n_citacoes como pedido no output do test!
tabela_out[['id', 'track_name', 'size_bytes', 'price', 'prime_genre']].to_csv("EXECUÇÃO-01")

print(tabela_out[['id', 'track_name', 'size_bytes', 'price', 'prime_genre']])

tabela_json_load={"id":tabela_out.id}
tabela_json=json.loads(tabela_json_load)

print(tabela_json['id'])

test
asassas
