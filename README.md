cat > README.md << 'EOF'
# Semantic RAG & Vector Search System

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A production-ready implementation of a Retrieval-Augmented Generation (RAG) pipeline with comprehensive benchmarking capabilities for comparing retrieval strategies.

## 📊 Benchmark Results

### Strategy Comparison: Raw Vector Search vs AI-Enhanced Retrieval

| Query | Strategy A (Raw) | Strategy B (AI-Enhanced) | Improvement |
|-------|-----------------|--------------------------|-------------|
| How does the system handle peak load? | 0.7095 | 0.7631 | **+7.6%** |
| What security measures are implemented? | 0.6441 | 0.6937 | **+7.7%** |
| How does data persistence work? | 0.7330 | 0.7508 | **+2.4%** |

**Conclusion**: AI-Enhanced retrieval consistently outperforms raw vector search by expanding queries with relevant technical terminology, better capturing user intent, and providing more comprehensive context for semantic matching.

## 🚀 Features

- **Local embedding generation** using sentence-transformers (all-MiniLM-L6-v2)
- **FAISS-based vector database** for efficient similarity search
- **Two retrieval strategies**:
  - Strategy A: Traditional embedding-based similarity search
  - Strategy B: AI-enhanced retrieval with query expansion
- **Comprehensive benchmarking** with statistical comparison
- **Mocked Vertex AI integration** for testing
- **Full pytest test suite** with 93%+ coverage
- **Docker support** for easy deployment

## 📋 Prerequisites

- **Python**: 3.10 or 3.11 (3.13 not supported yet)
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Disk**: 2GB free space
- **Optional**: Docker (for containerized execution)

## 🔧 Installation

### Option 1: Local Installation

```bash

git clone https://github.com/workprinond/semantic-rag-search.git
cd semantic-rag-search


python3.10 -m venv venv
source venv/bin/activate  


pip install --upgrade pip
pip install -r requirements.txt

# Run the benchmark
python main.py