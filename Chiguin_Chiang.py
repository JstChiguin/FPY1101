listaNombresUsuario = []
listaSexos = []
listaContrasenias = []

def compruebaContrasenia(contraseniaIngresada):
    if len(contraseniaIngresada) < 8:
        return False

    if " " in contraseniaIngresada:
        return False

    contieneLetra = any(caracter.isalpha() for caracter in contraseniaIngresada)
    contieneNumero = any(caracter.isdigit() for caracter in contraseniaIngresada)

    if not contieneLetra:
        return False

    if not contieneNumero:
        return False

    print("Contraseña válida.")
    return True

def ingresarUsuario():
    while True:
        nombreNuevoUsuario = input("\nIngrese nombre de usuario: ").strip()
        if nombreNuevoUsuario in listaNombresUsuario:
            print("Usuario ya existe. Intente otro.")
        else:
            break

    while True:
        sexoUsuario = input("Ingrese sexo (M/F): ").strip().upper()
        if sexoUsuario in ['M', 'F']:
            break
        else:
            print("Debe ingresar M o F solamente. Intente de nuevo.")

    while True:
        contraseniaNueva = input("Ingrese contraseña: ")
        if compruebaContrasenia(contraseniaNueva):
            listaNombresUsuario.append(nombreNuevoUsuario)
            listaSexos.append(sexoUsuario)
            listaContrasenias.append(contraseniaNueva)
            print("Usuario ingresado con éxito!!")
            break
        else:
            print("Contraseña no válida. Intente otra.")

def buscarUsuario():
    nombreBuscado = input("\nIngrese usuario a buscar: ").strip()
    if nombreBuscado in listaNombresUsuario:
        posicion = listaNombresUsuario.index(nombreBuscado)
        sexoEncontrado = listaSexos[posicion]
        contraseniaEncontrada = listaContrasenias[posicion]
        print(f"El sexo del usuario es: {sexoEncontrado} y la contraseña es: {contraseniaEncontrada}")
    else:
        print("El usuario no se encuentra.")

def eliminarUsuario():
    nombreEliminar = input("\nIngrese usuario a eliminar: ").strip()
    if nombreEliminar in listaNombresUsuario:
        posicion = listaNombresUsuario.index(nombreEliminar)
        del listaNombresUsuario[posicion]
        del listaSexos[posicion]
        del listaContrasenias[posicion]
        print("Usuario eliminado con éxito!")
    else:
        print("No se pudo eliminar usuario!")

def mostrarMenuPrincipal():
    continuarPrograma = True
    while continuarPrograma:
        print("\nMENU PRINCIPAL")
        print("1.- Ingresar usuario.")
        print("2.- Buscar usuario.")
        print("3.- Eliminar usuario.")
        print("4.- Salir.")
        opcionElegida = input("Ingrese opción: ").strip()

        if opcionElegida == '1':
            ingresarUsuario()
        elif opcionElegida == '2':
            buscarUsuario()
        elif opcionElegida == '3':
            eliminarUsuario()
        elif opcionElegida == '4':
            print("Programa terminado...")
            continuarPrograma = False
        else:
            print("Debe ingresar una opción válida!!")

mostrarMenuPrincipal()
