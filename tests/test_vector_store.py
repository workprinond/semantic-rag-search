import pytest
import numpy as np
import sys
from pathlib import Path
import tempfile
import shutil
import os

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.vector_store import VectorStore


class TestVectorStore:
    
    def test_initialization_cosine(self):
        store = VectorStore(dimension=384, metric="cosine")
        assert store.metric == "cosine"
        assert store.index is not None
        
    def test_initialization_l2(self):
        store = VectorStore(dimension=384, metric="l2")
        assert store.metric == "l2"
        
    def test_add_vectors(self):
        store = VectorStore(dimension=384)
        embeddings = np.random.rand(5, 384).astype(np.float32)
        texts = ["text" + str(i) for i in range(5)]
        store.add_vectors(embeddings, texts)
        assert store.index.ntotal == 5
        
    def test_search(self):
        store = VectorStore(dimension=384)
        embeddings = np.random.rand(3, 384).astype(np.float32)
        texts = ["doc1", "doc2", "doc3"]
        store.add_vectors(embeddings, texts)
        
        query = embeddings[0].reshape(1, -1)
        results = store.search(query, k=2)
        assert len(results) == 2
        assert results[0][0] == "doc1"
        
    def test_save_load(self):
        # Create a temporary directory manually (fix for tempfile.mkdtemp issue)
        tmpdir = tempfile.mkdtemp()
        try:
            store = VectorStore(dimension=384)
            embeddings = np.random.rand(3, 384).astype(np.float32)
            texts = ["doc1", "doc2", "doc3"]
            store.add_vectors(embeddings, texts)
            store.save(tmpdir)
            
            new_store = VectorStore(dimension=384)
            new_store.load(tmpdir)
            assert new_store.index.ntotal == 3
            assert new_store.texts == texts
        finally:
            # Clean up
            shutil.rmtree(tmpdir, ignore_errors=True)
    
    def test_search_with_different_k(self):
        store = VectorStore(dimension=384)
        embeddings = np.random.rand(5, 384).astype(np.float32)
        texts = [f"doc{i}" for i in range(5)]
        store.add_vectors(embeddings, texts)
        
        query = embeddings[0].reshape(1, -1)
        results = store.search(query, k=3)
        assert len(results) == 3
