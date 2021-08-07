
import cv2
import basicColor


print('========================================================================')
print('   BIENVENIDO AL PROGRAMA PRINCIPAL PROCESAMIENTO BASICO IMAGEN')
print('========================================================================')
ruta = str(input("Digite la ruta de la imagen   "))
nuevaIMG = basicColor.basicColor(ruta)
cv2.waitKey(0)
# Visualizar las propiedades de la imagen
print('-------------------------------------------------------------------------')
print('')
print(nuevaIMG.displayProperties())
print('')
print('-------------------------------------------------------------------------')
# Visualizar la imagen blanco y negro
nuevaIMG.makeBW()

# visulizar la imagen colorizada
H = int(input("Ingrese el valor Hue (H)      "))
nuevaIMG.colorize(H)
print('')
print('FIN DEL PROGRAMA')
print('========================================================================')

