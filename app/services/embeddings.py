import cohere
from langchain_cohere import CohereEmbeddings
from app.config import settings

cohere_client = cohere.client_v2(api_key=settings.COHERE_API_KEY) #type:ignore

def get_embeddings():
    cohere_embeddings = CohereEmbeddings(
        model=settings.cohere_embedding_model,
        client=cohere_client
    ) #type:ignore
    return cohere_embeddings