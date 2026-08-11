# Práctica 08: Scatter Plot 3D con sprites de Pokémon

## Portada

| Dato | Información |
| --- | --- |
| **Estudiante** | Al Farias Leyva |
| **Matrícula** | 230389 |
| **Grupo** | 9A IDGS |
| **Fecha** | 11 de agosto de 2026 |
| **Asignatura** | Análisis de Datos para Negocios Digitales |
| **Título** | Scatter Plot 3D con sprites de Pokémon |
| **Repositorio de Git** | [ECBD_9AIDGS_PRACTICAS_230389](https://github.com/fariasdgs/ECBD_9AIDGS_PRACTICAS_230389) |

## Objetivo

Analizar un conjunto de datos con estadísticas de Pokémon mediante Python, Pandas, NumPy y Plotly, aplicando procesos de inspección, limpieza y análisis estadístico para construir una visualización tridimensional interactiva. La gráfica relacionará la generación, el tipo principal y el promedio de estadísticas de cada Pokémon, incorporando colores, información emergente, filtros y sprites para facilitar la identificación e interpretación de patrones y valores atípicos.

## Descripción

La práctica utiliza un dataset de Pokémon que contiene información como nombre, tipos, generación, puntos de salud, ataque, defensa, ataque especial, defensa especial y velocidad. Antes de generar la visualización se revisarán y normalizarán los datos, se calculará la columna `promedio_estadisticas` y se obtendrán estadísticas descriptivas.

El resultado principal será un Scatter Plot 3D interactivo exportado en formato HTML. Cada punto representará un Pokémon y permitirá consultar su nombre, tipo, generación, promedio de estadísticas y sprite.

## Archivos de la práctica

La carpeta quedará organizada de la siguiente manera cuando se agreguen los archivos del análisis:

```text
Practica08/
├── README.md
├── practica08_pokemon_230389.ipynb
├── pokemon.csv
└── scatterplot_3d_pokemon.html
```

Los nombres del Notebook, dataset y archivo HTML pueden ajustarse a los nombres reales de los archivos utilizados.

## Tecnologías

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Plotly

## Ejecución

Desde la raíz del repositorio, instalar las dependencias necesarias:

```bash
python3 -m pip install pandas numpy plotly jupyter
```

Después, iniciar Jupyter Notebook:

```bash
jupyter notebook Practica08/
```

Abrir el archivo `.ipynb` y ejecutar todas las celdas en orden. Al finalizar, se debe comprobar que el Scatter Plot 3D funcione correctamente y que la exportación HTML conserve la interactividad.

## Lista de verificación de la rúbrica

| Criterio | Firmas | Estado |
| --- | :---: | :---: |
| Portada con estudiante, grupo, fecha, título y objetivo | 2 | ✅ |
| Importación de Pandas, NumPy y Plotly | 2 | ⬜ |
| Carga y descripción del origen y contenido del dataset | 3 | ⬜ |
| Inspección mediante `head()`, `shape`, `info()` y `describe()` | 2 | ⬜ |
| Limpieza de columnas y valores categóricos | 3 | ⬜ |
| Tratamiento de nulos, duplicados y datos incorrectos | 2 | ⬜ |
| Selección y justificación de las variables estadísticas | 3 | ⬜ |
| Creación de `promedio_estadisticas` | 2 | ⬜ |
| Media, mediana, mínimo, máximo y desviación estándar | 4 | ⬜ |
| Preparación de generación y tipo principal | 3 | ⬜ |
| Obtención y validación de sprites | 2 | ⬜ |
| Primera versión del Scatter Plot 3D | 3 | ⬜ |
| Diferenciación visual por tipo principal | 3 | ⬜ |
| Información emergente personalizada | 2 | ⬜ |
| Integración de sprites | 3 | ⬜ |
| Filtros interactivos | 2 | ⬜ |
| Personalización del diseño de la gráfica | 3 | ⬜ |
| Tres hallazgos relevantes | 2 | ⬜ |
| Exportación interactiva en HTML | 2 | ⬜ |
| Conclusiones y ejecución completa sin errores | 2 | ⬜ |
| **Total** | **50** | |

## Resultados esperados

- Dataset limpio y documentado.
- Columna `promedio_estadisticas` calculada correctamente.
- Resumen estadístico de las variables seleccionadas.
- Scatter Plot 3D con colores por tipo de Pokémon.
- Información emergente con los datos principales de cada Pokémon.
- Sprites relacionados con los puntos de la visualización.
- Filtros por generación, tipo o rango de estadísticas.
- Visualización exportada como HTML interactivo.
- Al menos tres hallazgos y una conclusión final.

## Estado actual

La estructura y la documentación inicial de la práctica están listas. Está pendiente agregar y revisar el Notebook, el dataset utilizado y la visualización HTML exportada.

---

**Autor:** Al Farias Leyva  
**Matrícula:** 230389
