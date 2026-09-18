def calcular_stock(inventario):
    total = 0

    for producto in inventario:
        total = total + inventario[producto]

    return total


inventario = {}

cantidad_productos = int(input("cuantos productos vas a ingresar: "))

for i in range(cantidad_productos):
    nombre = input("ingresa el nombre del producto: ")
    cantidad = int(input("ingresa la cantidad en stock: "))

    inventario[nombre] = cantidad


total = calcular_stock(inventario)

print(f"total de unidades en stock: {total}")
print()

print("productos con stock bajo:")

for producto in inventario:
    if inventario[producto] < 5:
        print(f"{producto}: {inventario[producto]} unidades")

print()

print("resto de productos:")

for producto in inventario:
    if inventario[producto] >= 5:
        print(f"{producto}: {inventario[producto]} unidades")


with open("inventario.txt", "w") as archivo:
    for producto in inventario:
        archivo.write(f"{producto}: {inventario[producto]} unidades\n")