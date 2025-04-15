import pandas as PD
import matplotlib.pyplot as plt
import seaborn as sns
import os

## Cargar el archivo CSV
DataPath = os.path.join(".", "Data" , 'gastos.csv')
df = PD.read_csv(DataPath)

#format of datetime
df['Fecha'] = PD.to_datetime(df['Fecha'], errors='coerce')
print(df.head())

#NULL VALUES
print(f'Datos nulos :  {df.isnull().sum()}')
#DELETE DUPLICATED DATA
df = df.drop_duplicates()

#EDA
print(df.describe())
print(df.info())

total_per_category = df.groupby('Categoria')['Monto'].sum().reset_index()
total_per_user = df.groupby('Usuario')['Monto'].sum().reset_index()
total_per_type = df.groupby('Tipo')['Monto'].sum().reset_index()

plt.figure(figsize=(10, 6))
df.groupby('Categoria')['Monto'].sum().plot(kind='bar', color ='purple')
plt.title('Gasto total por categoría')
plt.ylabel('Monto')
plt.show()

#Evolution of expenses and income 

df['Mes'] = df['Fecha'].dt.to_period('M')
total_por_mes_y_tipo = df.groupby(['Mes', 'Tipo'])['Monto'].sum().unstack()
import matplotlib.pyplot as plt

total_por_mes_y_tipo.plot(kind='line')
plt.title('Evolucion de ingresos y gastos por mes')
plt.ylabel('Monto')
plt.show()

