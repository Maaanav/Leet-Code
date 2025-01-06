# Write your MySQL query statement below
SELECT * FROM Cinema
Where Cinema.description != 'boring' AND Cinema.id%2 != 0
ORDER BY Cinema.rating DESC; 
