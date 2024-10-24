print("ALMACEN COJAMEN LA MONDA")
nombre_cliente = input("Digite el nombre del cliente: ")
print("Ingrese los productos")

productos = []

def calcular_total(cantidad, precio_unitario):
  """Calcula el total de un producto."""
  return cantidad * precio_unitario

def calcular_iva(subtotal):
  """Calcula el IVA de una compra."""
  return subtotal * 0.19

def imprimir_factura(nombre_cliente, productos, subtotal, iva, total):
  """Imprime la factura con los datos proporcionados."""
  print("==========================")
  print("FACTURA")
  print("ALMACEN COJAMEN LA MONDA")
  print(f"Cliente: {nombre_cliente}")
  print("==========================")
  print("Cant.\t\tUnitario\tTotal")
  for producto in productos:
    print(f"{producto['cantidad']}\t{producto['detalle']}\t{producto['precio_unitario']}\t\t{producto['total']}")
  print("==========================")
  print(f"Subtotal:\t\t\t\t{subtotal}")
  print(f"IVA (19%):\t\t\t\t{iva}")
  print(f"Total:\t\t\t\t{total}")
  print("==========================")

# Ciclo para ingresar los productos
while True:
  detalle = input("Detalle del producto (o 'terminar' para finalizar): ")
  if detalle.lower() == 'terminar':
    break
  cantidad = int(input("Cantidad: "))
  precio_unitario = float(input("Precio unitario: "))
  total_producto = calcular_total(cantidad, precio_unitario)
  productos.append({
    'detalle': detalle,
    'cantidad': cantidad,
    'precio_unitario': precio_unitario,
    'total': total_producto
  })

# Calcular el subtotal
subtotal = sum(producto['total'] for producto in productos)

# Calcular el IVA
iva = calcular_iva(subtotal)

# Calcular el total
total = subtotal + iva

# Imprimir la factura
imprimir_factura(nombre_cliente, productos, subtotal, iva, total)
