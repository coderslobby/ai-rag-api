from pydantic import BaseModel
from typing import List

class DocumentUploadResponse(BaseModel):
    filename : str
    message: str

class QuestionRequest(BaseModel):
    question: str
    collection_name: str

class AnswerResponse(BaseModel):
    answer: str
    answer_source: List[str]