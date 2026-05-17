================================================================================
RETRIEVAL STRATEGIES BENCHMARK REPORT
================================================================================

Query: How does the system handle peak load?
------------------------------------------------------------

Strategy A (Raw Vector Search):
----------------------------------------
+--------+---------+---------------------------------------------------------------------------------------------------------+
|   Rank |   Score | Chunk Preview                                                                                           |
+========+=========+=========================================================================================================+
|      1 |  0.7755 | Our distributed system implements automatic horizontal scaling based on CPU utilization and request ... |
+--------+---------+---------------------------------------------------------------------------------------------------------+
|      2 |  0.6785 | Rate limiting is implemented at the API gateway level using the token bucket algorithm. Each API key... |
+--------+---------+---------------------------------------------------------------------------------------------------------+
|      3 |  0.6744 | The database layer uses read replicas and sharding to handle high query volumes. Write operations ar... |
+--------+---------+---------------------------------------------------------------------------------------------------------+

Strategy B (AI-Enhanced Retrieval):
----------------------------------------
+--------+---------+---------------------------------------------------------------------------------------------------------+
|   Rank |   Score | Chunk Preview                                                                                           |
+========+=========+=========================================================================================================+
|      1 |  0.8599 | Our distributed system implements automatic horizontal scaling based on CPU utilization and request ... |
+--------+---------+---------------------------------------------------------------------------------------------------------+
|      2 |  0.7233 | The database layer uses read replicas and sharding to handle high query volumes. Write operations ar... |
+--------+---------+---------------------------------------------------------------------------------------------------------+
|      3 |  0.7061 | Rate limiting is implemented at the API gateway level using the token bucket algorithm. Each API key... |
+--------+---------+---------------------------------------------------------------------------------------------------------+

📊 Summary for this query:
   Average Score (Strategy A): 0.7095
   Average Score (Strategy B): 0.7631
   Improvement: +7.6%

============================================================

Query: What security measures are implemented?
------------------------------------------------------------

Strategy A (Raw Vector Search):
----------------------------------------
+--------+---------+---------------------------------------------------------------------------------------------------------+
|   Rank |   Score | Chunk Preview                                                                                           |
+========+=========+=========================================================================================================+
|      1 |  0.7626 | Security is implemented through multiple layers including JWT-based authentication, RBAC (Role-Based... |
+--------+---------+---------------------------------------------------------------------------------------------------------+
|      2 |  0.5852 | Rate limiting is implemented at the API gateway level using the token bucket algorithm. Each API key... |
+--------+---------+---------------------------------------------------------------------------------------------------------+
|      3 |  0.5844 | The system includes comprehensive monitoring with Prometheus metrics and Grafana dashboards. Alerts ... |
+--------+---------+---------------------------------------------------------------------------------------------------------+

Strategy B (AI-Enhanced Retrieval):
----------------------------------------
+--------+---------+---------------------------------------------------------------------------------------------------------+
|   Rank |   Score | Chunk Preview                                                                                           |
+========+=========+=========================================================================================================+
|      1 |  0.8291 | Security is implemented through multiple layers including JWT-based authentication, RBAC (Role-Based... |
+--------+---------+---------------------------------------------------------------------------------------------------------+
|      2 |  0.631  | The database layer uses read replicas and sharding to handle high query volumes. Write operations ar... |
+--------+---------+---------------------------------------------------------------------------------------------------------+
|      3 |  0.6211 | Rate limiting is implemented at the API gateway level using the token bucket algorithm. Each API key... |
+--------+---------+---------------------------------------------------------------------------------------------------------+

📊 Summary for this query:
   Average Score (Strategy A): 0.6441
   Average Score (Strategy B): 0.6937
   Improvement: +7.7%

============================================================

Query: How does data persistence work?
------------------------------------------------------------

Strategy A (Raw Vector Search):
----------------------------------------
+--------+---------+---------------------------------------------------------------------------------------------------------+
|   Rank |   Score | Chunk Preview                                                                                           |
+========+=========+=========================================================================================================+
|      1 |  0.7636 | For data persistence, we use a combination of PostgreSQL for transactional data and S3-compatible st... |
+--------+---------+---------------------------------------------------------------------------------------------------------+
|      2 |  0.7494 | The caching layer uses Redis for frequently accessed data with TTL-based expiration. Cache invalidat... |
+--------+---------+---------------------------------------------------------------------------------------------------------+
|      3 |  0.686  | The database layer uses read replicas and sharding to handle high query volumes. Write operations ar... |
+--------+---------+---------------------------------------------------------------------------------------------------------+

Strategy B (AI-Enhanced Retrieval):
----------------------------------------
+--------+---------+---------------------------------------------------------------------------------------------------------+
|   Rank |   Score | Chunk Preview                                                                                           |
+========+=========+=========================================================================================================+
|      1 |  0.8349 | For data persistence, we use a combination of PostgreSQL for transactional data and S3-compatible st... |
+--------+---------+---------------------------------------------------------------------------------------------------------+
|      2 |  0.7416 | The caching layer uses Redis for frequently accessed data with TTL-based expiration. Cache invalidat... |
+--------+---------+---------------------------------------------------------------------------------------------------------+
|      3 |  0.6759 | The database layer uses read replicas and sharding to handle high query volumes. Write operations ar... |
+--------+---------+---------------------------------------------------------------------------------------------------------+

📊 Summary for this query:
   Average Score (Strategy A): 0.7330
   Average Score (Strategy B): 0.7508
   Improvement: +2.4%

============================================================