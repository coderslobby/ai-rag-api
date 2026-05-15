from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    COHERE_API_KEY : str
    GROQ_API_KEY : str
    language_model : str
    cohere_embedding_model : str
    chunk_size: int
    chunk_overlap: int
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

settings = Setting()