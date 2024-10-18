import os
import subprocess

'''
==================================================
Desarrollado por: Pablo Isai Ortiz Angulo
==================================================
'''

def limpiar_pantalla():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def ejecutar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, check=True)
        return resultado
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {comando}")
        print(f"Detalles: {e}")

def mostrar_menu():
    print("\nMenu de Opciones:")
    print("1. Encontrar IP (Socket)")
    print("2. Encontrar IP (Python)")
    print("3. Encontrar subdominios")
    print("4. Banner Grabbing")
    print("5. Wad")
    print("6. Escaneo de Puertos")
    print("7. Salir")
    
def obtener_input(opcion):
    if opcion == 1:
        dominio = input("Obtener IP: ")
        comando = f"py getip.py -t {dominio}"
    elif opcion == 2:
        dominio = input("Obtener IP: ")
        comando = f"py getip2.py -t {dominio}"
    elif opcion == 3:
        dominio = input("Ingrese el dominio: ")
        comando = f"py subdominios.py -t {dominio}"
    elif opcion == 4:
        dominio = input("Ingrese el dominio: ")
        puerto = input("Ingrese el puerto: ")
        comando = f"py bannergraby.py -t {dominio} -p {puerto}"
    elif opcion == 5:
        print("Wad")
        input("Presione Enter para continuar...")
        return None
    elif opcion == 6:
        print("Escaneo de Puertos")
        input("Presione Enter para continuar...")
        return None
    elif opcion == 7:
        print("Saliendo del sistema...")
        return None
    else:
        print("Opcion no valida, intenta de nuevo.")
        return None

    return comando

def main():
    print("===========================================")
    print("Seguridad Informatica (Scripts)")
    print("Desarrollado por: Pablo Isai Ortiz Angulo")
    print("===========================================")

    input("Presione Enter para continuar...")  
    limpiar_pantalla()
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opcion: "))
            comando = obtener_input(opcion)
            
            if comando:
                ejecutar_comando(comando)
                input("Finalizado. Presione Enter para continuar...")
                limpiar_pantalla()
            elif opcion == 7:
                break  # Salir del bucle

        except ValueError:
            print("Error: Ingrese un numero valido.")

if __name__ == "__main__":
    main()
