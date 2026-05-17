import pytest
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.embedding import EmbeddingGenerator
from src.vector_store import VectorStore
from src.retrieval import RetrievalEngine
class TestRetrievalEngine:
    @pytest.fixture
    def setup_engine(self):
        embedding_gen = EmbeddingGenerator()
        vector_store = VectorStore(dimension=embedding_gen.dimension, metric="cosine")
        test_docs = [
            "The system handles peak load through auto-scaling based on CPU metrics",
            "Security is implemented with JWT authentication and TLS encryption",
            "Data persistence uses PostgreSQL with WAL and daily backups"
        ]
        embeddings = embedding_gen.generate_embeddings(test_docs)
        vector_store.add_vectors(embeddings, test_docs)
        engine = RetrievalEngine(vector_store, embedding_gen)
        return engine, test_docs
    def test_strategy_a_raw_search(self, setup_engine):
        engine, docs = setup_engine
        results = engine.strategy_a_raw_search("How does scaling work?", k=2)
        assert len(results) == 2
        assert isinstance(results[0][1], float)
    def test_strategy_b_ai_enhanced(self, setup_engine):
        engine, docs = setup_engine
        results = engine.strategy_b_ai_enhanced("How does scaling work?", k=2)
        assert len(results) == 2
    def test_compare_strategies(self, setup_engine):
        engine, docs = setup_engine
        comparison = engine.compare_strategies("How does scaling work?", k=2)
        assert 'query' in comparison
        assert 'strategy_a' in comparison
        assert 'strategy_b' in comparison
        assert len(comparison['strategy_a']) == 2
        assert len(comparison['strategy_b']) == 2
