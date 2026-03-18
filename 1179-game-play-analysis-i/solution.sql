# Write your MySQL query statement below
SELECT player_id, MIN(event_date) As first_login     
FROM Activity
GROUP BY player_id;

