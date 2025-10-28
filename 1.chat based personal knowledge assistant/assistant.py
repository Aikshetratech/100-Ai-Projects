from flask import Flask, request, jsonify, render_template_string
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# Paths
DATA_PATH = "data/knowledge_base.txt"

# Load knowledge base
if not os.path.exists(DATA_PATH):
    os.makedirs("data", exist_ok=True)
    open(DATA_PATH, "w").write("Add your knowledge here!")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    knowledge_data = [line.strip() for line in f if line.strip()]

# Embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
kb_embeddings = model.encode(knowledge_data)
index = faiss.IndexFlatL2(kb_embeddings.shape[1])
index.add(np.array(kb_embeddings))

# Flask app
app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Offline Knowledge Assistant</title>
    <style>
        body { font-family: Arial; margin: 40px; background-color: #f8f9fa; }
        .chatbox { max-width: 600px; margin: auto; padding: 20px; background: white; border-radius: 10px; }
        .user, .bot { margin: 10px 0; }
        .user { text-align: right; color: blue; }
        .bot { text-align: left; color: green; }
    </style>
</head>
<body>
    <div class="chatbox">
        <h2>Offline Personal Knowledge Assistant</h2>
        <div id="chat"></div>
        <input type="text" id="userInput" placeholder="Ask something..." style="width:80%">
        <button onclick="sendMessage()">Send</button>
    </div>

    <script>
        async function sendMessage() {
            let input = document.getElementById("userInput").value;
            let chat = document.getElementById("chat");
            chat.innerHTML += `<div class='user'><b>You:</b> ${input}</div>`;
            document.getElementById("userInput").value = '';

            let response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ query: input })
            });
            let data = await response.json();
            chat.innerHTML += `<div class='bot'><b>Assistant:</b> ${data.answer}</div>`;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    query = data.get("query", "")
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k=3)
    answers = [knowledge_data[i] for i in indices[0]]
    response = " | ".join(answers)
    return jsonify({"answer": response})

if __name__ == "__main__":
    print("🚀 Offline Personal Knowledge Assistant running at http://127.0.0.1:5000/")
    app.run(debug=True)
