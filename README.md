# ecommerce-proyecto

Proyecto e-commerce laboratorio de software

python manage.py makemigrations
python manage.py migrate

mysql
pip install mysqlclient

CORS Cross-origin resource sharing
pip install django-cors-headers

Rest framework
pip install django-cors-headers

para iniciar el proyecto (Django):
python manage.py runserver

Instalar angular
npm install -g @angular/cli

Para iniciar el proyecto (Angular):
ng serve

Para los test
python manage.py test app.tests.productoTest
python manage.py test app.tests.proveedorTest

Instalar Boostrap:
npm i bootstrap@5.3.3


Inserts de la base de datos:

INSERT INTO app_cliente(nombre, email, direccion, telefono)
VALUES
('Alejandro García Mendoza', 'agmendoza@mail.com', 'direccion1', '3001234567'),
('Miguel Sánchez Pérez', 'msanchezperez@mail.com', 'direccion2', '3011234567'),
('Isabel Torres Ruiz', 'itorresruiz@mail.com', 'direccion3', '3021234567'),
('Adriana Vargas Moreno', 'avargasm@mail.com', 'direccion4', '3031234567'),
('Roberto Guzmán Hernández', 'robertogh@mail.com', 'direccion5', '3041234567'),
('Daniela Ríos Silva', 'daniriossilva@mail.com', 'direccion6', '3051234567'),
('Luis Montoya Cárdenas', 'luismc@mail.com', 'direccion7', '3061234567'),
('Liliana López Ramírez', 'lilianalr@mail.com', 'direccion8', '3071234567'),
('Felipe Arias Galindo', 'fariasgalindo@mail.com', 'direccion9', '3081234567'),
('Camila Medina Rosales', 'camilamr@mail.com', 'direccion10', '3091234567');

INSERT INTO app_proveedor(nombre, telefono, email, direccion)
VALUES
('Empresa 1', '3001234567', 'email1@example.com', 'direccion1'),
('Empresa 2', '3012345678', 'email2@example.com', 'direccion2'),
('Empresa 3', '3023456789', 'email3@example.com', 'direccion3'),
('Empresa 4', '3034567890', 'email4@example.com', 'direccion4'),
('Empresa 5', '3045678901', 'email5@example.com', 'direccion5');

INSERT INTO app_producto(nombre, descripcion, precio, categoria, stock, proveedor_id)
VALUES
('Pantalla XYZ', 'Pantalla OLED de 32 pulgadas con resolución 8K. Ideal para diseño gráfico profesional.', 599.99, 'Pantalla', 15, 1),
('Mouse Gamer Pro', 'Mouse ergonómico con luz LED. Ideal para gaming.', 49.99, 'Mouse', 20, 2),
('Teclado Mecánico RGB', 'Teclado mecánico con luz RGB y teclas programables. Perfecto para programadores y gamers.', 79.99, 'Teclado', 17, 3),
('Disco Duro Externo 2TB', 'Disco duro externo de 2TB. Compatible con USB 3.0. Perfecto para almacenamiento de datos.', 89.99, 'Disco duro', 18, 4),
('Pantalla 4K Gamer', 'Pantalla de 27 pulgadas con tasa de refresco de 144Hz. Ideal para gaming.', 399.99, 'Pantalla', 16, 5),
('Mouse Inalámbrico', 'Mouse inalámbrico con autonomía de 30 horas. Diseño slim y ergonómico.', 29.99, 'Mouse', 19, 1),
('Teclado Inalámbrico', 'Teclado inalámbrico con autonomía de 40 horas. Conectividad Bluetooth.', 59.99, 'Teclado', 20, 2),
('Disco Duro Interno 1TB', 'Disco duro interno de 1TB. Velocidad de 7200RPM.', 49.99, 'Disco duro', 17, 3),
('Pantalla UltraWide', 'Pantalla UltraWide de 34 pulgadas. Ideal para multitasking y diseño gráfico.', 699.99, 'Pantalla', 15, 4),
('Mouse Pad Gamer', 'Mouse Pad de gran tamaño con superficie optimizada para precisión.', 19.99, 'Mouse', 20, 5),
('Teclado Compacto', 'Teclado compacto con diseño minimalista. Perfecto para trabajar en espacios reducidos.', 39.99, 'Teclado', 19, 1),
('Disco Duro SSD 500GB', 'Disco duro SSD de 500GB. Velocidad de transferencia ultra rápida.', 109.99, 'Disco duro', 18, 2),
('Pantalla Curva', 'Pantalla curva de 32 pulgadas. Perfecta para una experiencia inmersiva.', 549.99, 'Pantalla', 16, 3),
('Mouse Gamer RGB', 'Mouse gamer con luz RGB. Con 8 botones programables.', 59.99, 'Mouse', 20, 4),
('Teclado Gaming Pro', 'Teclado con switches mecánicos y luz RGB. Ideal para gaming.', 89.99, 'Teclado', 18, 5),
('Disco Duro Externo 4TB', 'Disco duro externo de 4TB. Perfecto para backup de grandes cantidades de datos.', 139.99, 'Disco duro', 17, 1),
('Pantalla Portátil', 'Pantalla portátil de 15 pulgadas. Perfecta para trabajadores nómadas.', 249.99, 'Pantalla', 19, 2),
('Mouse Ergonómico', 'Mouse ergonómico diseñado para prevenir el síndrome del túnel carpiano.', 39.99, 'Mouse', 20, 3),
('Teclado Ergonómico', 'Teclado ergonómico con apoyo para las muñecas. Perfecto para largas jornadas de trabajo.', 69.99, 'Teclado', 16, 4),
('Disco Duro SSD 1TB', 'Disco duro SSD de 1TB. Ideal para acelerar el rendimiento de tu computadora.', 159.99, 'Disco duro', 15,5);

INSERT INTO app_factura(fecha, precio, cliente_id)
VALUES
('2023-01-15 09:00:00', 0, 7),
('2023-01-28 15:00:00', 0, 3),
('2023-02-08 12:00:00', 0, 10),
('2023-02-18 16:00:00', 0, 1),
('2023-03-05 10:00:00', 0, 4),
('2023-03-22 11:00:00', 0, 6),
('2023-04-03 14:00:00', 0, 2),
('2023-04-19 10:00:00', 0, 9),
('2023-05-07 13:00:00', 0, 5),
('2023-05-20 11:00:00', 0, 7),
('2023-06-05 16:00:00', 0, 1),
('2023-06-22 09:00:00', 0, 8),
('2023-07-03 15:00:00', 0, 3),
('2023-07-10 13:00:00', 0, 6),
('2023-07-16 11:00:00', 0, 4),
('2023-07-20 14:00:00', 0, 10),
('2023-07-22 16:00:00', 0, 2),
('2023-07-25 09:00:00', 0, 9),
('2023-07-27 15:00:00', 0, 5),
('2023-07-30 10:00:00', 0, 7);

INSERT INTO app_facturaproducto(factura_id, producto_id, cantidad)
VALUES
(1, 1, 2),
(1, 4, 1),
(1, 5, 3),
(2, 2, 1),
(2, 7, 3),
(3, 3, 2),
(3, 6, 2),
(3, 9, 1),
(4, 8, 2),
(4, 10, 3),
(4, 12, 1),
(5, 11, 3),
(5, 13, 1),
(6, 14, 2),
(6, 15, 2),
(7, 16, 1),
(7, 17, 3),
(7, 18, 2),
(8, 19, 1),
(8, 20, 1),
(9, 7, 2),
(9, 5, 3),
(9, 3, 1),
(10, 1, 2),
(10, 4, 3),
(10, 9, 1),
(11, 2, 2),
(11, 6, 1),
(11, 12, 3),
(12, 10, 1),
(12, 13, 3),
(12, 11, 2),
(13, 14, 1),
(13, 15, 3),
(14, 16, 1),
(14, 17, 2),
(14, 18, 3),
(15, 19, 1),
(15, 20, 2),
(15, 8, 1);
