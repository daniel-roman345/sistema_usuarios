from app.config.settings import APP_NAME, APP_VERSION, ADMIN_USER
from app.usuarios.gestor import GestorUsuarios


def mostrar_menu():
    print("\n" + "=" * 40)
    print(APP_NAME)
    print(f"Versión: {APP_VERSION}")
    print(f"Administrador: {ADMIN_USER}")
    print("=" * 40)

    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Salir")


def main():
    gestor = GestorUsuarios()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Ingrese el nombre: ")
                edad = int(input("Ingrese la edad: "))

                mensaje = gestor.registrar_usuario(nombre, edad)
                print(mensaje)

            elif opcion == "2":
                usuarios = gestor.listar_usuarios()

                if not usuarios:
                    print("No hay usuarios registrados.")
                else:
                    print("\nUsuarios registrados:")

                    for usuario in usuarios:
                        print(
                            f"- Nombre: {usuario['nombre']}, "
                            f"Edad: {usuario['edad']}"
                        )

            elif opcion == "3":
                nombre = input("Ingrese el nombre que desea buscar: ")

                usuario = gestor.buscar_usuario(nombre)

                if usuario:
                    print(
                        f"Usuario encontrado: "
                        f"{usuario['nombre']} - {usuario['edad']} años"
                    )
                else:
                    print("Usuario no encontrado.")

            elif opcion == "4":
                print("Programa finalizado.")
                break

            else:
                print("Opción no válida.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()