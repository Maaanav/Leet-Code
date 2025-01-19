# Write your MySQL query statement below
WITH Categories AS (
    SELECT 'Low Salary' as category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
)
SELECT 
    c.category,
    COUNT(a.account_id) as accounts_count
FROM Categories c
LEFT JOIN (
    SELECT 
        account_id,
        CASE 
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS salary_category
    FROM Accounts
) a ON c.category = a.salary_category
GROUP BY c.category;
