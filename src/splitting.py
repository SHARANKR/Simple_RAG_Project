from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.data_load import transcript

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])

