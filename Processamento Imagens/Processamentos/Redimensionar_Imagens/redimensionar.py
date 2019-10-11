########################################################################################################################
# Lavras - MG, 11/10/09/2019, 10:48
# Desenvolvedor: Vinícius Quintão Carneiro - Professor da Universidade Federal de Lavras - UFLA
# E-mail: vinicius.carneiro@ufla.br
# Github: VQCarneiro
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
import imutils
########################################################################################################################
# Leitura da imagem
img = cv2.imread('exemplo_01.jpg',1) # Carrega imagem colorida em BGR
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
lin, col, canais = np.shape(img)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Número de Canais: ' + str(canais))
########################################################################################################################
# Redimensionar

# Ajustando o número de linhas para 150 pixels
r1 = 150/img.shape[1]
print(r1)
dim1=(150,int(img.shape[0]*r1))
print(dim1)
img_red1 = cv2.resize(img,dim1,interpolation=cv2.INTER_AREA)
# Ajustando o número de linhas para 50 pixels
r2 = 50/img.shape[0]
print(r2)
dim2=(int(img.shape[1]*r2),50)
print(dim2)
img_red2 = cv2.resize(img,dim2,interpolation=cv2.INTER_AREA)

########################################################################################################################
# Usando a função translação do pacote imutils
img_red3 = imutils.redimensionar(img,largura = 150)
img_red4 = imutils.redimensionar(img,comprimento = 50)
########################################################################################################################
# Apresentar imagens na tela

plt.figure('Transformações imagens')
plt.subplot(2,3,1)
plt.imshow(img)
plt.title('Imagem')

plt.subplot(2,3,2)
plt.imshow(img_red1)
plt.title('Redimensionar (150 x 150)')

plt.subplot(2,3,3)
plt.imshow(img_red2)
plt.title('Redimensionar (50 x 50)')

plt.subplot(2,3,5)
plt.imshow(img_red3)
plt.title('Redimensionar (150 x 150)')

plt.subplot(2,3,6)
plt.imshow(img_red4)
plt.title('Redimensionar (50 x 50)')

plt.show()
########################################################################################################################




