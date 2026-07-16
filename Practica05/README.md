# Práctica 05: Dataset Clínico Simulado de Pacientes de Puebla

## Objetivo general

Generar y analizar un dataset reproducible de 5,000 pacientes ficticios del estado de Puebla, con indicadores generales, clínicos, geográficos y factores que permiten calcular un nivel académico de riesgo cardiovascular.

## Descripción y contexto

Esta práctica usa exclusivamente datos sintéticos para aprender generación, validación, limpieza, análisis exploratorio y visualización con Python. No utiliza datos de pacientes reales ni contiene nombres, CURP, teléfonos, correos o domicilios. El indicador de riesgo es didáctico: no representa un diagnóstico médico ni debe emplearse para tomar decisiones clínicas.

## Estructura

```text
Practica05/
├── data/
│   └── pacientes_puebla_5000.csv
├── docs/
│   └── diccionario_datos.md
├── notebooks/
│   └── analisis_pacientes_puebla.ipynb
├── outputs/
│   └── (gráficas generadas por el notebook)
├── src/
│   └── generar_dataset.py
├── README.md
└── requirements.txt
```

## Columnas

| Grupo          | Columnas                                                                                                  |
| -------------- | --------------------------------------------------------------------------------------------------------- |
| Identificación | `id_paciente`                                                                                             |
| Generales      | `edad`, `sexo`, `peso_kg`, `estatura_m`, `imc`                                                            |
| Geográficas    | `municipio`, `localidad`, `latitud`, `longitud`                                                           |
| Clínicas       | `presion_sistolica`, `presion_diastolica`, `glucosa_mg_dl`, `colesterol_mg_dl`, `frecuencia_cardiaca_lpm` |
| Factores       | `tabaquismo`, `actividad_fisica`, `diabetes`, `hipertension`, `antecedentes_familiares`                   |
| Resultado      | `puntaje_riesgo`, `riesgo_cardiovascular`                                                                 |

Los tipos, rangos y reglas exactas se encuentran en el [diccionario de datos](./docs/diccionario_datos.md).

## Ejecución

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r Practica05/requirements.txt
python3 Practica05/src/generar_dataset.py
jupyter notebook Practica05/notebooks/analisis_pacientes_puebla.ipynb
```

> El generador utiliza la semilla `230389`, por lo que el dataset puede reproducirse con los mismos resultados.

También puede ejecutarse y validarse el notebook completo sin interfaz:

```bash
jupyter nbconvert --to notebook --execute Practica05/notebooks/analisis_pacientes_puebla.ipynb \
  --output analisis_pacientes_puebla_ejecutado.ipynb --output-dir /tmp
```

## Resultados generados

El análisis produce las siguientes visualizaciones en la carpeta `outputs/`:

- [Distribución de pacientes por municipio](./outputs/barras_municipios.png)
- [Distribución del riesgo cardiovascular](./outputs/barras_riesgo_cardiovascular.png)
- [Relación entre edad y presión sistólica](./outputs/dispersion_edad_presion.png)
- [Histogramas de edad e IMC](./outputs/histogramas_edad_imc.png)

**Autor:** Al Farias Leyva

**Matrícula:** 230389
