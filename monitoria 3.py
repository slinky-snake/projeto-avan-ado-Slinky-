with open('alunos.txt','a',encoding='utf-8') as arquivo: #exe1
    while True:
      v=str(input('escreva o nome dos alunos:')).lower()
      arquivo.write(v+'\n')
      if v =='sair':
       print('alunos cadastrados com sucesso')
       break

with open('texto.txt','r',encoding='utf-8') as arquivo:#exe2
    conteudo = arquivo.read()
    print(conteudo)
    lista=conteudo.split('\n')
    len(lista) 
    print(conteudo)
    print(len(lista))

import os#exe3
def ler_diretorios():
    diretorios= os.listdir('c:/Users/isabe/OneDrive/python_slinky/exercicios python/ADS')
    print(diretorios)
ler_diretorios()    

import pygame
pygame.init()#exe4
print('olá, eu sou um mp3 player')#nenhuma musica funcionou
pygame.mixer.music.load('nous deux.mp3')
pygame.mixer.music.play()
pygame.event.wait()



