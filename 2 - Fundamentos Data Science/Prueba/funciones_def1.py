import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def graficar(df, variable):

    temp = df[variable]
    temp = temp.dropna()

    plt.figure()
    plt.title(variable)

    sns.distplot(temp, rug=True, )
    plt.axvline(temp.mean(), color='tomato', linestyle='--', label='mean')
    plt.axvline(temp.median(), color='tomato', linestyle='-', label='median')
    plt.legend()
