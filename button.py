import os, random, sys, math
import time
import pygame

from principal import *
from pygame.locals import *
from configuracion import *
from extras import *

screen = pygame.display.set_mode((ANCHO, ALTO))
#pygame.init()
pygame.font.init()
font= pygame.font.Font('src/data/Pixeled.ttf', 15)
font2= pygame.font.Font('src/data/Pixeled.ttf', 30)


# CREAR BOTONES------------------------------------
class Button:

    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.color = (100,100,100) 
        self.set_rect()
        self.draw()
        self.clicked= False
        self.hovered = False  
    
    def set_rend(self):
        self.rend = font2.render(self.text,True,self.color)
    
    def draw(self):
        action= False
        self.set_rend()
        screen.blit(self.rend, self.rect)
        pos= pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.color= (255,255,255)
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked =True
                action= True
                
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked = False
        else:
            self.color=(100,100,100)
        return action
    
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos   
        



#CREO DISTINTOS BOTONES PARA CADA ESCENA

#BOTONES DEL MAIN MENU ----------------------------------
Play = Button("JUGAR",((ANCHO/2)-76, 150))
Options_Main_Menu = Button("OPCIONES", ((ANCHO/2)-110, 250))
Quit = Button("SALIR", ((ANCHO/2)-76, 350))


#BOTONES DEL PAUSE MENU --------------------------------
Continue = Button('CONTINUAR', ((ANCHO/2)-120,150))
Options = Button("OPCIONES", ((ANCHO/2)-105, 250))
Back_to_menu = Button('MENU PRINCIPAL', ((ANCHO/2)-170,350))

#BOTONES OPTIONS MENU -------------------------------------
Mute = Button('MUTE MUSIC',((ANCHO/2)-130,150))
unmute= Button('UNMUTE MUSIC',((ANCHO/2)-150,250))
Mute_sfx = Button('MUTE SFX',((ANCHO/2)-120,350))
#UnMute_sfx = Button('UNMUTE SFX', ((ANCHO/2)+60,300))
Back = Button('BACK',((ANCHO/2)-55,450))


#BOTONES OPTIONS IN GAME -----------------------------------

Mute_ingame = Button('MUTE MUSIC', ((ANCHO/2)-130,150))
unmute_ingame= Button('UNMUTE MUSIC',((ANCHO/2)-150,250))
Mute_sfx_ingame = Button('MUTE SFX', ((ANCHO/2)-120,350))
#UnMute_sfx_ingame = Button('UNMUTE SFX', ((ANCHO/2)+60,300))
Back_ingame = Button('BACK',((ANCHO/2)-55,450))


