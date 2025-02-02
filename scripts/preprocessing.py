# preprocessing.py

# 📦 Imports principais
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.feature_selection import mutual_info_classif

# 📊 Configurações
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "{:.2f}".format)
sns.set_theme(style="whitegrid")

# 🖼 Configurações de gráficos
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12

# 🧹 Função para limpeza dos dados
def clean_data(df):
    """
    Realiza a limpeza dos dados:
    - Remove duplicados
    - Padroniza textos em colunas categóricas
    - Converte a coluna 'Date' para datetime
    """
    print("🔍 Iniciando a limpeza dos dados...")

    # Remover duplicados
    original_size = df.shape[0]
    df = df.drop_duplicates().reset_index(drop=True)
    print(f"✅ Registros duplicados removidos: {original_size - df.shape[0]}")

    # Padronizar textos
    df.loc[:, "Country"] = df["Country"].str.strip().str.title()
    df.loc[:, "Status"] = df["Status"].str.strip().str.title()
    print("✅ Textos padronizados nas colunas 'Country' e 'Status'.")

    # Converter "Date" para datetime
    df.loc[:, "Date"] = pd.to_datetime(df["Date"])
    print("✅ Coluna 'Date' convertida para datetime.")

    print("🚀 Limpeza dos dados concluída!")
    return df

