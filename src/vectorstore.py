import json
import os
from pathlib import Path

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document


DATA_DIR = Path(__file__).parent.parent / "data"
CHROMA_DIR = Path(__file__).parent.parent / "chroma_db"


def load_documents() -> list[Document]:
    documents = []
    for json_file in DATA_DIR.glob("*.json"):
        with open(json_file, "r", encoding="utf-8") as f:
            items = json.load(f)
        for item in items:
            content = f"Pregunta: {item['pregunta']}\n\nRespuesta: {item['respuesta']}"
            metadata = {
                "id": item["id"],
                "categoria": item["categoria"],
                "source": json_file.name,
            }
            documents.append(Document(page_content=content, metadata=metadata))
    return documents


def create_vectorstore() -> Chroma:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    documents = load_documents()
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
    )
    return vectorstore


def get_vectorstore() -> Chroma:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    if CHROMA_DIR.exists():
        return Chroma(
            persist_directory=str(CHROMA_DIR),
            embedding_function=embeddings,
        )
    return create_vectorstore()
