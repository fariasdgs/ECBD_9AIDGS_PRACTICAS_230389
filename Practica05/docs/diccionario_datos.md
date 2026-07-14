# Diccionario de datos y metodología

## Alcance

El archivo `pacientes_puebla_5000.csv` contiene 5,000 registros **completamente ficticios** creados con fines académicos. No parte de expedientes clínicos ni incluye nombres, CURP, teléfonos, correos o domicilios. La semilla `230389` permite reproducir exactamente el resultado.

El dataset sirve para practicar validación, limpieza, análisis exploratorio y visualización. El nivel calculado es un indicador didáctico y **no es un diagnóstico ni sustituye una evaluación médica**.

## Atributos, tipos y rangos

| Columna | Tipo | Valores o rango permitido | Descripción |
|---|---|---|---|
| `id_paciente` | texto | `PAC0001` a `PAC5000` | Identificador ficticio único. |
| `edad` | entero | 18–90 años | Edad simulada. |
| `sexo` | categórico | Mujer, Hombre | Sexo simulado. |
| `municipio` | categórico | Catálogo geográfico del script | Municipio de Puebla. |
| `localidad` | categórico | Catálogo geográfico del script | Localidad válida asociada al municipio. |
| `latitud` | decimal | centro de localidad ±0.018° | Coordenada simulada próxima a la localidad. |
| `longitud` | decimal | centro de localidad ±0.018° | Coordenada simulada próxima a la localidad. |
| `peso_kg` | decimal | derivado de estatura e IMC; aprox. 35.7–159.7 kg | Peso corporal. |
| `estatura_m` | decimal | 1.45–1.95 m | Estatura. |
| `imc` | decimal | 17–42 kg/m² (con redondeo) | Índice de masa corporal. |
| `presion_sistolica` | entero | 90–190 mmHg | Presión sistólica. |
| `presion_diastolica` | entero | 55–120 mmHg y al menos 20 menor que la sistólica | Presión diastólica. |
| `glucosa_mg_dl` | entero | 65–240 mg/dL | Glucosa simulada. |
| `colesterol_mg_dl` | entero | 110–330 mg/dL | Colesterol total simulado. |
| `frecuencia_cardiaca_lpm` | entero | 50–120 lpm | Frecuencia cardíaca. |
| `tabaquismo` | categórico | Nunca, Exfumador, Actual | Condición respecto al tabaco. |
| `actividad_fisica` | categórico | Baja, Moderada, Alta | Nivel de actividad. |
| `diabetes` | categórico binario | Sí, No | Indicador clínico simulado. |
| `hipertension` | categórico binario | Sí, No | Indicador clínico simulado. |
| `antecedentes_familiares` | categórico binario | Sí, No | Antecedentes cardiovasculares familiares simulados. |
| `puntaje_riesgo` | entero | 0–19 | Suma de las reglas indicadas abajo. |
| `riesgo_cardiovascular` | categórico objetivo | bajo, medio, alto | Clase obtenida a partir del puntaje. |

Los límites exactos se validan en el notebook; los extremos observados de peso pueden variar dentro del rango derivado por el redondeo.

## Reglas de generación

- Se usa `random.Random(230389)` y se generan exactamente 5,000 identificadores consecutivos.
- La edad sigue una distribución triangular entre 18 y 90 años, con mayor densidad alrededor de 43.
- El sexo se genera con proporciones aproximadas de 51 % Mujer y 49 % Hombre.
- Los pares municipio–localidad se toman de un catálogo cerrado. Las coordenadas parten del centro aproximado y reciben una variación máxima de 0.018 grados.
- Estatura, actividad y edad influyen en el IMC y el peso. El peso se calcula como `IMC × estatura²`.
- La probabilidad de diabetes e hipertensión aumenta con edad e IMC mediante una función logística.
- Los diagnósticos simulados modifican glucosa y presión; actividad y tabaquismo modifican la frecuencia cardíaca. Las variables se limitan a los rangos documentados.

Estas relaciones aportan coherencia académica sin pretender reproducir con exactitud una población real.

## Cálculo de `riesgo_cardiovascular`

El riesgo no se asigna al azar. Se suma un punto por cada condición, excepto donde se indican dos:

| Factor | Puntos |
|---|---:|
| Edad ≥55 / ≥70 | +1 / +1 adicional |
| IMC ≥25 / ≥30 | +1 / +1 adicional |
| Sistólica ≥130 o diastólica ≥80 | +1 |
| Sistólica ≥140 o diastólica ≥90 | +1 adicional |
| Glucosa ≥100 / ≥126 | +1 / +1 adicional |
| Colesterol ≥200 / ≥240 | +1 / +1 adicional |
| Exfumador / fumador actual | +1 / +2 |
| Actividad física baja | +1 |
| Diabetes | +2 |
| Hipertensión | +2 |
| Antecedentes familiares | +2 |

Clasificación final:

- `bajo`: 0 a 4 puntos;
- `medio`: 5 a 9 puntos;
- `alto`: 10 puntos o más.

La columna `puntaje_riesgo` permite auditar la clasificación.

## Catálogo geográfico

El generador incluye pares válidos como Puebla–Heroica Puebla de Zaragoza, Tehuacán–Tehuacán, Atlixco–Atlixco, San Pedro Cholula–Cholula de Rivadavia, Huauchinango–Huauchinango y otros diez pares del estado. El catálogo completo, sus coordenadas centrales y ponderaciones están visibles en `src/generar_dataset.py`.
