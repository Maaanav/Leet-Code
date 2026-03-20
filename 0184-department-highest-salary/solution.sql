# Write your MySQL query statement below
SELECT d.name As Department, e.name As Employee, e.salary as Salary
FROM Employee As e
JOIN Department As d ON e.departmentId = d.id
WHERE(e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary) 
    FROM Employee
    Group By departmentId);
