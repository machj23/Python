import time
import os
import random
import numpy as np

#region
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
coordinatelist=[]
mat=[[None,None],
    [None,None],
    [None,None]]
#endregion
def list():
    i=1
    for menu in range (len(menulist)): 
        print(str(i),menulist[menu])
        i=i+1

def passwords(lock1,lock2):
    if lock1==lock2:
        return True
    else:
        return False

def coordinate(originallist):
    newcoordinate = []
    for x in range (3):
        latitude=input('Ingrese su latitud: ')
        latitude=float(latitude)
        if latitude<=-3.002 and latitude>=-4.227:
            longitude=input('Ingrese su longitud: ')
            longitude=float(longitude) 
            if longitude<=-69.714 and longitude>=-70.365:
                coord = [latitude, longitude]
                newcoordinate.append(coord)
            else:
                print('error coordenada')
                time.sleep(1)
                print('Hasta pronto')
                exit()
            
        else: 
            print('error coordenada')
            time.sleep(1)
            print('Hasta pronto')
            exit()            
    return newcoordinate

def printingcoordinates(originallist):
    #newlisting2=[originallist]
    print('Sus coordenadas son: ')
    for x in range(0, len(originallist)):
        item = x + 1
        print(f"{item}. Coordenada Latitud: '{originallist[x][0]}' Coordenada Longitud: '{originallist[x][1]}'")
    sortinglatitudes(originallist)
    coordinateupdate=int(input('Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú: '))
    if coordinateupdate==0:
        time.sleep(1)
    elif coordinateupdate !=1 and coordinateupdate !=2 and coordinateupdate !=3:
        print('Error actualización')
        exit()
    else:
        updatingcoordinates(coordinateupdate,originallist)

def sortinglatitudes(orginallist):
    print (f"Coordenada ubicada más al occidente {min (posicion[1] for posicion in orginallist)}")
    print (f"Coordenada promedio de todos los puntos: {(orginallist[0][1]+orginallist[1][1]+orginallist[2][1])/3}")

def updatingcoordinates(coordinateupdate,originallist):
    coordinateupdate=-1
    newcoordinate=[originallist]
    latitude=input('Ingrese su latitud: ')
    latitude=float(latitude)
    if latitude<=-3.002 and latitude>=-4.227:
        longitude=input('Ingrese su longitud: ')
        longitude=float(longitude) 
        if longitude<=-69.714 and longitude>=-70.365:
            newcoordinate[coordinateupdate].insert(0,latitude)
            newcoordinate[coordinateupdate].insert(1,longitude)
        else:
            print('Error coordenada')
            time.sleep(1)
            print('Hasta pronto')
            exit()
        
    else: 
        print('Error coordenada')
        time.sleep(1)
        print('Hasta pronto')
        exit()   

print ('Bienvenido al sistema de ubicación para zonas públicas WIFI')
#region Inicio de Sistema
if passwords(int(input('Nombre de usuario: ')), user1):
    if passwords (int(input ('contraseña: ')),password):
        verificacion=int(input ('Por favor resuelva la siguiente operación: 209+0= '))
        if verificacion == captcha:
            print('Sesión iniciada')
            time.sleep(2)
            #region Menu Principal
            while counter <3:
                list()
                favoriteoption=int(input('Elija una opción: '))
                if favoriteoption >0 and favoriteoption <8:
                        if favoriteoption ==1: 
                            time.sleep(1)
                            print('Usted ha eligido la opción 1')
                            time.sleep(1)
                            if passwords (int(input('Confirme la contraseña actual: ')),password):
                                newpassword=input('Ingrese la nueva contraseña: ')
                                if passwords (password,newpassword):
                                    print('La contraseña no puede coincidir')
                                else:
                                    if passwords (input('Confirme la nueva contraseña: '),newpassword):
                                        pass
                                    else:
                                        time.sleep(1)
                                        print('Error')
                                        exit()
                            else:
                                print('Error')
                                time.sleep(1)
                                exit()
                        elif favoriteoption ==2:
                            time.sleep(1)
                            print('Usted ha eligido la opción 2')
                            if coordinatelist==[]:
                                coordinatelist=coordinate(coordinatelist)
                            else:
                                printingcoordinates(coordinatelist)
                        elif favoriteoption ==3:
                            time.sleep(1)
                            print('Usted ha eligido la opción 3')
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
            #endregion
        else:
            print('Error')
            time.sleep(2)
    else: 
        print('Error')
        time.sleep(2)
else:
    print('Error! Usuario no encontrado.')
    time.sleep(2)
#endregion