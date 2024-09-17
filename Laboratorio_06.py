# Ejercicio parte 01:
# Ejercicio Complejo:
# Generador de Contraseñas Seguras
# Descripción: Vamos a crear un generador de contraseñas seguras utilizando los conceptos
# que hemos aprendido hasta ahora, incluyendo funciones, módulos y control de flujo. La idea
# es que el programa genere una contraseña aleatoria con una longitud específica y asegure
# que cumple con ciertos requisitos de seguridad.
# Requisitos de seguridad de la contraseña:
# La contraseña debe tener al menos 8 caracteres.
# Debe incluir al menos una letra mayúscula y una letra minúscula.
# Debe contener al menos un número.
# Debe contener al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.).

import random
import string

def generar_contraseña(longitud):
    if longitud < 8:
        raise ValueError("La longitud de la contraseña debe ser al menos 8 caracteres.")

    # Conjuntos de caracteres
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits
    caracteres_especiales = string.punctuation

    # Asegurarse de que la contraseña tenga al menos un carácter de cada tipo
    contraseña = [
        random.choice(letras_mayusculas),
        random.choice(letras_minusculas),
        random.choice(digitos),
        random.choice(caracteres_especiales)
    ]

    # Completar la contraseña con caracteres aleatorios hasta alcanzar la longitud deseada
    todos_los_caracteres = letras_mayusculas + letras_minusculas + digitos + caracteres_especiales
    contraseña += random.choices(todos_los_caracteres, k=longitud - 4)

    # Barajar la contraseña para asegurar que los caracteres obligatorios no estén siempre al principio
    random.shuffle(contraseña)

    # Convertir la lista a una cadena y devolverla
    return ''.join(contraseña)

# Ejemplo de uso
longitud_deseada = 12
print("Contraseña generada:", generar_contraseña(longitud_deseada))