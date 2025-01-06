# Write your MySQL query statement below
SELECT e1.name 
FROM Employee AS e1
WHERE EXISTS (
    SELECT 1
    FROM Employee e2
    WHERE e1.id = e2.managerId
    GROUP BY e2.managerId
    HAVING COUNT(*) >= 5
);

