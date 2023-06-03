import os
import time
import msvcrt

lista_ruts = []
lista_nombres_usuario = []
lista_telefonos = []
lista_edades = []
lista_correos = []
lista_contrasenas = []

while True:
    print("""Bienvenido!, aqui puedes crear tu jugador:
    1. Crear jugador.
    2. Eliminar jugador.
    3. Ver datos de jugador
    4. Modificar correo.
    5. Ver todos los jugadores(nombres).
    6. Eliminar todos los jugadores.
    7. Salir.""")
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion in (1,2,3,4,5,6,7):
                break
            else:
                print("ERROR! DEBE INGRESAR UNA OPCION VALIDA.")
        except:
             print("ERROR! DEBE INGRESAR UN NUMERO ENTERO")

    if opcion==1:
        while True:
            try:
                rut = int(input("Ingrese rut(SIN PUNTOS NI DIGITO VERIFICADOR, MINIMO 7 Y MAXIMO 8 DIGITOS.): "))
                if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                    break
                else:
                    print("ERROR! EL RUTO DEBE ESTAR ENTRE 7 Y 8")
            except:
                print("ERROR! DEBE INGRESAR UN NUMERO ENTERO.")
        while True:
            nombre_usuario = input("Ingrese nombre de usuario: ")
            if len(nombre_usuario) >= 3:
                break
            else:
                print("ERROR! SU NOMBRE DEBE TENER MAS DE 3 CARACTERES.")
        while True:
            try:
                num_celular = int(input("Ingrese su numero de telefono: "))
                if len(str(num_celular)) == 9:
                    break
                else:
                    print("ERROR! SU NUMERO DE TELEFONO DEBE TENER 9 DIGITOS.")
            except:
                print("ERROR! DEBE INGRESAR NUMEROS ENTEROS.")
        while True:
            try:
                edad = int(input("Ingrese su edad: ")) 
                if edad >= 18 and edad <= 100:
                    break
                else:
                    print("ERROR! EDAD NO VALIDA, DEBE ESTAR ENTRE 18 Y 100 AÑOS.")
            except:
                print("ERROR! DEBE INGRESAR UN NUMERO ENTERO")              
        while True:
            correo = input("Ingrese su correo: ")
            if "@" in correo:
                break
            else:
                print("ERROR! CORREO NO VALIDO")
        while True:
            contrasena = input("Por favor ingrese su contraseña(DEBE CONTENER ENTRE 6 Y 18 CARACTERES: ")
            if len(contrasena.strip()) >= 6 and len(contrasena.strip()) <= 18:
                break
            else:
                print("ERROR! CONTRASEÑA INCORRECTA, DEBE TENER ENTRE 6 Y 18 CARACTERES.")
        while True:
            val_contrasena = input("Vuelva a ingresar la contraseña: ")
            if val_contrasena == contrasena:
                break
            else:
                print("ERROR LAS CONTRASEÑAS NO COINCIDEN")

        lista_ruts.append(rut)
        lista_nombres_usuario.append(nombre_usuario)
        lista_telefonos.append(num_celular)
        lista_edades.append(edad)
        lista_correos.append(correo)
        lista_contrasenas.append(contrasena)

        print("EL USUARIO HA SIDO CREADO CON EXITO!")
        time.sleep(4.5)
        os.system ("cls")

    elif opcion==2:
        rut = int(input("Ingrese Rut: "))
        if rut in lista_ruts:
            for x in range(len(lista_ruts)):
                if rut == lista_ruts[x]:
                    posicion_encontrada = x
                    break
            lista_ruts.pop(posicion_encontrada)
            lista_nombres_usuario.pop(posicion_encontrada)
            lista_telefonos.pop(posicion_encontrada)
            lista_edades.pop(posicion_encontrada)
            lista_correos.pop(posicion_encontrada)
            lista_contrasenas.pop(posicion_encontrada)

            print("EL USUARIO HA SIDO ELIMINADO CON EXITO!!.")
        else:
            print("ERROR! EL RUT QUE HA INGRESADO NOS SE ENCUENTRA EN LA PAGINA.")
        time.sleep(4.5) 
        os.system("cls")   

    elif opcion==3:
        while True:
            try:
                rut = int(input("Ingrese el rut del jugador: "))
                if rut in lista_ruts:
                    for x in range(len(lista_ruts)):
                        if rut == lista_ruts[x]:
                            posicion_encontrada = x
                            break
                    print("DATOS DEL JUGADOR!!!: ")
                    print(lista_ruts[posicion_encontrada])
                    print(lista_nombres_usuario[posicion_encontrada])
                    print(lista_telefonos[posicion_encontrada])
                    print(lista_edades[posicion_encontrada])
                    print(lista_correos[posicion_encontrada])
                else:
                    print("ERROR!! EL RUT NO EXISTE EN NUESTRA PAGINA.")
            except:
                print("ERROR!! DEBE INGRESAR NUMEROS ENTEROS")
            time.sleep(4.5)  
            os.system("cls")              

    elif opcion==4:
        while True:
            try:
                rut = int(input("Ingrese el rut del jugador: "))
                if rut in lista_ruts:
                    for x in range (len(lista_ruts)):
                        if rut == lista_ruts[x]:
                            posicion_encontrada = x
                            break
                    nuevo_correo = input("Ingrese el nuevo correo: ")
                    if "@" in correo:
                        break
                    else:
                        print("ERROR! CORREO INCORRECTO.")
                    lista_correos[posicion_encontrada] = nuevo_correo
                    print("EL CORREO A SIDO ACUTUALIZADO CORRECTAMENTE!.")
                else:
                    print("ERROR! EL RUT NO SE ENCUENTRA REGISTRADO.")
            except:
                print("ERROR! DEBE INGRESAR NUMEROS ENTEROS.")
            time.sleep(4.5)
            os.system("cls")    

    elif opcion==5:
        print("La lista de usuarios es: ")
        print(len(lista_nombres_usuario))
        while True:
            respuesta = input("Desea salir del menu de nombres, si es asi escriba(si).")
            if respuesta.upper() == "SI":
                break
            else:
                print("ERROR! RESPUESTA NO VALIDA.")
            time.sleep(4.5)
            os.system("cls")

    elif opcion==6:
        while True:
            respuesta_sis = print("Por favor para limpiar el sistema escriba(si): ")
            if respuesta_sis.upper() == "SI":
                (len(lista_ruts.pop))
                (len(lista_nombres_usuario.pop))
                (len(lista_telefonos.pop))
                (len(lista_edades.pop))
                (len(lista_correos.pop))
                (len(lista_contrasenas.pop))

                print("EL SISTEMA A SIDO LIMPIADO CORRECTAMENTE!!")
            else:
                print("ERROR! LA OPCION INGRESADA NO ES VALIDA.") 
            time.sleep(4.5)  
            os.system("cls")

    else:
        break            


                       


                                    



         





        
                