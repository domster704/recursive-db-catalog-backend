WITH root_categories AS (SELECT id, name
                         FROM categories
                         WHERE parent_id IS NULL)
SELECT r.id,
       r.name,
       COUNT(c.id) AS children_count
FROM root_categories r
         LEFT JOIN categories c
                   ON c.parent_id = r.id
GROUP BY r.id, r.name;
