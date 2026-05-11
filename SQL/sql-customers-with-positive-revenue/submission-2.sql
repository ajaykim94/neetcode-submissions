-- Write your query below
SELECT c.customer_id
FROM customers c
WHERE c.revenue > 0 AND c.year = 2020
GROUP BY c.customer_id