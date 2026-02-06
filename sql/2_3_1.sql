CREATE OR REPLACE VIEW top_5_products_last_month AS
WITH RECURSIVE
    category_tree AS (SELECT id,
                             name,
                             parent_id,
                             id   AS root_id,
                             name AS root_name
                      FROM categories
                      WHERE parent_id IS NULL

                      UNION ALL

                      SELECT c.id,
                             c.name,
                             c.parent_id,
                             ct.root_id,
                             ct.root_name
                      FROM categories c
                               JOIN category_tree ct
                                    ON c.parent_id = ct.id),
    last_month_order AS (SELECT id
                         FROM orders
                         WHERE order_date >= date_trunc('month', CURRENT_DATE - INTERVAL '1 month')
                           AND order_date < date_trunc('month', CURRENT_DATE)
                           AND status IN ('paid', 'shipped', 'delivered')),
    product_sales AS (SELECT p.name           AS product_name,
                             ct.root_name     AS root_category_name,
                             SUM(oi.quantity) AS quantity
                      FROM order_items oi
                               JOIN last_month_order o
                                    ON o.id = oi.order_id
                               JOIN products p
                                    ON p.id = oi.product_id
                               JOIN category_tree ct
                                    ON ct.id = p.category_id
                      GROUP BY p.name,
                               ct.root_name)
SELECT product_name,
       root_category_name,
       quantity
FROM product_sales
ORDER BY quantity DESC
LIMIT 5;

SELECT *
FROM top_5_products_last_month;