# Write your MySQL query statement below
SELECT machine_id, ROUND(AVG(end_timestamp - start_timestamp), 3) AS processing_time
FROM (
    SELECT machine_id,
           MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_timestamp,
           MIN(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_timestamp
    FROM Activity
    GROUP BY machine_id, process_id
) subquery
GROUP BY machine_id;

