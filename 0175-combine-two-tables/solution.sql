# Write your MySQL query statement below
SELECT T1.firstName, T1.lastName, T2.city, T2.state
FROM Person as T1 
LEFT JOIN Address as T2
ON T1.personId = T2.personId;
