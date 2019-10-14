########################################################################################################################
# Lavras - MG, 26/09/2019, 08:57
# Desenvolvedor: Vinícius Quintão Carneiro - Professor da Universidade Federal de Lavras - UFLA
# E-mail: vinicius.carneiro@ufla.br
# Github: VQCarneiro
########################################################################################################################
# Script
# Como abrir, salvar e apresentar uma imagem
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
import os # Importa o pacote os (Operation System)
########################################################################################################################
# Leitura da imagem
nome_arquivo = 'exemplo_01.jpg'

img_bgr = cv2.imread(nome_arquivo,1) # Carrega imagem colorida em BGR
img_cinza = cv2.imread(nome_arquivo,0) # Carrega imagem em escala de cinza
print(img_cinza)
lin, col, canais = np.shape(img_bgr)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Número de Canais: ' + str(canais))
########################################################################################################################
# Correção do ordenamento dos canais das imagens

# Alternativa 1:
#b,g,r = cv2.split(img_bgr)
#img_rgb = cv2.merge([r,g,b])

# Alternativa 2:
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
########################################################################################################################
# Salvar imagens

# Salvar imagem em RGB
cv2.imwrite('exemplo_01_png.png',img_bgr)

# Salvar imagem em escala de cinza
cv2.imwrite('exemplo_01_cinza.png',img_cinza)
########################################################################################################################
# Apresentar imagens

# Imagem Em RGB
plt.figure('Imagem em RGB')
plt.imshow(img_rgb)
plt.title("Imagem em RGB")

# Todas em uma única figura
plt.figure('Imagens')
plt.subplot(231)
plt.imshow(img_bgr)
plt.title("Imagem em BGR")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y

plt.subplot(233)
plt.imshow(img_rgb)
plt.title("Imagem em RGB")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y

plt.subplot(235)
plt.imshow(img_cinza, cmap = 'gray', interpolation = 'bicubic')
plt.title("Imagem em Escala de Cinza")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y
plt.show()
########################################################################################################################
