from sklearn.linear_model import LinearRegression
import matplotlib
import matplotlib.pyplot as plt
plt.style.use("ggplot")
matplotlib.rcParams['figure.figsize'] = (12.8, 7.2)
matplotlib.rcParams['figure.dpi'] = 70
matplotlib.rcParams['axes.titlesize'] = 16
matplotlib.rcParams['axes.labelsize'] = 12
import numpy as np

def tLabels(textX="", textY="", titleText=""):
    plt.xlabel(textX, fontweight ='bold', loc="left")
    plt.ylabel(textY, fontweight ='bold', rotation=0, loc="top")
    plt.title(label=titleText, fontweight ='bold')

def gBar(func, serie):
    eje_x = np.arange(serie.index.size)
    eje_y = serie.values
    graph = plt.bar(eje_x, eje_y)
    plt.xticks(eje_x, serie.index, rotation=360)

    """Funcion para agregar una etiqueta con el valor en cada barra"""
    for rect in graph:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def gBarH(func, serie):
    y = serie.index
    y_pos = np.arange(serie.index.size)
    performance = serie.values
    hbars = plt.barh(y_pos, performance, tick_label=y)
    plt.bar_label(hbars, fmt='%i')

def gPie(func, values, names):
    plt.pie(values, autopct="%0.2f %%", colors=["darkgray", "aqua"])
    plt.legend(names, fontsize=14, loc='upper right', bbox_to_anchor=(1.2, 1))
    plt.show()

def scatterReg(func, dataframe):
    rating = [[x] for x in dataframe['Rating']]
    salario = [[x] for x in dataframe['salary']]

    plt.scatter(dataframe.Rating.values, dataframe.salary.values, color="blue")
    linreg = LinearRegression()
    linreg.fit(rating, salario) 
    y_pred = linreg.predict(rating)
    plt.plot(rating, y_pred, 'r')  # Dibuja un gráfico de línea
    plt.show()
