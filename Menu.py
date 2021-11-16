def header():
    print('_______________________________________________________________________________')
    print()
    print('                 /////////       //////////     /////////')
    print('                 //              //     //      //')
    print('                 //              ////////       //////')
    print('                 //   ////       //                 /////')
    print('                 //     //       //                    //')
    print('                 /////////       //             /////////') 
    print()
    print('                 C       U       P       I       D       O')
    print()
    print('>>>------Calcularemos la ruta mas rápida y segura para ver a tu pareja------->')
    print('_______________________________________________________________________________')

def menu():
    print('')
    print('>>>------MENÚ PRINCIPAL------->')
    print('Ingrese una de las siguiente opciones\n')
    print('[1] Iniciar GPS\n')
    print('[2] Sobre nosotros\n')
    print('[3] Contáctanos\n')
    print('[0] Cerrar GPS Cupidon\n')


def gps():
    print('')
    print('>>>------INICIAR GPS------->')
    print('Ingresa uno de las siguientes destinos:\n')
    print('[1] Discoteca The Darkness: Carrera 14 con Calle 50\n')
    print('[2] Bar La Pasión: Calle 54 con Carrera 11\n')
    print('[3] Cervecería Mi Rolita: Calle 50 con Carrera 12\n')
    print('[0] Volver a menú principal\n')

def aboutUs():
    print('')
    print('>>>------SOBRE NOSOTROS------->\n')
    print('GPS Cupido es una compañia en busca de unir amores prohibidos')
    print('y evitar desgracias como las que vivieron Romeo y Julieta')
    print('proporcionando rutas rápidas y seguras para que tu y tu pareja')
    print('lleguen a sus destinos deseados sin ser vistos por sus padres.\n')
    print('[0] Regresar a menú principal\n')

def contact():
    print('')
    print('>>>------CONTACTANOS------->\n')
    name = input("Ingrese su nombre y apellido: \n")
    email = input("Ingrese su correo electrónico: \n")
    content = input("¿Cuál es el motivo de su mensaje?: \n")
    print('\n\n¿Deseas enviar este mensaje?')
    print('De:', name, ': <', email, '>')
    print('Para: GPS Cupido\n')
    print(content)
    print('\n[1] Enviar\n')

header()
menu()
optionMenu = int(input("Ingrese su opción deseada: \n"))

while optionMenu != 0:

    if optionMenu == 1:
        gps()
        optionGps = int(input("Ingrese su opción deseada: \n"))

        while optionGps != 0:
            if optionGps == 1:
                print('Discoteca The Darkness: Carrera 14 con Calle 50')
            elif optionGps == 2:
                print('[2] Bar La Pasión: Calle 54 con Carrera 11\n')
            elif optionGps == 3:
                print('[3] Cervecería Mi Rolita: Calle 50 con Carrera 12\n')
            else:
                print('Opción invalida\n')
            gps()
            optionGps = int(input("Ingrese su opción deseada: \n"))

    elif optionMenu == 2:
        aboutUs()
        optionAboutUs = int(input("Ingrese su opción deseada: \n"))

        while optionAboutUs != 0:
            print('Opción invalida\n')
            aboutUs()
            optionAboutUs = int(input("Ingrese su opción deseada: \n"))

    elif optionMenu == 3:
        contact()
        optionContact = int(input("Ingrese su opción deseada: \n"))

        while optionContact != 1:
            print('Opción invalida\n')
            optionContact = int(input("Ingrese su opción deseada: \n"))
        print('______________________________________________________________________________')
        print('|¡Gracias por tu mensaje! Te contactaremos en cuanto llegue la luz al cuarto  |\n')
        print('|de servidores. ¡Por parte del equipo de GPS Cupido te deseamos un feliz día! |\n')
        print('|_____________________________________________________________________________|')

    else:
        print('Opción invalida\n')
    menu()
    optionMenu = int(input("Ingrese su opción deseada: \n"))


print('\nProyecto 1 - Modelación de Sistemas en Redes')
print('Profesor Rafael Matienzo')
print('Integrantes:')
print('     Oriana González')
print('     Luis Stanislao')
print('     Guillermo Sosa')
print('\nGPS Cupido finalizado\n')



