from app.usuarios.validaciones import validar_nombre, validar_edad


class GestorUsuarios:

    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre, edad):
        validar_nombre(nombre)
        validar_edad(edad)

        usuario = {
            "nombre": nombre,
            "edad": edad
        }

        self.usuarios.append(usuario)

        return "Usuario registrado correctamente."

    def listar_usuarios(self):
        return self.usuarios

    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario["nombre"].lower() == nombre.lower():
                return usuario

        return None