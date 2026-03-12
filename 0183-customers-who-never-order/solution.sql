# Write your MySQL query statement below
SELECT c.name As Customers
from Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.customerId IS NULL;
