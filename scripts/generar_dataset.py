# importar librerías
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
import os

# Definir carpeta de salida
output_dir = os.path.join(os.path.dirname(__file__), '..', 'data_sintetica')
os.makedirs(output_dir, exist_ok=True)

# Generar datos sintéticos
X, y = make_classification(
    n_samples=10000,         # 10 mil registros
    n_features=6,            # 6 variables predictoras
    n_informative=4,         # 4 relevantes
    n_redundant=1,           # 1 redundante
    n_classes=2,             # Compra: sí o no
    weights=[0.6, 0.4],      # 60% no compran, 40% sí
    random_state=42
)

# Nombres de las columnas
columnas = ['edad', 'ingresos', 'visitas_web', 'tiempo_web', 'productos_vistos', 'promociones_usadas']
df = pd.DataFrame(X, columns=columnas)

# Añadir columna de clasificación (target binario)
df['compra'] = y

# Crear columna ID_Cliente
df.insert(0, 'ID_Cliente', [f"C{str(i).zfill(4)}" for i in range(1, df.shape[0]+1)])

# Ajustar variables para mayor realismo

# Edad: entre 18 y 70 años
df['edad'] = (np.abs(df['edad']) * 10 + 18).clip(18, 70).astype(int)

# Ingresos mensuales: en rango razonable
df['ingresos'] = (np.abs(df['ingresos']) * 2000 + 1000).round(2)

# Monto de venta: solo si el cliente compró
df['monto_venta'] = np.where(
    df['compra'] == 1,
    np.random.uniform(100, 5000, size=df.shape[0]).round(2),
    0.00
)

# Guardar en CSV
output_path = os.path.join(output_dir, 'dataset_compras.csv')
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f" Dataset sintético generado con éxito en:\n{output_path}")

