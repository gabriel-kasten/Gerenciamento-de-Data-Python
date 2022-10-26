import pandas as pd

df = pd.read_excel("Base_de_dados.xlsx")

def qnt_clientes():
    df_filtrada = df['codigo_cliente'].drop_duplicates()
    qnt_clientes = df_filtrada.count()
    print(qnt_clientes)

def qnt_asessores():
    df_filtrada = df['codigo_assessor'].drop_duplicates()
    qnt_asessores = df_filtrada.count()
    print (qnt_asessores)

def custodia_total():
    custodia_total = df['custodia'].sum()
    print(custodia_total)

# def custodia_total_asessores():
#

def custodia_media():
    custodia_media = df['custodia'].median()
    print(custodia_media)

def idade_media():
    idade_media = df['idade'].median()
    print(idade_media)

qnt_clientes()
qnt_asessores()
custodia_total()
custodia_media()
idade_media()


