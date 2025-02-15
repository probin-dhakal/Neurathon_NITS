from src.helper import load_pdf, text_split, download_hugging_face_embeddings
# from langchain.vectorstores import Pinecone

import pinecone
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
import os
from pinecone import Pinecone
from pinecone import ServerlessSpec

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')


# print(PINECONE_API_KEY)
# print(PINECONE_API_ENV)

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


#Initializing the Pinecone

Pinecone(api_key=PINECONE_API_KEY)


index_name = "debate-ai"
#Creating Embeddings for Each of The Text Chunks & storing
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

