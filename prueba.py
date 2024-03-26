import pandas as pd

# Leer los archivos
archivo_principal = pd.read_excel('Articulos_Zalando_v3.xlsx')
archivo_combinado = pd.read_excel('SalesAndStock.xlsx')

# Convertir la columna 'Modelo' en el archivo principal a tipo object (cadena)
archivo_principal['Modelo'] = archivo_principal['Modelo'].astype('object')

# Iterar sobre las filas del archivo principal
for index, row in archivo_principal.iterrows():
    # Obtener el valor de Articulo en la fila actual
    articulo_actual = row['Articulo']

    # Buscar el valor de Articulo en el archivo combinado (ignorar espacios y convertir a minúsculas)
    fila_combinado = archivo_combinado.loc[archivo_combinado['Articulo'].str.strip().str.lower() == articulo_actual.strip().lower()]

    # Verificar si se encontró una coincidencia
    if not fila_combinado.empty:
        # Copiar los valores de Modelo y Stock al archivo principal
        archivo_principal.at[index, 'Modelo'] = fila_combinado['Modelo'].values[0]
        archivo_principal.at[index, 'Stock'] = fila_combinado['Stock'].values[0]

# Guardar el archivo principal actualizado
archivo_principal.to_excel('Articulos_Zalando_Actualizado.xlsx', index=False)
