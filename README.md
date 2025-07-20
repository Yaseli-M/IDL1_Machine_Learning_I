# IDL1_Machine_Learning_I
Este proyecto tiene como objetivo el desarrollo de modelos de Machine Learning aplicados a un conjunto de datos sintético que simula el comportamiento de compra de clientes en una tienda de productos electrónicos.

# Objetivos

- Generar un dataset sintético de clientes y su comportamiento de compra.
- Realizar análisis exploratorio de datos (EDA).
- Aplicar modelos de regresión (lineal y polinómica) para predecir el monto de venta.
- Implementar un modelo de clasificación (Random Forest) para predecir si un cliente comprará.
- Evaluar los modelos y guardar los resultados.

# 📁 Estructura del Proyecto
IDL1_Machine_Learning_I/
│
├── **data_sintetica/** # Dataset sintético generado
├── **notebooks/** # Notebooks con análisis exploratorio
│ └── *exploracion_datos.ipynb*
├── **resultados_modelos/** # Resultados y predicciones exportadas
│ ├── *regresion/*
│ ├── *clasificacion/*
├── **scripts/** # Scripts de modelos
│ ├── *generar_dataset.py*
│ ├── *modelo_regresion_lineal.ipynb*
│ ├── *modelo_regresion_polinomica.ipynb*
│ └── *modelo_clasificacion_rf.ipynb*
├── **venv_IDL1_ML_I/** # Entorno virtual (ignorado por git)
├── **.gitignore**
├── **README.md**
└── **requirements.txt**

# Tecnologías y librerías
    - Python 3.x
    - pandas, numpy
    - scikit-learn
    - matplotlib, seaborn
    - Jupyter Notebooks
    - Joblib

# Descripción de los modelos

- **Regresión Lineal**: Predice el `monto_venta` a partir de variables como edad, ingresos, visitas web, etc.
- **Regresión Polinómica**: Usa variables transformadas polinómicamente para mejorar el ajuste del modelo.
- **Clasificación Random Forest**: Predice la probabilidad de que un cliente realice una compra (`compra` = 1 - `no compra` = 0).

# Dataset Sintético
- Generado con `sklearn.datasets.make_classification`.
- 10,000 clientes simulados.
- Variables: edad, ingresos, visitas web, tiempo web, productos vistos, promociones usadas.
- Variables objetivo: `compra` (clasificación), `monto_venta` (regresión).

##  ¿Cómo ejecutar el proyecto?

1. **Clonar el repositorio:**

   cmder
   git clone https://github.com/Yaseli-M/IDL1_Machine_Learning_I.git
   cd IDL1_Machine_Learning_I

2. **Crear y activar el entorno virtual:**

    python -m venv venv_IDL1_ML_I
    venv_IDL1_ML_I\Scripts\activate

3. **Instalar dependencias:**

    pip install -r requirements.txt

4. **Ejecutar scripts y notebooks:**

    - **Generar datos:** python scripts/generar_dataset.py

    - **Regresión lineal:** scripts/modelo_regresion_lineal.ipynb

    - **Regresión polinómica:** scripts/modelo_regresion_polinomica.ipynb

    - **Clasificación RF:** scripts/modelo_clasificacion_rf.ipynb

    - **Exploración:** notebooks/exploracion_datos.ipynb

# AUTOR: 
Proyecto desarrollado por Yaseli Mendez. para el curso Machine Learning I - IDL1