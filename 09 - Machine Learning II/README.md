Este repositorio contiene dos trabajos de MLOps en [Google Cloud Platform](https://console.cloud.google.com/) (GCP).

## Predicciones en tiempo real (VM+Bucket)

En la carpeta [1_gcp_real_time_prediction](./1_gcp_real_time_prediction) se encuentran los archivos necesarios para ralizar las predicciones de un modelo en tiempo real, en Cloud. Para esto, se debe instanciar una Maquina Virtual y un Bucket en GCP. En el directorio raiz del Bucket, se depositan los nuevos datos a predecir de manera asincrónica y en la carpeta `output` se obtienen las predicciones. La VM ejecuta un script de Python que hace polling sobre el Bucket y al encontrar nuevos archivos de datos (de extensión csv), registra los nombres en el archivo de texto `new_data_filenames.txt`. Luego dichos datos son cargados y procesados tambien en la VM, quien escribe los resultados en al carpeta output.

<p align="center" float="left" justify-content="center">
    <img src="./outputs/gcp_output.gif" alt="real_time_prediction" class="center" width="820"/>
</p>

Los archivos son los siguientes:
- [airline-passenger-satisfaction.ipynb](./1_gcp_real_time_prediction/airline-passenger-satisfaction.ipynb): es el notebook con el análisis de datos y donde los modelos fueron entrenados.
- [real_time_prediction_cloud.py](./1_gcp_real_time_prediction/real_time_prediction_cloud.py): es un script que se ejecuta en la vm, polea los datos del Bucket, realiza las predicciones y escribe el resultado en el Bucket.
- [real_time_prediction.py](./1_gcp_real_time_prediction/real_time_prediction.py): tiene la misma funcion que `real_time_prediction_cloud.py` pero de manera local (en SO Ubuntu).
- [preprocess.pickle](./1_gcp_real_time_prediction/preprocess.pickle): archivo binario con los transformeners necesarios de sklearn para el preprocesado de datos.

Nota: el modelo ariline_passanger_satisfaction_model_rf.pickle no fue subido al repositorio porque excede el tamaño permitido.
