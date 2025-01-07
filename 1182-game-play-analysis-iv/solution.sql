# Write your MySQL query statement below
WITH FirstLogins AS (
    SELECT 
        player_id, 
        MIN(event_date) as first_login,
        DATE_ADD(MIN(event_date), INTERVAL 1 DAY) as next_day
    FROM Activity 
    GROUP BY player_id
),
ConsecutiveLogins AS (
    SELECT 
        f.player_id,
        CASE 
            WHEN EXISTS (
                SELECT 1 
                FROM Activity a 
                WHERE a.player_id = f.player_id 
                AND a.event_date = f.next_day
            ) THEN 1
            ELSE 0
        END as logged_in_next_day
    FROM FirstLogins f
)

SELECT 
    ROUND(
        SUM(logged_in_next_day) / COUNT(*), 
        2
    ) as fraction
FROM ConsecutiveLogins;
