-- Preguntas para resolver con consultas PostgreSQL:

-- 1. Listar todos los productos y sus precios unitarios de la tabla Ventas_Tienda.
SELECT nombre_producto, precio_unitario
FROM ventas_tienda;
-- 2. Calcular el ingreso total generado por todas las ventas.
SELECT SUM(cantidad*precio_unitario) as ventas_totales
FROM ventas_tienda;
-- 3. Contar el número total de ventas registradas.
SELECT COUNT(id_venta)
FROM ventas_tienda;
-- 4. Encontrar la fecha de la venta más antigua y la más reciente.
SELECT MIN(fecha_venta), MAX(fecha_venta)
FROM ventas_tienda;
-- 5. Mostrar la cantidad total vendida para cada nombre_producto.
SELECT nombre_producto, SUM(cantidad)
FROM public.ventas_tienda
GROUP BY nombre_producto
-- 6. Listar las ventas (todos los campos) donde el precio_unitario es superior a 100.00.
SELECT *
FROM ventas_tienda
WHERE precio_unitario > 100.00;
-- 7. Obtener la región con el mayor número de ventas (basado en el conteo de id_venta).
SELECT region, COUNT(id_venta) AS region_ventas
FROM ventas_tienda
GROUP BY region
ORDER BY region_ventas DESC
LIMIT 1;
-- 8. Calcular el total de ingresos por región, pero solo para las regiones que han generado más de 1000.00 en ingresos.
SELECT region, SUM(cantidad * precio_unitario) AS ingresos_totales
FROM Ventas_Tienda
GROUP BY region
HAVING SUM(cantidad * precio_unitario) > 1000.00
ORDER BY ingresos_totales DESC;
-- 9. Unir Ventas_Tienda con Productos para mostrar el nombre_producto, categoria y la cantidad vendida para cada venta.
SELECT nombre_producto
FROM venta_tienda
UNION ALL
SELECT categoria, 
-- 10. Contar cuántos productos diferentes hay en cada categoría de la tabla Productos.
SELECT categoria, COUNT(*) AS cantidad_productos
FROM Productos
GROUP BY categoria
ORDER BY cantidad_productos DESC;
-- 11. Listar el nombre_producto y el fabricante de los productos que tienen un stock_actual menor a 50.
SELECT nombre_producto, fabricante, stock_actual
FROM productos
WHERE stock_actual < 50
ORDER BY stock_actual DESC;
-- 12. Mostrar todas las ventas de 'Laptop Basic' y 'Monitor Full HD' utilizando UNION (elimina duplicados).
SELECT *
FROM ventas_tienda
WHERE nombre_producto = 'Laptop Basic'
UNION
SELECT *
FROM ventas_tienda
WHERE nombre_producto = 'Monitor Full HD'
ORDER BY fecha_venta, id_venta;
-- 13. Mostrar todas las ventas de 'Laptop Basic' y 'Monitor Full HD' utilizando UNION ALL (incluye duplicados).
SELECT *
FROM ventas_tienda
WHERE nombre_producto = 'Laptop Basic'
UNION ALL
SELECT *
FROM ventas_tienda
WHERE nombre_producto = 'Monitor Full HD'
ORDER BY fecha_venta, id_venta
-- 14. Encontrar el nombre_producto que ha sido vendido en más de una región.

-- 15. Calcular el total de stock_actual para cada categoría de productos.
