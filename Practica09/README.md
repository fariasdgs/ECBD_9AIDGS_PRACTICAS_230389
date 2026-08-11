# Práctica 09: Segmentación de clientes con K-Means

## Portada

| Dato | Información |
| --- | --- |
| **Institución** | Universidad Tecnológica de Xicotepec de Juárez |
| **Asignatura** | Análisis de Datos para Negocios Digitales |
| **Unidad** | Unidad 4 — Aprendizaje no supervisado |
| **Estudiante** | Al Farias Leyva |
| **Matrícula** | 230389 |
| **Grupo** | 9A IDGS |
| **Fecha** | 11 de agosto de 2026 |
| **Notebook original** | [Unsupervised Learning: 3-6 Clusters \| K-Means \| EDA](https://www.kaggle.com/code/tanmay111999/unsupervised-learning-3-6-clusters-k-means-eda) |
| **Repositorio** | [ECBD_9AIDGS_PRACTICAS_230389](https://github.com/fariasdgs/ECBD_9AIDGS_PRACTICAS_230389) |

## Objetivo

Aplicar K-Means para segmentar clientes de un centro comercial a partir de edad, ingreso anual y puntuación de gasto. Se comparan datos originales y normalizados, seleccionando el número de clústeres mediante el método del codo y el coeficiente de silueta.

## Contenido del análisis

- Inspección, limpieza y validación de `Mall_Customers.csv`.
- Estadística descriptiva y análisis exploratorio.
- Codificación de género sin interpretación ordinal.
- Normalización con `StandardScaler`.
- Tres combinaciones de variables en versión original y normalizada.
- Evaluación de `k=2` a `k=10` mediante inercia y silueta.
- Seis modelos finales con centroides y métricas.
- Perfiles de clientes, comparación y limitaciones.

## Archivos

| Archivo | Descripción |
| --- | --- |
| [Practica_09_KMeans_230389.ipynb](./Practica_09_KMeans_230389.ipynb) | Notebook documentado y ejecutado |
| [Mall_Customers.csv](./Mall_Customers.csv) | Dataset de 200 clientes descargado de [Kaggle](https://www.kaggle.com/datasets/kandij/mall-customers) |
| [EVIDENCIA_EJECUCION.md](./EVIDENCIA_EJECUCION.md) | Resumen de la ejecución y modelos finales |
| [requirements.txt](./requirements.txt) | Dependencias mínimas |

## Ejecución

Desde la raíz del repositorio:

```bash
python3 -m pip install -r Practica09/requirements.txt
jupyter notebook Practica09/Practica_09_KMeans_230389.ipynb
```

Ejecutar todas las celdas en orden mediante **Kernel → Restart & Run All**.

## Estado

Práctica completada. El Notebook fue ejecutado completamente: 25 celdas de código en orden, cero errores y 10 comprobaciones automáticas correctas.
