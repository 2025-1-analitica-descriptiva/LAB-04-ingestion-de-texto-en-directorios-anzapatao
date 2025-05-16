# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import zipfile
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    # Descomentar la siguiente linea para ejecutar el test
    # raise NotImplementedError("Falta implementar la funcion pregunta_01")

    # Descomprimir el archivo zip en la raíz del repositorio
    with zipfile.ZipFile('files/input.zip', 'r') as zip_ref:
        zip_ref.extractall('.')

    # Crear la carpeta de salida si no existe
    os.makedirs('files/output', exist_ok=True)

    # Inicializar listas para almacenar los datos
    train_data = []
    test_data = []

    # Función para procesar los archivos y agregar a las listas
    def process_files(directory, data_list):
        for sentiment in ['positive', 'negative', 'neutral']:
            path = os.path.join(directory, sentiment)
            for filename in os.listdir(path):
                if filename.endswith('.txt'):
                    with open(os.path.join(path, filename), 'r', encoding='utf-8') as file:
                        phrase = file.read().strip()
                        data_list.append({'phrase': phrase, 'target': sentiment})

    # Procesar los archivos de entrenamiento y prueba
    process_files('input/train', train_data)
    process_files('input/test', test_data)

    # Crear DataFrames y guardarlos como CSV
    train_df = pd.DataFrame(train_data)
    test_df = pd.DataFrame(test_data)

    train_df.to_csv('files/output/train_dataset.csv', index=False)
    test_df.to_csv('files/output/test_dataset.csv', index=False)
    
if __name__ == "__main__":
    pregunta_01()