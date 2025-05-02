from pymilvus import MilvusClient
import numpy as np
from src.helper.vector import encode_text
import os
import asyncio

client = MilvusClient(
    uri=f"http://{os.getenv("MILVUS_HOST")}:{os.getenv("MILVUS_PORT")}",
    db_name=os.getenv("MILVUS_DB_NAME"),
)

if client.has_collection(collection_name=os.getenv("MILVUS_COLLECTION_NAME_FOR_NEWS")): 
    print("Collection already exists")
else:
    try:
        client.create_collection(
            collection_name=os.getenv("MILVUS_COLLECTION_NAME_FOR_NEWS"), 
            dimension=768,

            primary_field_name="id",
            vector_field_name="vector",

            enable_dynamic_field=True,
        )
    except Exception as e:
        print(f"Error creating collection: {e}")

def insert_data(data: dict):
    client.insert(
        collection_name=os.getenv("MILVUS_COLLECTION_NAME_FOR_NEWS"),
        data=data,
    )

