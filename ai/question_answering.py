from transformers import pipeline
import json
from utils.logger import logger

# Initialize the model
qa_model = pipeline("sentence-similarity", model="sentence-transformers/all-MiniLM-L6-v2")

def load_qna_data(file_path):
    """Load Q&A data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

async def get_answer(question: str):
    """Get the best answer for a given question."""
    logger.debug(f"Processing question: {question}")
    data = load_qna_data("qna.json")
    
    # Check for exact match in pre-defined Q&A
    if question in data["questions"]:
        return data["questions"][question]
    
    # Use semantic search for similarity matching
    responses = [(qa["answer"], qa_model(question, qa["question"])) for qa in data.get("knowledge", [])]
    best_match = max(responses, key=lambda x: x[1]["score"], default=None)
    
    if best_match and best_match[1]["score"] > 0.75:  # Threshold for similarity
        return best_match[0]
    
    return "I'm sorry, I don't have an answer to that question right now."
