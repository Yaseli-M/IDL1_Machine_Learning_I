# IDL1 & IDL2 - Machine Learning I  

Repositorio de entregas para la materia **Machine Learning I**.  
Incluye el desarrollo de los **casos prácticos IDL1 (aprendizaje supervisado)** e **IDL2 (aprendizaje no supervisado)**.

---

## 📂 Estructura del proyecto

IDL1_Machine_Learning_I/
│
├── data/ # Datasets utilizados
│ └── historial_compras.csv # Dataset real de clientes (IDL2)
│
├── notebooks/ # Notebooks del caso IDL1
│ └── exploracion_datos.ipynb
│
├── notebooks_IDL2/ # Notebooks del caso IDL2
│ ├── 01_exploracion_datos.ipynb
│ ├── 02_clustering.ipynb
│ └── 03_pca.ipynb
│
├── resultados_modelos/ # Resultados de IDL1
│ ├── clasificacion/
│ └── regresion/
│
├── resultados_IDL2/ # Resultados y gráficos de IDL2
│ ├── clustering/
│ │ ├── kmeans_clusters.png
│ │ └── dbscan_clusters.png
│ ├── pca/
│ │ └── pca_2d.png
│ ├── clientes_segmentados.csv
│ └── pca_clientes.csv
│
├── scripts/ # Scripts del caso IDL1
├── scripts_IDL2/ # Scripts auxiliares del caso IDL2
│
├── requirements.txt
└── README.md


---

## 📘 Caso práctico IDL1 - Aprendizaje Supervisado  

**Objetivos**:
- Implementar un modelo de **clasificación** (Random Forest).
- Implementar un modelo de **regresión lineal y polinómica**.
- Evaluar con métricas adecuadas (Matriz de confusión, ROC, R², RMSE).
- Presentar resultados con gráficos.

**Resultados principales**:
- Se logró un modelo de clasificación con buen desempeño en predicción de compra/no compra.
- En regresión, se ajustaron modelos lineales y polinómicos para predecir ventas futuras.

Los notebooks se encuentran en `notebooks/` y los resultados exportados en `resultados_modelos/`.

---

## 📘 Caso práctico IDL2 - Aprendizaje No Supervisado  

**Objetivos**:
1. Aplicar **algoritmos de clustering** (K-Means y DBSCAN).
2. Reducir dimensionalidad con **PCA**.
3. Evaluar con métricas como **coeficiente de silueta** y **varianza explicada**.
4. Analizar resultados y proponer recomendaciones prácticas.

**Metodología**:
- Dataset utilizado: `data/historial_compras.csv` (clientes, compras totales, frecuencia y monto promedio).  
- Se estandarizaron las variables y se aplicaron:
  - **K-Means**: identificación de segmentos de clientes con patrones claros.
  - **DBSCAN**: detección de posibles valores atípicos.
- Se utilizó **PCA** para reducir a 2D y facilitar la visualización de clusters.

**Resultados principales**:
- Gráficos de clusters con K-Means y DBSCAN (`resultados_IDL2/clustering/`).
- Gráfico PCA con varianza acumulada y visualización de clientes (`resultados_IDL2/pca/`).
- CSVs con clientes segmentados y datos transformados.

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Yaseli-M/IDL1_Machine_Learning_I.git
   cd IDL1_Machine_Learning_I
