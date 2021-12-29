user1=52209
password=90225
captcha=(209+5+2+2-9)
captcha2=captcha 
print ('Bienvenido al sistema de ubicación para zonas públicas WIFI')
user=int(input('Nombre de usuario: '))
if user == user1:
  if int(input ('contraseña: ')) ==password:
    verificacion=int(input ('Por favor resuelva la siguiente operación: 209+0= '))
    if verificacion == captcha:
        print('Sesión iniciada')        
    else:
        print('Error')
  else: 
    print('Error')
else:
  print('Error! Usuario no encontrado.')