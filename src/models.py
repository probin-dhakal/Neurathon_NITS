from src.helper import download_hugging_face_embeddings

# from pinecone import PineconeClient

# from pinecone import ServerlessSpec
# from pinecone import Pinecone
# from langchain_pinecone import PineconeVectorStore
# from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# from src.prompt import *

# from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os


load_dotenv()

def get_llm():
    
    # PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

    # embeddings = download_hugging_face_embeddings()

    # #Initializing the Pinecone
    # Pinecone(api_key=PINECONE_API_KEY)


    # index_name = "debate-ai"

    # #Loading the index
    # docsearch=PineconeVectorStore.from_existing_index(index_name, embeddings)


    # PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    # chain_type_kwargs={"prompt": PROMPT}

    llm=CTransformers(model="Neurathon_NITS\models\llama_model_1.bin",
                    model_type="llama",
                    config={'max_new_tokens':512,
                            'temperature':0.8})


    # qa=RetrievalQA.from_chain_type(
    #     llm=llm, 
    #     chain_type="stuff", 
    #     retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    #     return_source_documents=True, 
    #     chain_type_kwargs=chain_type_kwargs)

    return llm

if __name__ == "__main__":
    print(os.getcwd())
    # print(get_llm())
    
    