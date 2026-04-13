"""Gestión de Productos : Una pequeña empresa desea informatizar su registro de productos activos y sus precios Actualmente la información se ingresa manualmente.
*******************************************************************************************************************
1) Generación del archivo CSV
El programa debe solicitar al usuario los siguientes datos para cada producto:

    id (entero positivo, único)

    nombre (texto de maximo 30 caracteres)

    categoría (texto: ALMACEN,LIMPIEZA,FRESCOS)

    precio (número real mayor o igual a 0)

    activo (1 = SI, 0 = NO)

Se deben controlar los ingresos con manejo de excepciones: valores vacíos, no numéricos o fuera de rango.

La carga finaliza cuando el usuario ingresa un ID vacío.

El archivo generado debe llamarse productos.csv.

*******************************************************************************************************************
2) A partir del archivo productos.csv se pide implementar un diccionario que agrupe los productos por categoria,
El diccionario debe gestionar una lista de productos activos por categoria y otra lista de productos inactivos por categoria.

*******************************************************************************************************************
3) Actualización masiva de precios para productos activos. Se solicita un porcentaje de aumento,
se procesa el arhivo productos.csv, generando un nuevo archivo llamado productos_actu.csv , el diseno de registro de este archivo sera
id, precio, categoria

########################################################################################
Restricciones técnicas

El programa debe estar dividido en funciones. Se recomienda utilizar funciones genéricas para validar ingresos numéricos y de texto.

No usar librerías externas, excepto random.

Manejar errores de entrada con try/except.

El programa principal (main) debe coordinar todas las etapas.

Si implementa listas/matrices, estas deben ser homogeneas.

import csv no se puede usar"""






