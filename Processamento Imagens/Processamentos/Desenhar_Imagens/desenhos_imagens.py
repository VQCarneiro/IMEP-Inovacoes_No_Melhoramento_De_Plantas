########################################################################################################################
# Lavras - MG, 10/10/2019, 07:51
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
img = cv2.imread('exemplo_01.jpg',1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_recorte = img.copy()
########################################################################################################################
verde = (0,255,0)
l,c,canal = np.shape(img)
inicio,fim = int(l/2 - l/4), int(l/2 + l/4)
cv2.rectangle(img,(inicio,inicio),(fim,fim),verde,20)
########################################################################################################################
# Recorte Imagem
img_recorte = img_recorte[inicio:fim,inicio:fim]
########################################################################################################################
# Apresentar imagens
plt.figure('Canvas')
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Imagem')

plt.subplot(1,2,2)
plt.imshow(img_recorte)
plt.title('Imagem Recorte')
plt.show()
########################################################################################################################