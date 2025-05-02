from src.service import milvus

def insert_data_controller():
    try:
        milvus.insert_data_service()
    except Exception as e:
        return {"error": str(e)}