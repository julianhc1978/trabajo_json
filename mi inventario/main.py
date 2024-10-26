from inicializador_datos import inicializar_archivo_json
from inventario.gestion_inventario import agregar, mostrar, eliminar, modificar

def menu():
    print("---inventario---")
    print("1.añadir producto")
    print("2.eliminar producto")
    print("3.modificar inventario")
    print("4.mostrar inventario")
    print("5.salir")
    return input("ingrese la opcion: ")

def main():
    inicializar_archivo_json()
    while True:
        opcion = menu()
        if opcion == "1":
            producto = input("ingrese el producto: ")
            precio = input("ingrese el precio: ")
            cantidad = input("ingrese la cantidad: ")
            agregar(producto, precio, cantidad)
        elif opcion == "2":
            producto = input("ingrese el producto: ")
            eliminar(producto)
        elif opcion == "3":
            modificar()
        elif opcion == "4":
            mostrar()
        elif opcion == "5":
            break
        else:
            print("opcion no valida")

if __name__ == '__main__':
    main()

