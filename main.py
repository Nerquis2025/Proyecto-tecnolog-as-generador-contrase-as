import string
import random

def mostrar_menu():
    print("\n1. Generar contraseña")
    print("2. Reglas")
    print("3. Salir")
    return input("Elige opción: ")

def menu_generar():
    print("\n1. Contraseña Propia")
    print("2. Fácil de decir")
    print("3. Fácil de leer")
    print("4. Todos los caracteres")
    return input("Elige opción: ")

def pedir_tamano():
    while True:
        valor = input("Dime el tamaño de contraseña que quieres (mínimo 4): ")
        if valor.isdigit() and int(valor) >= 4:
            return int(valor)
        print("Por favor, ingresa un número válido mayor o igual a 4.")

def generar_contrasena_propia(tam):
    while True:
        c = input(f"Escribe tu contraseña de {tam} caracteres: ")
        if len(c) == tam:
            return c
        print(f"La contraseña debe tener exactamente {tam} caracteres.")

def generar_facil_de_decir(tam):
    letras = string.ascii_letters
    return ''.join(random.choice(letras) for _ in range(tam))

def generar_facil_de_leer(tam):
    chars = list(string.ascii_letters)
    if input("¿Quieres agregar números? (s/n): ").lower() == 's':
        chars += list(string.digits)
    if input("¿Quieres agregar símbolos? (s/n): ").lower() == 's':
        chars += list("!@#$%^&*()-_=+[]{}|;:,.<>?")
    return ''.join(random.choice(chars) for _ in range(tam))

def generar_todos_caracteres(tam):
    if input("¿Quieres usar combinación estándar? (s/n): ").lower() == 's':
        chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?"
    else:
        chars = ""
        cuenta = 0
        if input("¿Agregar mayúsculas? (s/n): ").lower() == 's':
            chars += string.ascii_uppercase
            cuenta += 1
        if input("¿Agregar minúsculas? (s/n): ").lower() == 's':
            chars += string.ascii_lowercase
            cuenta += 1
        if input("¿Agregar números? (s/n): ").lower() == 's':
            chars += string.digits
            cuenta += 1
        if input("¿Agregar símbolos? (s/n): ").lower() == 's':
            chars += "!@#$%^&*()-_=+[]{}|;:,.<>?"
            cuenta += 1
        if cuenta < 3:
            print("Debes escoger al menos 3 tipos de caracteres, usaré la combinación estándar.")
            chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?"
    return ''.join(random.choice(chars) for _ in range(tam))

def evaluar_fuerza(c):
    may = any(l.isupper() for l in c)
    min = any(l.islower() for l in c)
    num = any(l.isdigit() for l in c)
    sim = any(l in "!@#$%^&*()-_=+[]{}|;:,.<>?" for l in c)
    tipos = may + min + num + sim
    if len(c) >= 12 and tipos == 4:
        return "Fuerte"
    elif len(c) >= 8 and tipos >= 3:
        return "Media"
    else:
        return "Débil"

def mostrar_reglas():
    print("""
Reglas del generador:

1. Puedes hacer tu propia contraseña o dejar que el programa la genere.
2. Las opciones son: fácil de decir, fácil de leer, o con todos los caracteres.
3. La contraseña fuerte tiene 12 o más caracteres y combina mayúsculas, minúsculas, números y símbolos.
4. Si personalizas, debes elegir al menos 3 tipos de caracteres.
5. Las contraseñas débiles son las que tienen menos de 8 caracteres o no combinan bien.
""")

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            op_contra = menu_generar()
            if op_contra not in ["1", "2", "3", "4"]:
                print("Opción inválida.")
                continue
            while True:
                tam = pedir_tamano()
                if op_contra == "1":
                    contra = generar_contrasena_propia(tam)
                elif op_contra == "2":
                    contra = generar_facil_de_decir(tam)
                elif op_contra == "3":
                    contra = generar_facil_de_leer(tam)
                elif op_contra == "4":
                    contra = generar_todos_caracteres(tam)
                print("Tu contraseña es:", contra)
                print("Fuerza:", evaluar_fuerza(contra))
                otra = input("¿Quieres generar otra contraseña con el mismo tipo? (s/n): ")
                if otra.lower() != "s":
                    break
        elif opcion == "2":
            mostrar_reglas()
        elif opcion == "3":
            print("Gracias por usar el programa, ¡adiós!")
            break
        else:
            print("Opción inválida, intenta otra vez.")

if __name__ == "__main__":
    main()