#############################################################################################
# Cabeçalho
# Data: 10/03/2019
# Horário: 10:51
# Desenvolvedor: Vinícius Quintão Carneiro
# Imagens: Abóboras
# Propietário das imagens: Ronaldo Machado Júnior
# Procedimento: Recortar imagens
#############################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
#import imutils
########################################################################################################################
# Leitura da imagem
img = cv2.imread('exemplo_01.jpg',1) # Carrega imagem colorida em BGR
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
lin, col, canais = np.shape(img)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Número de Canais: ' + str(canais))
########################################################################################################################
# Cropping - Recortar partes de imagens
img_recorte = img[1000:2500,1000:2500]
########################################################################################################################
# Apresentar imagens na tela

plt.figure('Transformações imagens')
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Imagem')

plt.subplot(1,2,2)
plt.imshow(img_recorte)
plt.title('Recorte')

plt.show()
########################################################################################################################




