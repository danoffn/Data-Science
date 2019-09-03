import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_graph(df, cols=4, var_numericas=[], var_categoricas=[],
              sub_width=5, sub_height=5, porcentaje=True):
    """
    grid_plot_batch: Genera una grilla con distintos tipos de gráficos para
    cada conjunto de variables. El tipo de gráfico dependerá del tipo de datos
    en la serie. Para datos numéricos, utiliza distplot; para datos categéricos
    utiliza countplot. La clasificación de tipo de datos se realiza
    automáticamente o puede ser definida a usando una lista con var_categoricas
    o var_numericas

    Parámetros de ingreso:
        - df: un objeto pd.DataFrame
        - cols: cantidad de columnas en la grilla.
        - var_numericas: lista con nombres de columnas del tipo numérica.
        - var_categoricas: lista con nombres de columnas del tipo categoricas.
        - sub_width: ancho de subplot.
        - sub_height: alto de subplot.
        - Porcentaje: grafica el porcentaje de las variables categóricas

    Retorno:
        - Una grilla generada con sns.distplot y sns.countplot dependiendo del
        tipo de datos en la serie.

    """

    if len(var_numericas) == 0:
        var_numericas = list(
            df.select_dtypes(include=["float64", "int64"]).columns
        )
    var_numericas.sort()

    rows = np.ceil(len(var_numericas) / cols)

    plt.figure(figsize=(cols * sub_width, rows * sub_height))

    for index, col_name in enumerate(var_numericas):
        plt.subplot(rows, cols, index + 1)
        g = sns.distplot(df[col_name], color="green")
        plt.axvline(np.mean(df[col_name]), color='tomato')
        plt.title(col_name, fontsize=16)
        plt.xlabel('')
        plt.ylabel('')
        for item in g.get_xticklabels():
            item.set_rotation(30)

    plt.tight_layout()

    if len(var_categoricas) == 0:
        var_categoricas = list(
            df.select_dtypes(include=["object"]).columns
        )

    var_categoricas.sort()

    rows = np.ceil(len(var_categoricas) / cols)

    plt.figure(figsize=(cols * sub_width, rows * sub_height))

    for index, col_name in enumerate(var_categoricas):
        plt.subplot(rows, cols, index + 1)
        value_count = df[col_name].value_counts(
            normalize=porcentaje,
            ascending=True
            )
        g = sns.barplot(value_count.index,
                        value_count.values,
                        palette="Greens"
                        )
        plt.title(col_name + " count", fontsize=16)
        plt.xlabel('')
        plt.ylabel('')
        for item in g.get_xticklabels():
            item.set_rotation(45)
    plt.tight_layout()


def plot_class_report(class_report, title):
    plt.figure()
    plt.plot(class_report.loc["precision", ["1"]], [
             1], marker='x', color="tomato", label="Clase 1")
    plt.plot(class_report.loc["precision", ["0"]], [
             1], marker='x', color="green", label="Clase 0")
    plt.plot(class_report.loc["recall", ["1"]],
             [2], marker='x', color="tomato")
    plt.plot(class_report.loc["recall", ["0"]], [2], marker='x', color="green")
    plt.plot(class_report.loc["f1-score", ["1"]],
             [3], marker='x', color="tomato")
    plt.plot(class_report.loc["f1-score", ["0"]],
             [3], marker='x', color="green")
    plt.axvline(0.5, linestyle="--", color="gray", label="azar")
    plt.xlim((0, 1.0))
    plt.yticks([1, 2, 3], ['Precision', 'Recall', 'F1-Score'])
    plt.legend()
    plt.title(title)
