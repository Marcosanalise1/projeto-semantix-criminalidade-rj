from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv( r"C:\Users\marco\Documents\modulo 4\Data\Ready\BaseMunicipioTaxaMes_Limpa.csv" )

X = df[
    [
        "hom_doloso",
        "letalidade_violenta",
        "roubo_rua",
        "roubo_carga",
        "estupro",
        "trafico_drogas"
    ]
]

y = df["roubo_veiculo"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

modelo = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

modelo.fit(
    X_train,
    y_train
)

pred = modelo.predict(X_test)

print(
    "R²:",
    r2_score(y_test, pred)
)

print(
    "MAE:",
    mean_absolute_error(y_test, pred)
)



fi = pd.DataFrame(
    {
        "Variavel": X.columns,
        "Importancia": modelo.feature_importances_
    }
)

fi = fi.sort_values(
    "Importancia",
    ascending=False
)

print(fi)

plt.figure(figsize=(10,8))

plt.scatter(
    y_test,
    pred,
    alpha=0.4
)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red",
    linewidth=2,
    label="Previsão Perfeita"
)

plt.title(
    "Previsão de Taxa de Roubo de Veículos\nValores Reais x Valores Previstos"
)

plt.xlabel(
    "Taxa Real de Roubo de Veículos"
)

plt.ylabel(
    "Taxa Prevista de Roubo de Veículos"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    r"C:\Users\marco\Documents\modulo 4\Data\Ready\real_vs_previsto.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()