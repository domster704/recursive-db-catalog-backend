SELECT c.name                                                     as client_name,
       COALESCE(SUM(order_items.quantity * order_items.price), 0) AS total_amount
FROM customers c
         LEFT JOIN orders ON c.id = orders.customer_id
         LEFT JOIN order_items ON orders.id = order_items.order_id
GROUP BY c.id, c.name
ORDER BY total_amount DESC;