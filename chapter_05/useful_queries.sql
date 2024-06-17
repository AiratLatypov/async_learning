-- Запрос для получения количества записей в каждой таблице
SELECT 'brand' AS table_name, COUNT(*) AS row_count FROM brand
UNION ALL
SELECT 'product' AS table_name, COUNT(*) AS row_count FROM product
UNION ALL
SELECT 'product_color' AS table_name, COUNT(*) AS row_count FROM product_color
UNION ALL
SELECT 'product_size' AS table_name, COUNT(*) AS row_count FROM product_size
UNION ALL
SELECT 'sku' AS table_name, COUNT(*) AS row_count FROM sku;
