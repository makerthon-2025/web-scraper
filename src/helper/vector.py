from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("model")

def encode_text(text):
    return model.encode(text)   

if __name__ == "__main__":
    arr_string = np.array2string(encode_text("lễ diễu binh ngày 30/4"), separator=', ', formatter={'all': lambda x: format(x, '.10f')})
    print(arr_string)