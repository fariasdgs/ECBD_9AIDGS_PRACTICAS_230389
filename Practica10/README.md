# Unidad 05 — Machine Learning con Scikit-learn

## Introducción

En esta práctica se desarrolla un modelo que predice si un pasajero del Titanic sobrevivió. El trabajo recorre un flujo básico de Machine Learning: conocer los datos, preparar sus variables, separar ejemplos para entrenamiento y prueba, entrenar un clasificador y evaluar sus predicciones.

## ¿Qué es Machine Learning?

Machine Learning, o aprendizaje automático, es una rama de la inteligencia artificial que permite que un programa encuentre patrones en datos y los utilice para hacer predicciones o tomar decisiones. En lugar de escribir una regla para cada caso posible, se proporcionan ejemplos para que un algoritmo aprenda relaciones útiles.

## ¿Para qué sirve Machine Learning?

Se utiliza, entre otras aplicaciones, para detectar correos no deseados, recomendar productos o películas, reconocer imágenes, estimar precios, identificar operaciones fraudulentas y apoyar diagnósticos. La calidad de sus resultados depende de los datos y de que el modelo sea adecuado para el problema.

## Tipos de aprendizaje

- **Aprendizaje supervisado:** aprende con ejemplos que incluyen la respuesta correcta. Sirve para clasificación y regresión.
- **Aprendizaje no supervisado:** busca estructuras o grupos en datos que no tienen una etiqueta conocida.
- **Aprendizaje por refuerzo:** un agente aprende a actuar mediante recompensas y penalizaciones recibidas al interactuar con un entorno.

Esta práctica utiliza **aprendizaje supervisado de clasificación**, porque `Survived` proporciona la respuesta conocida para cada pasajero del conjunto de entrenamiento.

## Ventajas de Machine Learning

- Encuentra patrones en grandes cantidades de datos.
- Automatiza predicciones que serían difíciles de expresar con reglas fijas.
- Puede mejorar cuando se entrena con más datos representativos.
- Se adapta a problemas de clasificación, regresión, agrupamiento y otras tareas.

## Desventajas de Machine Learning

- Depende de la calidad, cantidad y representatividad de los datos.
- Puede aprender sesgos presentes en la información de entrenamiento.
- Algunos modelos son difíciles de interpretar.
- Una buena evaluación no garantiza el mismo desempeño frente a datos muy diferentes.
- Requiere supervisión para evitar conclusiones incorrectas o usos fuera de contexto.

## Scikit-learn

[Scikit-learn](https://scikit-learn.org/) es una biblioteca de Python para Machine Learning. Incluye algoritmos, herramientas de preprocesamiento, división de datos, selección de modelos y métricas de evaluación mediante una interfaz consistente.

Entre sus ventajas se encuentran su documentación, facilidad de uso, integración con Pandas y variedad de algoritmos. Como limitaciones, no está orientada principalmente a redes neuronales profundas o procesamiento distribuido de datos muy grandes, y aun con una API sencilla es necesario comprender los datos y evaluar correctamente el modelo.

## Dataset

Se utiliza el conjunto **Titanic - Machine Learning from Disaster** de [Kaggle](https://www.kaggle.com/competitions/titanic/data). Cada fila representa a un pasajero y contiene información como clase, sexo, edad, familiares a bordo, tarifa y puerto de embarque. El objetivo es predecir la variable `Survived`.

El CSV no se inventa ni se sustituye por datos sintéticos. Las instrucciones para obtener el archivo oficial están en [`data/README.md`](./data/README.md).

## Variables utilizadas

| Variable | Descripción |
| --- | --- |
| `Pclass` | Clase del boleto: primera, segunda o tercera clase. |
| `Sex` | Sexo registrado del pasajero. |
| `Age` | Edad en años; contiene algunos valores faltantes. |
| `SibSp` | Número de hermanos, hermanas o cónyuges a bordo. |
| `Parch` | Número de padres, madres o hijos a bordo. |
| `Fare` | Tarifa pagada por el boleto. |
| `Embarked` | Puerto de embarque: C, Q o S. |
| `Survived` | Variable objetivo que indica si el pasajero sobrevivió. |

La codificación de la variable objetivo es:

```text
Survived = 0 → No sobrevivió
Survived = 1 → Sobrevivió
```

## Modelo utilizado

El modelo principal es `RandomForestClassifier`. Un bosque aleatorio combina las decisiones de varios árboles entrenados con variaciones de los datos. La clase final se obtiene mediante el voto del conjunto. Es apropiado para este problema porque realiza clasificación, puede representar relaciones no lineales y trabaja bien con variables numéricas y categóricas después del preprocesamiento.

## Proceso realizado

1. Carga del `train.csv` oficial.
2. Exploración de dimensiones, tipos, valores faltantes y distribución de supervivencia.
3. Selección de siete características y de la variable objetivo.
4. Imputación de valores numéricos faltantes mediante la mediana.
5. Imputación de categorías y conversión con *one-hot encoding*.
6. División estratificada: 80 % para entrenamiento y 20 % para prueba.
7. Entrenamiento reproducible de 200 árboles.
8. Generación y comparación de predicciones.
9. Evaluación con accuracy, matriz de confusión y reporte de clasificación.
10. Prueba del pipeline con dos pasajeros ficticios.

El preprocesamiento y el clasificador forman un solo `Pipeline`, lo que aplica exactamente las mismas transformaciones durante entrenamiento y predicción.

## Tres ejemplos de Machine Learning con Scikit-learn

1. **Regresión lineal (`LinearRegression`):** estima un valor continuo, por ejemplo el precio de una vivienda.
2. **Árbol de decisión (`DecisionTreeClassifier`):** clasifica observaciones mediante reglas aprendidas de las características.
3. **Bosque aleatorio (`RandomForestClassifier`):** combina varios árboles para obtener una clasificación más estable; es el algoritmo usado en esta práctica.

## Resultados

El notebook se ejecutó completamente con los 891 registros del `train.csv` oficial de Kaggle. La división estratificada dejó 712 pasajeros para entrenamiento y 179 para prueba.

El modelo obtuvo un **accuracy de 0.8212, equivalente a 82.12 %**. La matriz de confusión fue:

| Valor real / Predicción | No sobrevivió | Sobrevivió |
| --- | ---: | ---: |
| No sobrevivió | 99 | 11 |
| Sobrevivió | 21 | 48 |

Esto representa 147 predicciones correctas y 32 incorrectas. Para la clase `Sobrevivió`, el modelo obtuvo precision de 0.8136, recall de 0.6957 y f1-score de 0.7500. Estas métricas corresponden exactamente a la ejecución guardada en el notebook con `random_state=42`.

En la prueba manual, el primer pasajero ficticio fue clasificado como **No sobrevivió** y el segundo como **Sobrevivió**. Son estimaciones estadísticas del modelo, no certezas históricas.

El notebook también conserva dos figuras listas para usarse como evidencia: una comparación de supervivencia general, por sexo y por clase, y una visualización etiquetada de la matriz de confusión.

## Ejecución

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r Practica10/requirements.txt
jupyter notebook Practica10/notebooks/machine_learning_titanic.ipynb
```

El archivo `train.csv` debe permanecer en `Practica10/data/`. Para repetir el análisis, ejecutar todas las celdas en orden mediante **Kernel → Restart & Run All**.

También se puede validar sin interfaz:

```bash
jupyter nbconvert --to notebook --execute \
  Practica10/notebooks/machine_learning_titanic.ipynb \
  --output machine_learning_titanic.ipynb \
  --output-dir Practica10/notebooks \
  --ExecutePreprocessor.timeout=120
```

## Conclusión

La práctica integra los pasos principales de un proyecto de aprendizaje supervisado. Además de entrenar un Random Forest, permite comprender por qué la exploración, el tratamiento de valores faltantes y una separación correcta entre entrenamiento y prueba son necesarios para evaluar el modelo de manera honesta. El uso de un pipeline hace que el proceso sea ordenado, reproducible y fácil de aplicar a pasajeros nuevos. Las predicciones representan estimaciones estadísticas y no certezas históricas.

El notebook quedó ejecutado con sus 21 celdas de código completas y sin excepciones.

## Tecnologías utilizadas

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Jupyter Notebook
- Kaggle
- Git

**Autor:** Al Farias Leyva  
**Matrícula:** 230389  
**Grupo:** 9A IDGS
