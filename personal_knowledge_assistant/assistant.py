import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load sentence-transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load knowledge base
with open("data/knowledge_base.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f if line.strip()]

# Generate embeddings for knowledge base
print("Generating embeddings for knowledge base...")
embeddings = model.encode(documents, convert_to_numpy=True)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)
print(f"FAISS index created with {index.ntotal} entries.\n")

# Function to get top relevant results
def ask_question(query, top_k=3):
    q_emb = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(q_emb, top_k)
    # Collect top-k results
    top_docs = [documents[i] for i in indices[0]]
    # Summarize into a single answer
    answer = " ".join(top_docs)
    return answer

# Main loop
if __name__ == "__main__":
    print("Offline Personal Knowledge Assistant ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = ask_question(user_input, top_k=2)  # adjust top_k as needed
        print(f"Assistant: {answer}\n")
