# Write your MySQL query statement below
WITH QueryStats AS (
    SELECT 
        query_name,
        AVG(CAST(rating AS DECIMAL) / CAST(position AS DECIMAL)) AS avg_ratio,
        SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) AS poor_query_count,
        COUNT(*) AS total_queries
    FROM 
        Queries
    GROUP BY 
        query_name
)

SELECT 
    query_name,
    ROUND(avg_ratio, 2) AS quality,
    ROUND(CAST(poor_query_count AS DECIMAL) / CAST(total_queries AS DECIMAL) * 100, 2) AS poor_query_percentage
FROM 
    QueryStats;
