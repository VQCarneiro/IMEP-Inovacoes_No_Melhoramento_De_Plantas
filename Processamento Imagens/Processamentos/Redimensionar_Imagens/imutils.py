########################################################################################################################
# Lavras - MG, 11/10/2019, 10:49
# Desenvolvedor: Vinícius Quintão Carneiro - Professor da Universidade Federal de Lavras - UFLA
# E-mail: vinicius.carneiro@ufla.br
# Github: VQCarneiro
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
########################################################################################################################
# Fução de translação de imagens
def translar(img,x,y):
    M = np.float32([[1,0,x],[0,1,y]])
    t = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
    return t

def rotacionar(img, angulo, centro = None, escala = 1.0):
    (lin,col) = img.shape[:2]
    if centro == None:
        centro = (col/2,lin/2)
    M = cv2.getRotationMatrix2D(centro,angulo, escala)
    img_r = cv2.warpAffine(img,M,(col,lin))
    return img_r

def redimensionar(img, largura = None, comprimento = None, inter = cv2.INTER_AREA):
    dim = None
    (lin,col) = img.shape[:2]

    if largura==None and comprimento==None:
        return img
    if largura == None:
        r = comprimento/float(lin)
        dim = (int(col*r),comprimento)
    else:
        r = largura/float(col)
        dim = (largura,int(lin*r))

    img_red = cv2.resize(img,dim, interpolation=inter)
    return img_red
