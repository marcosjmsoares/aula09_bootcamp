import pandas as pd
import os 
import glob
import pandera as pa

#um funcao de extract que le e consolida no json
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivo_json = glob.glob(os.path.join(pasta,'*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivo_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

#print(df_total)
#print(arquivo_json) ##imprimir nome dos arquivos
#print(df_list) ##imprime os dados dos arquivos
#pd.read_json(path_or_buf=)

# uma funcao que transforma

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame: 
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


# uma funcao que da load em csv ou parquet

def carregar_dados(df: pd.DataFrame, formato_saida: list):
    """
    parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)
    return carregar_dados


def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)


#if __name__ == "__main__":
    