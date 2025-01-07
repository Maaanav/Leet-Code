# Write your MySQL query statement below
WITH FirstOrders AS (
    SELECT 
        customer_id,
        order_date,
        customer_pref_delivery_date
    FROM Delivery d1
    WHERE order_date = (
        SELECT MIN(order_date)
        FROM Delivery d2
        WHERE d2.customer_id = d1.customer_id
    )
)

SELECT 
    ROUND(
        (COUNT(CASE 
            WHEN order_date = customer_pref_delivery_date THEN 1 
        END) * 100.0) / COUNT(*),
        2
    ) as immediate_percentage
FROM FirstOrders;
