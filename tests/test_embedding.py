import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.embedding import EmbeddingGenerator, MockVertexAIEmbedding, MockGenerativeModel
class TestEmbeddingGenerator:
    def test_initialization(self):
        generator = EmbeddingGenerator()
        assert generator.dimension == 384
        assert generator.model is not None
    def test_generate_embedding(self):
        generator = EmbeddingGenerator()
        embedding = generator.generate_embedding("test text")
        assert len(embedding) == 384
    def test_generate_embeddings(self):
        generator = EmbeddingGenerator()
        embeddings = generator.generate_embeddings(["text1", "text2"])
        assert embeddings.shape == (2, 384)
    def test_mock_vertex_generate(self):
        generator = EmbeddingGenerator()
        embeddings = generator.mock_vertex_generate(["test"])
        assert len(embeddings) == 1
        assert len(embeddings[0]) == 384
class TestMockGenerativeModel:
    def test_query_expansion(self):
        model = MockGenerativeModel()
        query = "How does the system handle peak load?"
        expanded = model.generate_content(query)
        assert len(expanded) > len(query)
        assert "performance" in expanded.lower()
    def test_generic_expansion(self):
        model = MockGenerativeModel()
        expanded = model.generate_content("unknown query")
        assert "Please provide detailed information" in expanded
