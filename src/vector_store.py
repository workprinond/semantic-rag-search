"""
Vector database implementation using FAISS
"""
import faiss
import numpy as np
from typing import List, Tuple, Dict, Any
import pickle
import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class VectorStore:
    """
    FAISS-based vector store for efficient similarity search
    """
    def __init__(self, dimension: int, metric: str = "cosine"):
        """
        Initialize vector store
        Args:
            dimension: Embedding dimension
            metric: Similarity metric ('cosine' or 'l2')
        """
        self.dimension = dimension
        self.metric = metric
        self.index = None
        self.metadata = []
        self.texts = []
        if metric == "cosine":
            self.index = faiss.IndexFlatIP(dimension)
        elif metric == "l2":
            self.index = faiss.IndexFlatL2(dimension)
        else:
            raise ValueError(f"Unsupported metric: {metric}. Use 'cosine' or 'l2'")
        logger.info(f"Initialized FAISS index with {metric} similarity")
    def add_vectors(self, embeddings: np.ndarray, texts: List[str], metadata: List[Dict] = None):
        """
        Add vectors to the index
        Args:
            embeddings: numpy array of embeddings
            texts: list of original texts
            metadata: list of metadata dictionaries
        """
        if len(embeddings) != len(texts):
            raise ValueError("Number of embeddings and texts must match")
        if self.metric == "cosine":
            faiss.normalize_L2(embeddings)
        self.index.add(embeddings)
        self.texts.extend(texts)
        if metadata:
            self.metadata.extend(metadata)
        else:
            self.metadata.extend([{} for _ in texts])
        logger.info(f"Added {len(embeddings)} vectors to index. Total: {self.index.ntotal}")
    def search(self, query_embedding: np.ndarray, k: int = 3) -> List[Tuple[str, float, Dict]]:
        """
        Search for similar vectors
        Args:
            query_embedding: embedding of query
            k: number of results to return
        Returns:
            List of (text, score, metadata) tuples
        """
        if query_embedding.ndim == 1:
            query_embedding = query_embedding.reshape(1, -1)
        if self.metric == "cosine":
            faiss.normalize_L2(query_embedding)
        distances, indices = self.index.search(query_embedding, min(k, self.index.ntotal))
        results = []
        for i, idx in enumerate(indices[0]):
            if idx != -1:
                if self.metric == "cosine":
                    score = (distances[0][i] + 1) / 2
                else:
                    score = 1 / (1 + distances[0][i])
                results.append((
                    self.texts[idx],
                    float(score),
                    self.metadata[idx] if idx < len(self.metadata) else {}
                ))
        return results
    def save(self, path: str):
        """Save index and metadata to disk"""
        save_path = Path(path)
        save_path.mkdir(parents=True, exist_ok=True)
        faiss.write_index(self.index, str(save_path / "index.faiss"))
        with open(save_path / "metadata.pkl", "wb") as f:
            pickle.dump({
                'texts': self.texts,
                'metadata': self.metadata,
                'dimension': self.dimension,
                'metric': self.metric
            }, f)
        logger.info(f"Saved vector store to {path}")
    def load(self, path: str):
        """Load index and metadata from disk"""
        load_path = Path(path)
        self.index = faiss.read_index(str(load_path / "index.faiss"))
        with open(load_path / "metadata.pkl", "rb") as f:
            data = pickle.load(f)
            self.texts = data['texts']
            self.metadata = data['metadata']
            self.dimension = data['dimension']
            self.metric = data['metric']
        logger.info(f"Loaded vector store from {path} with {self.index.ntotal} vectors")
