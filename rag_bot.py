import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Load PDF
docs = PyPDFLoader('textbook.pdf').load()
print(f"Loaded {len(docs)} pages")

# Chunk
chunks = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=64).split_documents(docs)
print(f"Created {len(chunks)} chunks")

# FREE embeddings (runs locally, no API key needed)
print("Loading embedding model... please wait")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Embed + Store
print("Embedding... please wait")
db = Chroma.from_documents(chunks, embeddings)
retriever = db.as_retriever(search_kwargs={'k': 5})

# FREE LLM via Groq
llm = ChatGroq(model='llama-3.3-70b-versatile')

# Prompt
prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the context below.
If you don't know, say "I don't know".

Context: {context}

Question: {input}
""")

# Chain
chain = create_retrieval_chain(
    retriever,
    create_stuff_documents_chain(llm, prompt)
)

print("\nBot ready! Type your question (Ctrl+C to quit)\n")
while True:
    try:
        question = input('Q: ')
        result = chain.invoke({"input": question})
        print(f"\nA: {result['answer']}\n")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break