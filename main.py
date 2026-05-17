"""
Main orchestration script for Semantic RAG & Vector Search
"""
import sys
import os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from src.embedding import EmbeddingGenerator
from src.vector_store import VectorStore
from src.retrieval import RetrievalEngine
from src.benchmarking import Benchmarker
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
def load_documents(filepath: str = "data/sample_documents.txt"):
    """Load documents from file and split into chunks"""
    with open(filepath, 'r') as f:
        content = f.read()
    chunks = [chunk.strip() for chunk in content.split('\n\n') if chunk.strip()]
    logger.info(f"Loaded {len(chunks)} document chunks")
    return chunks
def main():
    """Main execution function"""
    logger.info("Step 1: Loading documents...")
    documents = load_documents()
    logger.info("Step 2: Generating embeddings...")
    embedding_generator = EmbeddingGenerator(model_name="all-MiniLM-L6-v2")
    embeddings = embedding_generator.generate_embeddings(documents)
    logger.info(f"Generated embeddings with shape: {embeddings.shape}")
    logger.info("Step 3: Initializing vector store...")
    vector_store = VectorStore(dimension=embedding_generator.dimension, metric="cosine")
    vector_store.add_vectors(embeddings, documents)
    logger.info("Step 4: Initializing retrieval engine...")
    retrieval_engine = RetrievalEngine(vector_store, embedding_generator)
    logger.info("Step 5: Running benchmarks...")
    benchmarker = Benchmarker(retrieval_engine)
    test_queries = [
        "How does the system handle peak load?",
        "What security measures are implemented?",
        "How does data persistence work?"
    ]
    benchmark_results = benchmarker.run_benchmark(test_queries, k=3)
    report = benchmarker.generate_report(benchmark_results)
    print("\n" + report)
    benchmarker.save_report(benchmark_results, "benchmark_results.json")
    with open("retrieval_benchmark.md", "w") as f:
        f.write(report)
    logger.info("Report saved to retrieval_benchmark.md")
    return benchmark_results
if __name__ == "__main__":
    main()
