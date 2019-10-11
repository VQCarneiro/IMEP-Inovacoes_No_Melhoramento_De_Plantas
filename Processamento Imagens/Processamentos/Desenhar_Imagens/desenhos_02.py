########################################################################################################################
# Lavras - MG, 11/10/2019, 10:41
# Desenvolvedor: Vinícius Quintão Carneiro - Professor da Universidade Federal de Lavras - UFLA
# E-mail: vinicius.carneiro@ufla.br
# Github: VQCarneiro
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Exemplo 1
########################################################################################################################
# Gerar imagem
canvas = np.zeros((300,300,3),dtype="uint8")
xcentro,ycentro = canvas.shape[1]/2, canvas.shape[0]/2
xcentro = int(xcentro)
xcentro = int(ycentro)
########################################################################################################################
# Gerar circulos
branco = (255,255,255)
for r in range(0,175,25):
    print(r)
    cv2.circle(canvas,(150,150),int(r),branco)
########################################################################################################################
# Apresentar imagem na tela
plt.figure('Circulos 01')
plt.imshow(canvas)
########################################################################################################################
# Exemplo 2
########################################################################################################################
# Gerar imagem
canvas = np.zeros((300,300,3),dtype="uint8")
########################################################################################################################
# Gerar circulos
for i in range(0,25):
    raios = np.random.randint(5,high=200)
    cor = np.random.randint(0,high=256,size= (3,)).tolist()
    pt = np.random.randint(0,high=300,size=(2,))
    cv2.circle(canvas,tuple(pt),raios,cor,-1)
########################################################################################################################
# Apresentar imagem na tela
plt.figure('Circulos 02')
plt.imshow(canvas)
plt.show()
########################################################################################################################





