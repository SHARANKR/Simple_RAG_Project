embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = FAISS.from_documents(chunks, embeddings)

vector_store.index_to_docstore_id

vector_store.get_by_ids(['2436bdb8-3f5f-49c6-8915-0c654c888700'])