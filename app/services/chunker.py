from langchain_community.document_loaders import PyPDFLoader
from typing import List
from langchain_core.documents import Document

def load_documents(file_path: str) -> List[Document]: 
    loader = PyPDFLoader(file_path=file_path, mode='single')
    docs = loader.load()
    return docs