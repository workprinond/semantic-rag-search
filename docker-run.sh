#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Semantic RAG - Docker Runner${NC}"
echo -e "${BLUE}========================================${NC}"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker is not installed. Please install Docker first.${NC}"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo -e "${YELLOW}⚠️  Docker Compose not found. Using docker commands instead.${NC}"
    USE_COMPOSE=false
else
    USE_COMPOSE=true
fi

# Function to build and run with docker-compose
run_with_compose() {
    echo -e "${GREEN}📦 Building Docker image...${NC}"
    docker-compose build
    
    echo -e "${GREEN}🚀 Running Semantic RAG System...${NC}"
    docker-compose up semantic-rag
}

# Function to build and run with docker
run_with_docker() {
    echo -e "${GREEN}📦 Building Docker image...${NC}"
    docker build -t semantic-rag:latest .
    
    echo -e "${GREEN}🚀 Running Semantic RAG System...${NC}"
    docker run -it --rm \
        -v $(pwd)/data:/app/data \
        -v $(pwd)/output:/app/output \
        -v $(pwd)/results:/app/results \
        semantic-rag:latest
}

# Function to run tests
run_tests() {
    echo -e "${GREEN}🧪 Running tests...${NC}"
    if [ "$USE_COMPOSE" = true ]; then
        docker-compose run --rm semantic-rag-test
    else
        docker run -it --rm \
            -v $(pwd)/data:/app/data \
            semantic-rag:latest pytest tests/ -v
    fi
}

# Function to run dev environment
run_dev() {
    echo -e "${GREEN}💻 Starting development environment...${NC}"
    if [ "$USE_COMPOSE" = true ]; then
        docker-compose up semantic-rag-dev
        echo -e "${YELLOW}To enter container: docker exec -it semantic-rag-dev bash${NC}"
    else
        docker run -it --rm \
            -v $(pwd):/app \
            -v $(pwd)/data:/app/data \
            semantic-rag:latest bash
    fi
}

# Menu
case "${1:-run}" in
    run)
        if [ "$USE_COMPOSE" = true ]; then
            run_with_compose
        else
            run_with_docker
        fi
        ;;
    test)
        run_tests
        ;;
    dev)
        run_dev
        ;;
    build)
        echo -e "${GREEN}Building image only...${NC}"
        if [ "$USE_COMPOSE" = true ]; then
            docker-compose build
        else
            docker build -t semantic-rag:latest .
        fi
        ;;
    clean)
        echo -e "${YELLOW}Cleaning up Docker resources...${NC}"
        docker system prune -f
        ;;
    help|*)
        echo -e "${GREEN}Usage: $0 {run|test|dev|build|clean}${NC}"
        echo ""
        echo "Commands:"
        echo "  run   - Build and run the RAG benchmark (default)"
        echo "  test  - Run the test suite"
        echo "  dev   - Start development environment"
        echo "  build - Build Docker image only"
        echo "  clean - Clean up Docker resources"
        echo ""
        ;;
esac

echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✅ Done!${NC}"
echo -e "${BLUE}========================================${NC}"
