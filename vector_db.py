# vector_db.py
from sentence_transformers import SentenceTransformer
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection
import scrape as youtube_comments

def store_comments_in_vector_db(comments):
    # Initialize the sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Generate embeddings for the comments
    embeddings = model.encode(comments)

    # Connect to Milvus server
    connections.connect(alias="default", host="localhost", port="19530")

    # Define the schema for the collection
    fields = [
        FieldSchema(name="comment", dtype=DataType.TEXT, is_primary=True),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=len(embeddings[0]))
    ]
    schema = CollectionSchema(fields, description="YouTube Comments Collection")

    # Create a collection
    collection = Collection(name="youtube_comments", schema=schema)

    # Insert the comments and their embeddings into the collection
    data = [
        comments,    # comment field
        embeddings.tolist()  # embedding field
    ]
    collection.insert(data)

    print("Comments and their embeddings have been stored in Milvus.")

if __name__ == "__main__":
    video_id = input("Enter the YouTube video ID: ")
    comments = youtube_comments.get_youtube_comments(video_id)
    store_comments_in_vector_db(comments)
