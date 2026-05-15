import pymupdf
from typing import List

def read_document(file_path: str)-> str :
    with pymupdf.open(filename=file_path) as f:
        fullDocText: List[str] = []
        for page in f:
            fullDocText.append(str(page.get_text())) # type:ignore
        return ''.join(fullDocText)