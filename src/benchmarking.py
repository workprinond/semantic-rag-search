"""
Benchmarking module to compare retrieval strategies
"""
from typing import List, Dict
import json
from tabulate import tabulate
from .retrieval import RetrievalEngine
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class Benchmarker:
    """
    Benchmark different retrieval strategies
    """
    def __init__(self, retrieval_engine: RetrievalEngine):
        self.retrieval_engine = retrieval_engine
    def run_benchmark(self, queries: List[str], k: int = 3) -> Dict:
        """
        Run benchmark on multiple queries
        Args:
            queries: List of test queries
            k: Number of results to retrieve
        Returns:
            Benchmark results dictionary
        """
        results = {}
        for query in queries:
            logger.info(f"Benchmarking query: {query}")
            comparison = self.retrieval_engine.compare_strategies(query, k)
            results[query] = comparison
        return results
    def generate_report(self, benchmark_results: Dict) -> str:
        """
        Generate formatted report from benchmark results
        """
        report = []
        report.append("=" * 80)
        report.append("RETRIEVAL STRATEGIES BENCHMARK REPORT")
        report.append("=" * 80)
        for query, results in benchmark_results.items():
            report.append(f"\nQuery: {query}")
            report.append("-" * 60)
            report.append("\nStrategy A (Raw Vector Search):")
            report.append("-" * 40)
            table_a = []
            for i, item in enumerate(results['strategy_a'], 1):
                score_str = f"{item['score']:.4f}"
                text_preview = item['text'][:100] + "..." if len(item['text']) > 100 else item['text']
                table_a.append([i, score_str, text_preview])
            if table_a:
                report.append(tabulate(table_a, headers=["Rank", "Score", "Chunk Preview"], tablefmt="grid"))
            else:
                report.append("No results found")
            report.append("\nStrategy B (AI-Enhanced Retrieval):")
            report.append("-" * 40)
            table_b = []
            for i, item in enumerate(results['strategy_b'], 1):
                score_str = f"{item['score']:.4f}"
                text_preview = item['text'][:100] + "..." if len(item['text']) > 100 else item['text']
                table_b.append([i, score_str, text_preview])
            if table_b:
                report.append(tabulate(table_b, headers=["Rank", "Score", "Chunk Preview"], tablefmt="grid"))
            else:
                report.append("No results found")
            if table_a and table_b:
                avg_score_a = sum([float(row[1]) for row in table_a]) / len(table_a)
                avg_score_b = sum([float(row[1]) for row in table_b]) / len(table_b)
                improvement = ((avg_score_b - avg_score_a) / avg_score_a) * 100 if avg_score_a > 0 else 0
                report.append(f"\n📊 Summary for this query:")
                report.append(f"   Average Score (Strategy A): {avg_score_a:.4f}")
                report.append(f"   Average Score (Strategy B): {avg_score_b:.4f}")
                report.append(f"   Improvement: {improvement:+.1f}%")
            report.append("\n" + "=" * 60)
        return "\n".join(report)
    def save_report(self, benchmark_results: Dict, filepath: str):
        """Save benchmark results to JSON file"""
        def convert_to_serializable(obj):
            if hasattr(obj, 'tolist'):
                return obj.tolist()
            return obj
        with open(filepath, 'w') as f:
            json.dump(benchmark_results, f, indent=2, default=convert_to_serializable)
        logger.info(f"Saved benchmark results to {filepath}")
