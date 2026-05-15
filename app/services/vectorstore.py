from typing import List
from langchain_community.vectorstores import Chroma
from app.services.embeddings import get_embeddings
def store_vectors(chunks: List[str], collection_name:str) -> str:
    vectorstore = Chroma.from_texts(texts=chunks, # type: ignore
                      embedding=get_embeddings(),
                      collection_name=collection_name)
    return ''