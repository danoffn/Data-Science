import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns

def tipo_variable (DataFrame):
    """La función recibe la base de datos como un DataFrame.
       Retorna la lista con el nombre y tipo de variable"""
    for i in DataFrame.columns:
       print("La variable {} es de tipo {}.".format(i, DataFrame[i].dtype))
       
       
def descripcion_variable (DataFrame):
    """La función recibe la base de datos como un DataFrame.
       Retorna las estadísticas descriptivas de cada variable"""
    for i in DataFrame.columns:        
       print("\n Variable: {} \n \n Estadísticos descriptivos: \n".format(i))
       print(DataFrame[i].describe())

def histograma(df, variable):
    """La función recibe la base de datos como un DataFrame y la variable (continua) a graficar
       Retorna el histograma con una línea vertical indicando donde se ubica la media"""
    temp = df[variable]
    temp = temp.dropna()
    plt.figure()
    plt.title(variable)
    
    sns.distplot(temp, rug=True)
    plt.axvline(temp.mean(), color='tomato', linestyle='--', label='mean')
    plt.axvline(temp.median(), color='tomato', linestyle='-', label='median')
    plt.legend()
    
def distribucion_frecuencias (DataFrame, variable):
     """La función recibe la base de datos como un DataFrame y la variable (discreta) a graficar
       Retorna el gráfico de barra que nos indica la frecuencia de cada ítem"""
     plot = sns.catplot(x=variable, data=DataFrame,kind="count", dodge=False,)
     
def report_scores(vector_pred, vector_valid):
    """La función recibe el vecor de predicción y el vector validado. Devuelde los valores 
    de Error cuadrático medio y R Cuadrado"""
    mse = mean_squared_error(vector_pred, vector_valid).round(0)
    r2 = r2_score(vector_pred, vector_valid).round(2)
    print('Error cuadrático medio: ', mse)
    print('R-cuadrado: ', r2)

    return (mse, r2)