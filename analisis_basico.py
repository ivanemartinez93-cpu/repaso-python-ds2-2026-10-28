"""Repaso de Python para análisis de datos: cuatro tareas de la consigna."""

# Tarea 1: variables con los cuatro tipos básicos.
producto = "Teclado"
precio = 125.50
stock = 12
tiene_descuento = True

# Tarea 2: lista de cinco precios, incluido el valor límite 100.
precios = [45, 100, 125.50, 80, 210]

# Tarea 3: diccionario de productos y cantidades; alta de un producto nuevo.
almacen = {"Teclado": 12, "Mouse": 25, "Monitor": 8}
almacen["Auriculares"] = 15


# Tarea 4: la función recibe exactamente una lista y devuelve un diccionario.
def resumen_estadistico(numeros):
    """Devuelve total, promedio y cantidad, sin modificar la lista recibida.

    Si la lista está vacía, el total y la cantidad son 0 y el promedio es None,
    porque no existe un promedio definido para cero elementos.
    """
    total = sum(numeros)
    cantidad = len(numeros)
    if cantidad > 0:
        promedio = total / cantidad
    else:
        promedio = None
    return {"total": total, "promedio": promedio, "cantidad": cantidad}


def main():
    """Ejecuta e imprime cada tarea en el orden de la consigna."""
    print("TAREA 1 - Variables y f-string")
    print(f"Producto: {producto}; precio: ${precio:.2f}; stock: {stock}; descuento: {tiene_descuento}")

    print("\nTAREA 2 - Bucle y condicional")
    for precio_actual in precios:
        if precio_actual > 100:
            print(f"${precio_actual:.2f}: Caro")
        else:
            print(f"${precio_actual:.2f}: Económico")

    print("\nTAREA 3 - Diccionario y stock")
    print(f"Almacén actualizado: {almacen}")
    print(f"Stock de Mouse: {almacen['Mouse']}")

    print("\nTAREA 4 - Función de resumen")
    print(f"Resumen de precios: {resumen_estadistico(precios)}")
    print(f"Ejemplo [10, 20, 30]: {resumen_estadistico([10, 20, 30])}")
    print(f"Lista vacía: {resumen_estadistico([])}")


if __name__ == "__main__":
    main()
