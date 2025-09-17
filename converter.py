import csv
import json

# Caminho do seu CSV
csv_file = 'relação SKUs.csv'
# Caminho do JSON que será criado/atualizado
json_file = 'produtos 2.json'

produtos = []

# Lendo o CSV
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Cria um dicionário no formato do JSON
        produto = {
            "skuErp": row['skuErp'],
            "skuSite": row['skuSite'],
            "descricao": row['descricao']
        }
        produtos.append(produto)

# Salvando em JSON
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(produtos, f, ensure_ascii=False, indent=4)

print(f"{len(produtos)} produtos exportados para {json_file}")
