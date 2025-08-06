--Ejercicio 1:
--a) Para la tabla de detalle, obtener la lista de productos vendido por boleta, pero esta vez mostrar el nombre del producto y el monto vendido del producto.
SELECT *
FROM a3_m7.detalle
--b) Crear una lista de usuarios, y agregar la cantidad de dinero gastado en compras. Si no ha comprado nunca, se le debe agregar un 0.
--c) Crear la lista de Boletas, y agregar el nombre del cliente a quien le pertenece. Usar número, fecha, nombre cliente, email cliente. Si el cliente no tiene email, remplazarlo por “Sin información”.
--d) Crear una consulta que cree la lista de productos (nombre) y la cantidad de veces que se ha vendido (sin importar las unidades). Si no se ha vendido nunca, rellenar con un 0.
--e) Crear una consulta que enumere la lista de productos y la cantidad de unidades vendidas de cada una. Rellenar con 0 las que no se han vendido.
--f) Mostrar los datos de una boleta (elegir un número): Nro Boleta y Fecha; Rut, Nombre, Dirección; Detalle IVA y Total.
--g) Crear una lista de boletas, donde aparezca los datos del cliente, la cantidad de productos distintos vendidos y el subtotal pagado, sólo si el subtotal es mayor a 50.000.