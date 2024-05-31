import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def load_comments(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        comments = f.readlines()
    return [comment.strip() for comment in comments]

def embed_comments(comments, model):
    embeddings = model.encode(comments, convert_to_tensor=True)
    return embeddings

def create_vector_db(embeddings):
    d = embeddings.shape[1] 
    index = faiss.IndexFlatL2(d) 
    index.add(embeddings)
    return index

if __name__ == "__main__":
    
    comments = load_comments('comments.txt')
    
    
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    embeddings = embed_comments(comments, model)
    
    index = create_vector_db(np.array(embeddings))
    
    faiss.write_index(index, 'comments_index.faiss')
    
    print("Vector database created and stored as 'comments_index.faiss'")
