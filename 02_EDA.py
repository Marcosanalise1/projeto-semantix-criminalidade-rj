import pandas as pd
import matplotlib

# evita abrir janelas
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# =====================================================
# PASTA DE SAÍDA
# =====================================================

OUTPUT_DIR = Path(
    r"C:\Users\marco\Documents\modulo 4\Data\Ready"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# =====================================================
# LEITURA DOS DADOS
# =====================================================

df = pd.read_csv(
    r"C:\Users\marco\Documents\modulo 4\Data\Ready\BaseMunicipioTaxaMes_Limpa.csv"
)

print("\nBase carregada com sucesso!")
print(df.shape)

# =====================================================
# EVOLUÇÃO TEMPORAL
# =====================================================

evolucao = (
    df.groupby("ano")
    [
        [
            "hom_doloso",
            "letalidade_violenta",
            "roubo_rua",
            "roubo_veiculo"
        ]
    ]
    .mean()
)

plt.figure(figsize=(14,8))

for coluna in evolucao.columns:
    plt.plot(
        evolucao.index,
        evolucao[coluna],
        marker="o",
        linewidth=2,
        label=coluna
    )

plt.title(
    "Evolução dos Principais Indicadores Criminais"
)

plt.xlabel("Ano")

plt.ylabel(
    "Taxa Média por 100 mil Habitantes"
)

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "01_evolucao_criminalidade.png",
    dpi=300
)

plt.close()

# =====================================================
# TOP 10 ROUBO DE VEÍCULOS
# =====================================================

top10_roubo = (
    df.groupby("fmun")["roubo_veiculo"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top10_roubo.values,
    y=top10_roubo.index
)

plt.title(
    "Top 10 Municípios com Maior Taxa de Roubo de Veículos"
)

plt.xlabel(
    "Taxa Média por 100 mil Habitantes"
)

plt.ylabel(
    "Município"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "02_top10_roubo_veiculo.png",
    dpi=300
)

plt.close()

# =====================================================
# TOP 10 HOMICÍDIOS
# =====================================================

top_homicidio = (
    df.groupby("fmun")["hom_doloso"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_homicidio.values,
    y=top_homicidio.index
)

plt.title(
    "Top 10 Municípios com Maior Taxa de Homicídio Doloso"
)

plt.xlabel(
    "Taxa Média por 100 mil Habitantes"
)

plt.ylabel(
    "Município"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "03_top10_homicidios.png",
    dpi=300
)

plt.close()

# =====================================================
# ANÁLISE REGIONAL
# =====================================================

regioes = (
    df.groupby("regiao")
    [
        [
            "hom_doloso",
            "roubo_rua",
            "roubo_veiculo"
        ]
    ]
    .mean()
)

plt.figure(figsize=(12,6))

regioes.plot(
    kind="bar",
    figsize=(12,6)
)

plt.title(
    "Comparação dos Indicadores Criminais por Região"
)

plt.xlabel("Região")

plt.ylabel(
    "Taxa Média por 100 mil Habitantes"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "04_comparacao_regioes.png",
    dpi=300
)

plt.close()

# =====================================================
# HEATMAP CORRELAÇÃO
# =====================================================

cols = [
    "hom_doloso",
    "letalidade_violenta",
    "roubo_rua",
    "roubo_veiculo",
    "roubo_carga",
    "estupro",
    "trafico_drogas"
]

plt.figure(figsize=(12,8))

sns.heatmap(
    df[cols].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title(
    "Correlação entre Indicadores Criminais"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "05_heatmap_correlacao.png",
    dpi=300
)

plt.close()

# =====================================================
# BOXPLOT ROUBO VEÍCULO
# =====================================================

plt.figure(figsize=(12,6))

sns.boxplot(
    data=df,
    x="regiao",
    y="roubo_veiculo"
)

plt.title(
    "Distribuição da Taxa de Roubo de Veículos por Região"
)

plt.xlabel("Região")

plt.ylabel(
    "Taxa por 100 mil Habitantes"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "06_boxplot_roubo_veiculo.png",
    dpi=300
)

plt.close()

print("\nGráficos gerados com sucesso!")
print(f"Arquivos salvos em: {OUTPUT_DIR}")