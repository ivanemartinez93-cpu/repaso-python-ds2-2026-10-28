# Repaso de Python para análisis de datos

Práctica opcional del módulo 1 de Data Science II. Versión 2, 28/10/2026.

El programa resuelve las cuatro tareas de la consigna con Python estándar. No requiere datos externos, credenciales, instalaciones de paquetes ni configuración adicional.

## Ejecutar desde cero

1. Instalar Python 3.10 o posterior.
2. Descargar el repositorio como ZIP y extraerlo, o clonarlo.
3. Abrir una terminal en la carpeta que contiene `analisis_basico.py`.
4. Ejecutar:

```text
python analisis_basico.py
python -m unittest -v test_analisis_basico
```

En Windows también puede usarse `py` en lugar de `python`. En sistemas que lo requieran, usar `python3`.

## Correspondencia con la consigna

| Requisito | Implementación | Evidencia |
| --- | --- | --- |
| Archivo Python y README | `analisis_basico.py` y este documento en la raíz | Archivos del repositorio |
| Variables str, float, int y bool | `producto`, `precio`, `stock`, `tiene_descuento` | Tarea 1 de la salida y `test_tipos_basicos` |
| Frase con f-string | Resumen del producto en `main()` | Tarea 1 de la salida |
| Lista `precios` con al menos 5 valores | Lista global de cinco números | `test_lista_y_diccionario` |
| Bucle y condicional: Caro si >100; Económico si <=100 | `for` con `if/else` explícito | Tarea 2 y `test_salida_y_umbral` |
| Diccionario `almacen`, alta y consulta | Se agrega Auriculares y se consulta Mouse | Tarea 3 y `test_lista_y_diccionario` |
| `def resumen_estadistico(numeros)` | Un único parámetro y retorno de diccionario | Pruebas de firma, ejemplo, decimales y lista vacía |
| Llamada de ejemplo impresa | Lista `precios`, `[10, 20, 30]` y lista vacía | Tarea 4 de la salida |
| Comentarios y código ejecutable | Comentarios por tarea y docstrings | Ejecución y ocho pruebas automatizadas |

## Resultados y contrato de la función

`resumen_estadistico` devuelve las claves `total`, `promedio` y `cantidad`. No cambia la lista recibida. Para `[10, 20, 30]` devuelve `{'total': 60, 'promedio': 20.0, 'cantidad': 3}`. Para `precios`, el total es 560.5, el promedio 112.1 y la cantidad 5. Para una lista vacía devuelve total 0, cantidad 0 y promedio `None`, evitando una división por cero.

`evidencia_ejecucion.txt` contiene la salida real del programa y de las pruebas realizadas con Python 3.12.14. Se puede reproducir con los comandos anteriores. Los archivos `.txt` correspondientes a los scripts son copias idénticas de su código completo.

## Cambios de la versión 2

Se hizo explícito el `if/else` de clasificación, se separó la ejecución en `main()` para permitir importar y probar el módulo, se documentó cada criterio y se agregaron pruebas y evidencia de ejecución. La versión anterior se conserva en el historial de GitHub y en la copia local/Drive de la versión 1.
