#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

#Para tocar a musica precisamos copiar para dentro da mesma pasta a musica que deseja-se ouvir, basta copiar a musica (CRTL+C) e depois colar na pasta do projeto do pycharm (CRTL+V)
# Importando o método necessário dentro da bibliotéca o método mixer serve para tocar musicar dentro do python
from pygame import mixer

# O método "mixer" assim como o método pygame precisa de um comando para ser iniciaizado.
mixer.init()

# Vamos carregar a musica desejada
mixer.music.load('desafio021.mp3')

#vamos dar o play na musica carregada
mixer.music.play()

#neste caso vamos dar um imput para comecar tocar a musica
input('Aperrte a tecla enter para sair.! ')

#Desafio concluído