# Write your MySQL query statement below
SELECT customer_number 
FROM (
    SELECT customer_number,
        RANK() OVER (ORDER BY COUNT(customer_number) DESC) AS rnk
    FROM Orders
    GROUP BY customer_number
) AS temp
Where rnk = 1;




