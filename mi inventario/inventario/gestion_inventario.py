from .utils import cargar_datos, guardar_datos

def agregar (producto, precio, cantidad):
    productos = cargar_datos()
    nuevo = {
        "producto": producto,
        "precio" : precio,
        "cantidad": cantidad
    }
    productos.append(nuevo)
    guardar_datos(productos)
    print(f"se agrego {producto} de precio ${precio} y cantidad {cantidad}")

def eliminar(producto):
    productos = cargar_datos()
    producto_encontrado = False

    for item in productos:
        if item["producto"] == producto:
            productos.remove(item)
            producto_encontrado = True
            guardar_datos(productos)
            print(f"El producto '{producto}' ha sido eliminado.")
            break

    if not producto_encontrado:
        print(f"El producto '{producto}' no se encuentra en la lista.")





def modificar():
    productos= cargar_datos()
    producto = input("ingrese el producto: " )

    for item in productos:
        if item["producto"] == producto:
            print("___ingrese la opcion___")
            opcion = input("--1. para modificar el precio --2. para modificar la cantidad: ")

            if opcion == "1":
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                item['precio'] = nuevo_precio
                guardar_datos(productos)
                print(f"El precio del producto '{producto}' ha sido modificado a ${nuevo_precio}.")

            elif opcion == "2":
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                item['cantidad'] = nueva_cantidad
                guardar_datos(productos)
                print(f"La cantidad del producto '{producto}' ha sido modificada a {nueva_cantidad}.")

            else:
                print("Opción inválida.")

            break
    else:
        print(f"El producto '{producto}' no se encuentra en el inventario.")



def mostrar():
    productos = cargar_datos()
    if not productos:
        print("el inventario esta vacio")
        return
    else:
        print("inventario:")
        for i in productos:

            print(f"{i['producto']}:- precio ${i['precio']} - cantidad: {i['cantidad']}")
