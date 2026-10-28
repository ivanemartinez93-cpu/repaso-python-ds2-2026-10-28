"""Práctica opcional: repaso de Python para análisis de datos."""

# Variables y resumen de producto.
producto = "Teclado"
precio = 125.50
stock = 12
tiene_descuento = True
print(f"Producto: {producto}; precio: ${precio:.2f}; stock: {stock}; descuento: {tiene_descuento}")

# Clasificación de precios: 100 inclusive se considera económico.
precios = [45, 100, 125.50, 80, 210]
for valor in precios:
    categoria = "Caro" if valor > 100 else "Económico"
    print(f"${valor:.2f}: {categoria}")

# Registro de stock y alta de un producto.
almacen = {"Teclado": 12, "Mouse": 25, "Monitor": 8}
almacen["Auriculares"] = 15
print(f"Stock de Mouse: {almacen['Mouse']}")

# Estadísticas básicas, incluyendo el caso de una lista vacía.
def resumen_estadistico(numeros):
    total = sum(numeros)
    cantidad = len(numeros)
    promedio = total / cantidad if cantidad else None
    return {"total": total, "promedio": promedio, "cantidad": cantidad}


print("Resumen:", resumen_estadistico(precios))
