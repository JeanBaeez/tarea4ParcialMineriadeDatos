from re import X
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt


# 1. Cargar el archivo 'netflix_title.csv'
data = pd.read_csv("./netflix_titles.csv")

print(data)


# 2. Visualizar los primeros 10 registros del conjunto de datos
print(data.head(10))

# 3. Visualizar los últimos 15 registros del conjunto de datos
print(data.tail(15))

# 4. Generar los estadísticos básicos
print(data.describe())

# 5. Completar todos los datos vacíos(na) con ceros(0)
data.fillna(0)


# 6. Generar un gráfico de tipo barras que compare películas vs series desde el 2010 hasta el 2021. El resultado del grafico debe ser algo asi:


data = data.loc[data['release_year'].isin(
    [*range(2010, 2022)]), ['type', 'release_year']].copy()
data.dropna(inplace=True)
data['release_year'] = data['release_year'].astype('int')

cross_tab_prop = pd.crosstab(index=data['release_year'],
                             columns=data['type'],
                             normalize="index")


cross_tab = pd.crosstab(index=data['release_year'],
                        columns=data['type'])


cross_tab.plot(kind='bar',

                    figsize=(10, 5))


plt.legend(loc="upper left", ncol=2)
plt.xlabel("Release Year")
plt.ylabel("Conteo por año")
plt.show()
