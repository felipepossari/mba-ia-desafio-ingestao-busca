import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import embeddings

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")


def check_variables():
    for k in ("OPENAI_API_KEY", "OPENAI_EMBEDDING_MODEL", "DATABASE_URL", "PG_VECTOR_COLLECTION_NAME"):
        if not os.getenv(k):
            raise RuntimeError(f"Missing {k} environment variable")


def load_pdf() -> list[Document]:
    current_dir = Path(__file__).parent.parent
    pdf_path = current_dir / PDF_PATH
    return PyPDFLoader(str(pdf_path)).load()


def store_documents(documents: list[Document]):
    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL"))
    ids = [f"doc-{i}" for i in range(len(documents))]
    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True
    )
    store.add_documents(documents=documents, ids=ids)


def enrich_documents(docs: list[Document]) -> list[Document]:
    splitted_text = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        add_start_index=False
    ).split_documents(docs)

    if not splitted_text:
        raise RuntimeError("No documents found")

    enriched_docs: list[Document] = []
    for doc in splitted_text:
        meta = {k: v for k, v in doc.metadata.items() if v not in ("", None)}
        enriched_doc = Document(
            page_content=doc.page_content,
            metadata=meta,
        )
        enriched_docs.append(enriched_doc)
    return enriched_docs


def ingest_pdf():
    check_variables()
    docs = load_pdf()
    enriched_docs = enrich_documents(docs)
    store_documents(enriched_docs)


if __name__ == "__main__":
    ingest_pdf()
