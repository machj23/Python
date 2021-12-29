import time
import os
import random
user1=52209
password=90225
captcha=(209+5+2+2-9)
captcha2=captcha
Opc1=('Cambiar contraseña.')
Opc2=('Ingresar coordenadas actuales.')
Opc3=('Ubicar zona wifi mas cercana.')
Opc4=('Guardar archivo con ubicación cercana.')
Opc5=('Actualizar registros de zona wifi desde archivo.')
Opc6=('Eligir opción  de menú favorita.')
Opc7=('Cerrar sesión.')
menulist=[Opc1,Opc2,Opc3,Opc4,Opc5,Opc6,Opc7]
numberlist=[1,2,3,4,5,6,7]
counter=0 
print ('Bienvenido al sistema de ubicación para zonas públicas WIFI')
user=int(input('Nombre de usuario: '))
if user == user1:
  if int(input ('contraseña: ')) ==password:
    verificacion=int(input ('Por favor resuelva la siguiente operación: 209+0= '))
    if verificacion == captcha:
        print('Sesión iniciada')
        time.sleep(2) 
        while counter <3:
            i=1
            for menu in range (len(menulist)): 
                print(str(i),menulist[menu])
                i=i+1
            favoriteoption=int(input('Elija una opción: '))
            if favoriteoption >0 and favoriteoption <8:
                    if favoriteoption ==1: 
                        time.sleep(2)
                        print('Usted ha eligido la opción 1')
                        time.sleep(2)
                    elif favoriteoption ==2:
                        time.sleep(2)
                        print('Usted ha eligido la opción 2')
                        exit()
                    elif favoriteoption ==3:
                        print('Usted ha elegido la opción 3')
                        exit()
                    elif favoriteoption ==4:
                        time.sleep(2)
                        print('Usted ha eligido la opción 4')
                        exit()
                    elif favoriteoption ==5:
                        time.sleep(2)
                        print('Usted ha eligido la opción 5')
                        exit()
                    elif favoriteoption ==6:
                        time.sleep(2)
                        print('Usted ha eligido la opción 6')
                        newfavoriteoption=int(input('Seleccione opción favorita: '))
                        if newfavoriteoption==1 or newfavoriteoption==2 or newfavoriteoption==3 or newfavoriteoption==4 or newfavoriteoption==5:
                            if int(input('Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es” '))==0:
                                if int(input('Para confirmar por favor responda: Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es: '))==3:
                                        move=menulist[newfavoriteoption-1]
                                        menulist.remove(move)
                                        menulist.insert(0,move)
                                else:
                                    print('Error')
                                    time.sleep(2)
                            else:
                                print('Error')
                                time.sleep(2)
                        else:
                            print('Error')
                            time.sleep(2)
                            exit()
                    elif favoriteoption ==7:
                        print('Usted ha eligido la opción 7')
                        time.sleep(2)
                        print('Hasta pronto')
                        exit()
            else:
                counter+=1
                os.system('cls')
                print('Error')
                time.sleep(2)
                
    else:
        print('error')
        time.sleep(2)
  else: 
    print('error')
    time.sleep(2)
else:
  print('Error! Usuario no encontrado.')
  time.sleep(2)