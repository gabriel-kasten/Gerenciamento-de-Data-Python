import pandas as pd

df = pd.read_excel("Base_de_dados.xlsx")

def qnt_clientes():
    df_filtrada = df['codigo_cliente'].drop_duplicates()
    qnt_clientes = df_filtrada.count()
    print(f'Quantidade de clientes no banco: {qnt_clientes}')

def qnt_asessores():
    df_filtrada = df['codigo_assessor'].drop_duplicates()
    qnt_asessores = df_filtrada.count()
    print (f'Quantidade de assessores no banco: {qnt_asessores}')

def custodia_total():
    custodia_total = df['custodia'].sum()
    print(f'Custódia total dos clientes no banco: R${custodia_total:,.2f}')

def custodia_media():
    custodia_media = df['custodia'].median()
    print(f'Custódia média dos clientes no banco: R${custodia_media:,.2f}')

def idade_media():
    idade_media = df['idade'].median()
    print(f'Idade média dos clientes no banco: {int(idade_media)} anos')

# def custodia_total_asessores():

# Não consegui completar essa questão, então deixei minha linha de raciocínio final.
# Obrigado pela oportunidade de qualquer forma

# coletar row codigo_assessores
# coletar row custodia
# separar assessores com mais de um cliente em array separado
# o array duplicado concatena com o primeiro array somando a custodia dos clientes

qnt_clientes()
qnt_asessores()
custodia_total()
custodia_media()
idade_media()
# custodia_total_asessores()
