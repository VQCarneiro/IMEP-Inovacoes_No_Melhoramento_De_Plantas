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
# Gerar imagem
canvas = np.zeros((300,300,3),dtype="uint8")
########################################################################################################################
# Gerar desenhos

vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

cv2.line(canvas,(0,300),(300,0),vermelho,3)
cv2.line(canvas,(0,0),(300,300),verde,3)
cv2.rectangle(canvas,(10,10),(60,60),vermelho)
cv2.rectangle(canvas,(50,200),(200,225),azul,-1)
########################################################################################################################
# Apresentar imagens
plt.figure('Canvas')
plt.imshow(canvas)
plt.title('Imagem')
plt.show()
########################################################################################################################
