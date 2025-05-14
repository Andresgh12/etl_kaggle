import os
import pandas as pd
from pymongo import MongoClient

# Obtiene la URL de MongoDB Atlas desde variable de entorno
MONGO_URI = os.getenv('MONGO_URI')
if not MONGO_URI:
    raise RuntimeError("La variable de entorno MONGO_URI no está definida.")

# Nombre de la base de datos
DB_NAME = 'miBase'


def process_csv(path: str) -> list:
    """
    Lee un CSV con pandas, aplica transformaciones y devuelve lista de dicts.
    """
    df = pd.read_csv(path)
    # Ejemplo de transformación: añade un campo processed
    df['processed'] = True
    return df.to_dict(orient='records')


def load_to_mongo(records: list, collection_name: str):
    """
    Inserta documentos en MongoDB Atlas.
    """
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    coll = db[collection_name]
    if records:
        coll.insert_many(records)


def main():
    base_folder = 'kaggle_dataset'

    for fname in sorted(os.listdir(base_folder)):
        if not fname.endswith('.csv'):
            continue
        path = os.path.join(base_folder, fname)
        collection = os.path.splitext(fname)[0]
        print(f"Procesando {fname} → colección '{collection}'...")
        docs = process_csv(path)
        load_to_mongo(docs, collection)
        print(f"  ✅ Cargados {len(docs)} registros en {collection}\n")


if __name__ == '__main__':
    main()