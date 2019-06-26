import pandas as pd
import numpy as np
from IPython.display import display, Markdown
import matplotlib.pyplot as plt

df = pd.read_csv("qog_std_cs_jan18.csv")
df_full = df 


def descriptiva(dataframe):
    
    for column in dataframe.loc[:, dataframe.dtypes == np.float64].columns:
        print("Variable: " + column)
        print(dataframe[column].describe().round(3))

    # Estadistica descriptiva para variables discretas

    for column in dataframe.loc[:, dataframe.dtypes == object].columns:
        print("Variable: " + column)
        print(dataframe[column].value_counts("%"))


def obs_perdidas(dataframe, columna, print_list=False):
    lista = []
    
    numero_registros = dataframe[columna].shape[0]
    lista_NOK = dataframe.loc[dataframe[columna].isnull()]["ccodealp"].unique()
    numero_NOK = dataframe[columna].isna().sum()
    
    try:
        porcentaje_NOK = (numero_NOK/numero_registros).round(3)
    except:
        porcentaje_NOK = 0
    
    if print_list:
       display(Markdown("#### Columna " + columna))
       print(list(lista_NOK))
        
    return numero_NOK, porcentaje_NOK


def graficar_histograma(dataframe, var, sample_mean=False, true_mean=False):
    df_temp = dataframe[var].dropna()
    plt.figure()
    plt.hist(df_temp, color='k', alpha=0.3)
    plt.title("Histograma de columna '" + var + "'")
    
    if sample_mean:
        plt.axvline(df_temp.mean(), color="tomato", label="Media muestras 50%")
        
    if true_mean:
        plt.axvline(df_full[var].dropna().mean(), linestyle="--", label="Media total muestras")
        
    plt.legend()
    

def graficar_dotplot(dataframe, plt_var, plot_by, global_stat=False, statistic="mean"):
        
    plt.figure()
    
    if statistic == "mean":
        estadistica = "media"
        grupo = dataframe.groupby(plot_by)[plt_var].mean()

    elif statistic == "median":
        estadistica = "mediana"
        grupo = dataframe.groupby(plot_by)[plt_var].median()

    elif statistic == "z_score":
        estadistica = "puntaje Z"
        temp = dataframe.loc[:, [plt_var, plot_by]]
        temp["puntaje_z"] = (temp[plt_var] - temp[plt_var].mean())/temp[plt_var].std(ddof=0)
        grupo = temp.groupby(plot_by)["puntaje_z"]  
        grupo = grupo.mean()
        
        plt.plot(grupo.values, grupo.index, 'o', color='grey')
        plt.title("Gráfico de puntos de la " + estadistica + " de la variable "  + plt_var)


    if global_stat and statistic is 'mean':
        plt.axvline(dataframe[plt_var].mean(), color="tomato", label="Media")
    if global_stat and statistic is 'median':
        plt.axvline(dataframe[plt_var].median(), color="tomato", label="Mediana")
    if global_stat and statistic is 'z_score':
        plt.axvline(grupo.values.mean(), color="tomato", label="Puntaje Z promedio")

    plt.legend()