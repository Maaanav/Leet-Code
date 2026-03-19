# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary From Employee
WHERE salary != (SELECT MAX(salary) From Employee);
