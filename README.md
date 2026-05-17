# Semantic RAG & Vector Search System

A production-ready implementation of a Retrieval-Augmented Generation (RAG) pipeline with comprehensive benchmarking capabilities for comparing retrieval strategies.

## Features

- Local embedding generation using sentence-transformers
- FAISS-based vector database for efficient similarity search
- Two retrieval strategies:
  - **Strategy A**: Traditional embedding-based similarity search
  - **Strategy B**: AI-enhanced retrieval with query expansion
- Comprehensive benchmarking and comparison reporting
- Mocked Vertex AI integration for testing
- Pytest test suite

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/workprinond/semantic-rag-search.git
cd semantic-rag-search