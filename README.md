# Análise da Criminalidade nos Municípios do Estado do Rio de Janeiro (2014–2024)

## Sobre o Projeto

Este projeto foi desenvolvido como parte do desafio de parceria entre a EBAC e a Semantix.

O objetivo foi analisar a evolução da criminalidade nos municípios do Estado do Rio de Janeiro utilizando técnicas de análise exploratória de dados, visualização de informações e aprendizado de máquina.

---

# Problema

A criminalidade é um dos principais desafios enfrentados pela sociedade brasileira, impactando diretamente a segurança pública, a qualidade de vida da população e o desenvolvimento econômico das regiões afetadas.

Compreender padrões, tendências e diferenças regionais permite apoiar ações mais eficientes de combate à violência.

---

# Objetivos

## Objetivo Geral

Analisar o comportamento dos principais indicadores criminais dos municípios do Estado do Rio de Janeiro entre 2014 e 2024.

## Objetivos Específicos

- Realizar limpeza e tratamento dos dados.
- Identificar tendências temporais.
- Comparar municípios e regiões.
- Avaliar correlações entre indicadores.
- Desenvolver um modelo preditivo para estimar taxas de roubo de veículos.
- Construir um dashboard interativo no Power BI.

---

# Coleta de Dados

## Fonte dos Dados

Instituto de Segurança Pública do Estado do Rio de Janeiro (ISP-RJ).

Base utilizada:

```
BaseMunicipioTaxaMes.csv
```

A base contém indicadores mensais de criminalidade padronizados por 100 mil habitantes para todos os municípios do estado.

### Principais Variáveis

- hom_doloso
- letalidade_violenta
- roubo_rua
- roubo_veiculo
- roubo_carga
- estupro
- trafico_drogas

---

# Modelagem

## ETL

As etapas realizadas foram:

- Leitura da base CSV;
- Padronização de colunas;
- Tratamento de valores nulos;
- Remoção de duplicidades;
- Criação da coluna de data;
- Exportação da base tratada.

### Ferramentas

- Python
- Pandas
- NumPy

---

## Análise Exploratória de Dados

Foram realizadas análises para:

- Evolução temporal dos indicadores;
- Ranking dos municípios;
- Comparação regional;
- Correlação entre crimes;
- Distribuição dos indicadores.

### Gráficos Gerados

- Evolução da Criminalidade;
- Top 10 Municípios por Roubo de Veículos;
- Top 10 Municípios por Homicídios;
- Comparação Regional;
- Heatmap de Correlação;
- Boxplot de Roubo de Veículos.

---

## Machine Learning

### Objetivo

Prever a taxa de roubo de veículos.

### Modelo Utilizado

Random Forest Regressor.

### Variáveis Utilizadas

- hom_doloso
- letalidade_violenta
- roubo_rua
- roubo_carga
- estupro
- trafico_drogas

### Resultados

**R²**

```
0.774
```

O modelo conseguiu explicar aproximadamente 77% da variação observada na taxa de roubo de veículos.

**MAE**

```
7.55
```

O erro médio absoluto foi de aproximadamente 7,55 pontos.

### Principais Variáveis

| Variável | Importância |
|----------|------------|
| roubo_rua | 69,55% |
| roubo_carga | 12,33% |
| trafico_drogas | 5,73% |
| hom_doloso | 4,18% |
| estupro | 4,13% |
| letalidade_violenta | 4,07% |

---

# Dashboard

O dashboard foi desenvolvido em Power BI e contém:

- Visão Geral da Criminalidade;
- Evolução Temporal;
- Ranking dos Municípios;
- Análise Regional;
- Mapa Interativo;
- Resultados do Modelo de Machine Learning.

---

# Conclusões

Os resultados indicaram diferenças significativas entre municípios e regiões do Estado do Rio de Janeiro.

Os principais achados foram:

- Forte relação entre roubo de rua e roubo de veículos;
- Concentração de determinados indicadores em regiões metropolitanas;
- Existência de padrões temporais relevantes;
- Capacidade preditiva satisfatória utilizando Random Forest.

O projeto demonstrou como técnicas de análise de dados podem apoiar a compreensão da criminalidade e contribuir para processos de tomada de decisão baseados em evidências.

---

# Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Power BI

---

# Autor

Marcos Antonio Lima da Silva
