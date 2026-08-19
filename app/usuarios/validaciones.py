def validar_nombre(nombre):
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")

    if not nombre.replace(" ", "").isalpha():
        raise ValueError("El nombre solo puede contener letras.")

    return True


def validar_edad(edad):
    if edad < 18:
        raise ValueError("La edad debe ser igual o mayor a 18 años.")

    return True