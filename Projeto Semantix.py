import pandas as pd
import numpy as np

# =====================
# LEITURA
# =====================

df = pd.read_csv(
    r"C:\Users\marco\Documents\modulo 4\Data\Raw\BaseMunicipioTaxaMes.csv",
    sep=";",
    decimal=",",
    encoding="latin1"
)

# =====================
# PADRONIZAÇÃO
# =====================

df.columns = (
    df.columns
    .str.lower()
    .str.strip()
)

# =====================
# DATA
# =====================

df["data"] = pd.to_datetime(
    df["mes_ano"],
    format="%Ym%m"
)

# =====================
# REMOVER DUPLICADOS
# =====================

df = df.drop_duplicates()

# =====================
# NULOS
# =====================

numericas = df.select_dtypes(include=np.number).columns

df[numericas] = df[numericas].fillna(0)

# =====================
# CATEGÓRICAS
# =====================

categoricas = [
    "fmun",
    "regiao"
]

for col in categoricas:
    df[col] = df[col].str.strip()

# =====================
# VERIFICAÇÕES
# =====================

print(df.info())

print(df.isnull().sum())

print(df.shape)

# =====================
# SALVAR BASE LIMPA
# =====================

df.to_csv(
    r"C:\Users\marco\Documents\modulo 4\Data\Ready\BaseCriminalidadeLimpa.csv",
    index=False
)

print("ETL concluído.")



# =====================
# TRATAMENTO REGIÃO
# =====================

df["regiao"] = df["regiao"].fillna("Não Informado")

# =====================
# REMOVER DUPLICADOS
# =====================

print("Duplicados:", df.duplicated().sum())

df = df.drop_duplicates()

# =====================
# VERIFICAÇÃO FINAL
# =====================

print(df.describe())

# =====================
# EXPORTAÇÃO FINAL
# =====================

df.to_csv(
    r"C:\Users\marco\Documents\modulo 4\Data\Ready\BaseMunicipioTaxaMes_Limpa.csv",
    index=False
)

print("Base de dados limpa salva com sucesso.")