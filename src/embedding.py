"""
Embedding generation module using sentence-transformers
Mocking Vertex AI's textembedding-gecko behavior
"""
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Union
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class MockVertexAIEmbedding:
    """
    Mock class to simulate Vertex AI's TextEmbeddingModel
    """
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.embedding_dimension = self.model.get_sentence_embedding_dimension()
    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts"""
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings.tolist()
    def get_embedding(self, text: str) -> List[float]:
        """Generate embedding for a single text"""
        embedding = self.model.encode([text], convert_to_numpy=True)
        return embedding[0].tolist()
class MockGenerativeModel:
    """
    Mock class to simulate Vertex AI's GenerativeModel for query expansion
    """
    def __init__(self, model_name: str = "gemini-pro"):
        self.model_name = model_name
    def generate_content(self, query: str) -> str:
        """
        Mock query expansion by generating alternative query formulations
        In production, this would call actual LLM
        """
        expansions = {
            "How does the system handle peak load?":
                "What are the performance characteristics and scaling mechanisms when the system experiences maximum concurrent user load or sudden traffic spikes? How does it manage resource allocation, auto-scaling, and load balancing during peak demand?",
            "What security measures are implemented?":
                "Describe the authentication mechanisms, encryption protocols, access control systems, and security best practices implemented to protect data and prevent unauthorized access.",
            "How does data persistence work?":
                "Explain the storage mechanisms, backup strategies, durability guarantees, and data recovery processes for maintaining data persistence across system restarts and failures.",
        }
        if query in expansions:
            return expansions[query]
        else:
            return f"Please provide detailed information about: {query}. Include technical specifications, implementation details, and operational considerations."
class EmbeddingGenerator:
    """
    Main embedding generator class that orchestrates embedding generation
    using both mock Vertex AI and direct sentence-transformers
    """
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.mock_vertex_ai = MockVertexAIEmbedding(model_name)
        self.model = SentenceTransformer(model_name)
        self.dimension = self.mock_vertex_ai.embedding_dimension
    def generate_embeddings(self, texts: List[str]) -> np.ndarray:
        """Generate embeddings for multiple texts"""
        logger.info(f"Generating embeddings for {len(texts)} texts")
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings
    def generate_embedding(self, text: str) -> np.ndarray:
        """Generate embedding for a single text"""
        embedding = self.model.encode([text], convert_to_numpy=True)
        return embedding[0]
    def mock_vertex_generate(self, texts: List[str]) -> List[List[float]]:
        """Simulate Vertex AI embedding generation"""
        return self.mock_vertex_ai.get_embeddings(texts)
