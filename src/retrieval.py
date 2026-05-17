"""
Retrieval engine with two strategies:
A) Raw Vector Search
B) AI-Enhanced Retrieval with query expansion
"""
from typing import List, Tuple, Dict
import numpy as np
from .embedding import EmbeddingGenerator, MockGenerativeModel
from .vector_store import VectorStore
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class RetrievalEngine:
    """
    Orchestrates retrieval operations with different strategies
    """
    def __init__(self, vector_store: VectorStore, embedding_generator: EmbeddingGenerator):
        self.vector_store = vector_store
        self.embedding_generator = embedding_generator
        self.mock_generative_model = MockGenerativeModel()
    def strategy_a_raw_search(self, query: str, k: int = 3) -> List[Tuple[str, float, Dict]]:
        """
        Strategy A: Traditional embedding-based similarity search
        Args:
            query: User query
            k: Number of results
        Returns:
            List of (text, score, metadata) tuples
        """
        logger.info(f"Strategy A - Raw search for: {query}")
        query_embedding = self.embedding_generator.generate_embedding(query)
        results = self.vector_store.search(query_embedding, k)
        return results
    def strategy_b_ai_enhanced(self, query: str, k: int = 3) -> List[Tuple[str, float, Dict]]:
        """
        Strategy B: AI-enhanced retrieval with query expansion
        Args:
            query: User query
            k: Number of results
        Returns:
            List of (text, score, metadata) tuples
        """
        logger.info(f"Strategy B - AI-enhanced for: {query}")
        expanded_query = self.mock_generative_model.generate_content(query)
        logger.info(f"Expanded query: {expanded_query[:100]}...")
        query_embedding = self.embedding_generator.generate_embedding(expanded_query)
        results = self.vector_store.search(query_embedding, k)
        return results
    def compare_strategies(self, query: str, k: int = 3) -> Dict:
        """
        Compare both strategies for a given query
        Returns:
            Dictionary with results from both strategies
        """
        results_a = self.strategy_a_raw_search(query, k)
        results_b = self.strategy_b_ai_enhanced(query, k)
        return {
            'query': query,
            'strategy_a': [
                {
                    'text': text,
                    'score': score,
                    'metadata': metadata
                }
                for text, score, metadata in results_a
            ],
            'strategy_b': [
                {
                    'text': text,
                    'score': score,
                    'metadata': metadata
                }
                for text, score, metadata in results_b
            ]
        }
