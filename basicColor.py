import this

import cv2
import sys
import os

# Cree una clase llamada basicColor:
class basicColor:
    ruta = "C:\\Users\\caroj\\Pictures"
    imagen = 0
# CONSTRUCTOR recibe como parametro la ruta de la imagen y retorna la imagen cargada
    def __init__(self, ruta):
        self.ruta = ruta
        self.imagen = cv2.imread(ruta)
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Image", 1280, 720)
        cv2.imshow("Image", self.imagen)


    # image2 = cv2.imread('C:\\Users\\caroj\\Pictures\\IMG_4986.JPG')
    # cv2.imshow('cositas', image2)
    # cv2.waitKey(1000)

    # Visualiza en pantalla el numero de pixeles en millones y el numero de canales
    def displayProperties(self):
        CantPix = self.imagen.size
        CantCanales = self.imagen.shape[2]
        return 'La imagen tiene un total de PIXELES de :' + str(CantPix) + ' y cuenta con ' + str(
            CantCanales) + ' CANALES'
    # retorna una versión binaria (método de Otsu) de la imagen
    def makeBW(self):
        image_gray = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        u, Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Image", 1280, 720)
        cv2.imshow("Image", Ibw_otsu)
        cv2.waitKey(0)
    # pide un parámetro h de entrada (entre 0 y 179) devuelve una versión colorizada de la imagen. Para generar está imagen, transforme la imagen BGR a HSV y asigne h como el valor de Hue de todos los píxeles, dejando las componentes S y V intactas. Finalmente, transforme la imagen obtenida a BGR y regrésela
    def colorize(self, H):
        # h = hsv[:,:,0]
        # s = hsv[:,:,1]
        # v = hsv[:,:,2]
        hsv_img = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2HSV)
        hsv_img[:, :, 0] = H
        out = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 1280, 720)
        cv2.imshow('image', out)
        k = cv2.waitKey(0)



