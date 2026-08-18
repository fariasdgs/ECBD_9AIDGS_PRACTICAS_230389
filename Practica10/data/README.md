# Dataset Titanic

Esta carpeta debe contener el archivo oficial `train.csv` de la competencia **Titanic - Machine Learning from Disaster** de Kaggle.

## Descarga manual

1. Abrir <https://www.kaggle.com/competitions/titanic/data>.
2. Iniciar sesión en Kaggle y aceptar las reglas de la competencia si se solicita.
3. Elegir **Download All** y descomprimir el archivo descargado.
4. Copiar `train.csv` en esta carpeta, de modo que la ruta final sea:

```text
Practica10/data/train.csv
```

Los archivos `test.csv` y `gender_submission.csv` no son necesarios para la evaluación interna de esta práctica.

## Descarga con la API de Kaggle (opcional)

Con la API instalada y configurada fuera del repositorio:

```bash
kaggle competitions download -c titanic -p /tmp/titanic
unzip /tmp/titanic/titanic.zip -d Practica10/data
```

No se debe guardar `kaggle.json` dentro del repositorio ni publicar credenciales. El notebook comprueba la existencia y las columnas requeridas antes de entrenar.

