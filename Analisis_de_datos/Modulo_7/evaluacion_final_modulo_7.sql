--3. Revisar los datos de cada tabla mediante un SELECT *
SELECT * FROM disqueria.autores;
SELECT * FROM disqueria.discos;
SELECT * FROM disqueria.formatos;
SELECT * FROM disqueria.generos;
SELECT * FROM disqueria.productos;
--4. Existe un disco repetido en la tabla “Discos”. Crear una Query para detectarlo. Cuál es?
SELECT nombre, COUNT(*) AS discos_repetidos
FROM disqueria.discos
GROUP BY nombre
HAVING COUNT(*) > 1;
--5. Ahora que sabemos qué disco está repetido, cómo sabremos cual eliminar? Crear una Query para analizar este punto.
SELECT *
FROM disqueria.discos d
WHERE d.id NOT IN (SELECT MIN(id)
FROM disqueria.discos	
GROUP BY nombre);
-- Esta consulta arrojará el disco que se eliminará, conservando solamente el de menor id
--6. Según el análisis de la pregunta anterior, elimine el disco repetido
DELETE FROM disqueria.discos
WHERE id NOT IN (SELECT MIN(id)
FROM disqueria.discos
GROUP BY nombre);

--7. ¿Cuantos discos hay?
SELECT COUNT(*) AS cantidad_total
FROM disqueria.discos;

--8. Cree una lista de artistas, y entregue la cantidad de discos de cada uno.
SELECT a.nombre AS artista, COUNT(p.id) AS cantidad_discos -- se agrega a y p para no tener ambiguedades con los id que se repiten en las tablas.
FROM disqueria.Autores a
JOIN disqueria.discos p ON a.id = p.idAutor
GROUP BY a.id, a.nombre
ORDER BY cantidad_discos DESC;

--9. Crear una lista de géneros, indicando la cantidad de discos que pertenecen a cada uno. Si hay géneros que no tienen discos, debe aparecer un 0.
SELECT g.id, g.nombre AS genero_musical, COUNT(d.id) AS cantidad_discos
FROM disqueria.Generos g
LEFT JOIN disqueria.discos d ON g.id = d.idGenero
GROUP BY g.id, g.nombre
ORDER BY cantidad_discos DESC, g.nombre;
--10 . Indique cuantos discos distintos hay en bodega (sin importar el formato).
SELECT COUNT(DISTINCT d.id) AS discos_distintos_en_bodega
FROM disqueria.discos d
JOIN disqueria.productos pr ON d.id = pr.idDisco
WHERE pr.stock > 0;
--11. ¿Cual es, en promedio, el formato más caro?
SELECT 
    f.nombre AS formato,
    ROUND(AVG(p.precio)::numeric, 2) AS precio_promedio,
    COUNT(p.codigo) AS cantidad_productos,
    MIN(p.precio) AS precio_minimo,
    MAX(p.precio) AS precio_maximo
FROM disqueria.formatos f
JOIN disqueria.productos p ON f.id = p.idformato
GROUP BY f.id, f.nombre
HAVING COUNT(p.codigo) > 0  -- Solo formatos con productos existentes
ORDER BY precio_promedio DESC
LIMIT 1;
--12. Indique cual es el disco más caro que esté en formato vinilo y que sea de rock.
SELECT d.nombre AS disco, a.nombre AS artista, p.precio
FROM disqueria.Discos d
JOIN disqueria.Productos p ON d.id = p.idDisco
JOIN disqueria.Formatos f ON p.idFormato = f.id
JOIN disqueria.Generos g ON d.idGenero = g.id
JOIN disqueria.Autores a ON d.idAutor = a.id
WHERE f.nombre = 'Vinilo' AND g.nombre = 'Rock'
ORDER BY p.precio DESC
LIMIT 1;
--13. Crear una lista de cada producto, indicando el nombre, el género, el artista, el formato, el precio y el stock. Ordenado de más caro a más barato y por formato.
SELECT 
    d.nombre AS disco,
    g.nombre AS genero,
    a.nombre AS artista,
    f.nombre AS formato,
    p.precio,
    p.stock
FROM disqueria.Productos p
JOIN disqueria.Discos d ON p.idDisco = d.id
JOIN disqueria.Formatos f ON p.idFormato = f.id
JOIN disqueria.Generos g ON d.idGenero = g.id
JOIN disqueria.Autores a ON d.idAutor = a.id
ORDER BY p.precio DESC, f.nombre;
--14. ¿Cuál es el disco que más se repite en los productos?
SELECT d.nombre, COUNT(*) AS cantidad
FROM disqueria.Productos p
JOIN disqueria.Discos d ON p.idDisco = d.id
GROUP BY d.id, d.nombre
ORDER BY cantidad DESC
LIMIT 1;
--15. Indique cuales son los artistas que se formaron en los años 80 y cuanto suman sus productos e bodega. ¿Cuál es el que más dinero valen sus productos almacenados
SELECT 
    a.nombre,
    SUM(p.precio * p.stock) AS valor_total,
    COUNT(DISTINCT d.id) AS discos_distintos
FROM disqueria.Autores a
JOIN disqueria.Discos d ON a.id = d.idAutor
JOIN disqueria.Productos p ON d.id = p.idDisco
WHERE a.fechaFormacion BETWEEN '1980-01-01' AND '1989-12-31'
GROUP BY a.id
ORDER BY valor_total DESC;
--16. ¿Cuál es el valor de toda la bodega, sin considerar el dinero de los productos digitales?
SELECT SUM(p.precio * p.stock) AS valor_bodega
FROM disqueria.Productos p
JOIN disqueria.Formatos f ON p.idFormato = f.id
WHERE f.nombre != 'Digital';
--17. Un ladrón entró a la bodega y se llevó todos los cd de red hot chili peppers y guns n roses del estante. ¿Cuánto dinero perdió el negocio
SELECT SUM(p.precio * p.stock) AS perdida_total
FROM disqueria.Productos p
JOIN disqueria.Formatos f ON p.idFormato = f.id
JOIN disqueria.Discos d ON p.idDisco = d.id
JOIN disqueria.Autores a ON d.idAutor = a.id
WHERE f.nombre = 'CD' 
  AND a.nombre IN ('Red Hot Chili Peppers', 'Guns N Roses');
--18. Se está pensando en comprar más material para la bodega y así diversificar la colección. ¿De qué géneros musicales debería comprarse? Al mismo tiempo, se quiere liquidar stock. ¿Qué productos debería liquidarse?
-- Géneros para comprar (poco stock pero rentables)
SELECT 
    g.id,
    g.nombre AS genero,
    COUNT(DISTINCT d.id) AS cantidad_discos,
    COALESCE(SUM(p.stock), 0) AS stock_total,
    COALESCE(SUM(p.precio * p.stock), 0) AS valor_inventario
FROM disqueria.Generos g
LEFT JOIN disqueria.Discos d ON g.id = d.idGenero
LEFT JOIN disqueria.Productos p ON d.id = p.idDisco
GROUP BY g.id, g.nombre
HAVING COUNT(DISTINCT d.id) = 0       -- Géneros sin discos
    OR COALESCE(SUM(p.stock), 0) < 20 -- Géneros con bajo stock
ORDER BY valor_inventario DESC;

-- Productos para liquidar (exceso de stock y baja rotación)
SELECT 
    p.codigo,
    d.nombre AS disco,
    f.nombre AS formato,
    p.stock,
    p.precio,
    (p.precio * p.stock) AS valor_almacenado,
    ROUND((p.precio * 100 / NULLIF((SELECT AVG(precio) FROM disqueria.Productos), 0)), 2) AS porcentaje_sobre_precio_promedio
FROM disqueria.Productos p
JOIN disqueria.Discos d ON p.idDisco = d.id
JOIN disqueria.Formatos f ON p.idFormato = f.id
WHERE p.stock > (
    SELECT AVG(stock) * 1.5 FROM disqueria.Productos
)
ORDER BY p.stock DESC;