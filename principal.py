#!/usr/bin/env python
import os, random, sys, math
import time
import pygame
from pygame import mixer
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesVACIAS import *
from button import *

# SCREEN SET UP------------------------------
#screen = pygame.display.set_mode((ANCHO, ALTO))
gameClock = pygame.time.Clock()


#CARGANDO IMAGENES ---------------------------------------
square = pygame.image.load('src/images/Square.png').convert_alpha()
square2 = pygame.image.load('src/images/Square.png').convert_alpha()
square = pygame.transform.smoothscale(square, (350,350))
square2 = pygame.transform.smoothscale(square2, (350,350))
fondo = pygame.image.load('src/images/fondo.jpg').convert_alpha()


#CARGAR AUDIO//SFX----------------------------------------
pygame.mixer.init()

type = pygame.mixer.Sound('src/music/type.ogg')
click = pygame.mixer.Sound('src/music/menuclick.ogg')
continue_sfx = pygame.mixer.Sound('src/music/pause-continue-click.ogg')
continue_sfx2 = pygame.mixer.Sound('src/music/pause-retry-click.ogg')
okay_sfx = pygame.mixer.Sound('src/music/check-on.ogg')
bad_sfx = pygame.mixer.Sound('src/music/check-off.ogg')

okay_sfx.set_volume(0.2)
bad_sfx.set_volume(0.2)
mixer.music.load('src/music/Persona 5 OST 09 - Beneath the Mask -instrumental version-.mp3')
mixer.music.set_volume(0.2)


#CARGAR FUENTE//TEXTO-------------------------------------
pygame.init()
pygame.font.init()
font = pygame.font.Font('src/data/Pixeled.ttf', 15)
font2 = pygame.font.Font('src/data/Pixeled.ttf', 30)


# ESCENA DE INICIO ---------------------------------------
def start_screen():
    # variables para la animacion
    angle=0
    angle2=90
    pygame.display.set_caption("Inicio")
    last_time= time.time()
    start_screen = True
    mixer.music.play(-1)

    #mientras este en la escena de inicio, espero el input del usuario(enter) para pasar a la siguiente escena
    while start_screen:
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        screen.fill((COLOR_FONDO))

        # funcion que realiza la rotacion de los cuadrados
        blitRotateCenter(screen, square, (ANCHO/2-200,50), angle)
        blitRotateCenter(screen, square2, (ANCHO/2-200,50), angle2)

        startMessage = font.render('PRESIONA ENTER PARA COMENZAR',True,default_color)
        color_change(default_color,color_direction)
        screen.blit(startMessage,(((screen.get_width()/2-startMessage.get_width()/2) - math.sin(time.time()*5)*5 + 20),520 ))

        angle += 0.5
        angle2 -=0.5

        pygame.display.update()

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key== K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # cuando el usuario presiona enter, valor= False, salgo de esta escena y voy a main_menu
                if event.key== K_RETURN:
                    continue_sfx.play()
                    fade(ANCHO, ALTO)
                    main_menu()
                    start_screen = False
        pygame.display.update()
        gameClock.tick(60)





# ESCENA MAIN MENU --------------------------------------
def main_menu():
    main_menu = True
    pygame.display.set_caption("Menu Principal")
    # dibujo mis botones
    while main_menu:
        screen.fill((COLOR_FONDO))

        Play.draw()
        Options_Main_Menu.draw()
        Quit.draw()

        Text= font2.render('MAIN MENU',True,Violet)
        screen.blit(Text,((screen.get_width()/2-Text.get_width()/2),20))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key== K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # if Play.draw() es cuando el jugador hace click sobre el boton,
            # esto lo hago debido a que tengo el evento de click dentro de la funcion draw en la clase button
            if Play.draw():
                continue_sfx2.play()
                main()


            # if Options_Main_Menu.draw() es cuando el jugador hace click sobre el boton,
            if Options_Main_Menu.draw():
                click.play()
                options()

            # if Quit.draw() es cuando el jugador hace click sobre el boton,
            if Quit.draw():
                click.play()
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    gameClock.tick(60)


# ESCENA OPCIONES DEL MAIN MENU -------------------------------------------
def options():
    pygame.display.set_caption("Opciones")
    options = True

    while options:
        screen.fill((COLOR_FONDO))
        Mute.draw()
        unmute.draw()
        Mute_sfx.draw()
        #UnMute_sfx.draw()
        Back.draw()
        Text= font2.render('OPCIONES', True,Violet)
        screen.blit(Text,((screen.get_width()/2)-Text.get_width()/2,20))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key== K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if Back.draw():
                click.play()
                main_menu()

            if Mute.draw() and pygame.mixer.music.get_volume() > 0:
                #mixer.music.fadeout(2000)
                mixer.music.set_volume(0)

            if unmute.draw() and pygame.mixer.music.get_volume() == (0.0):
                mixer.music.set_volume(0.2)

            if Mute_sfx.draw():
                click.set_volume(0.0)
                type.set_volume(0.0)
                okay_sfx.set_volume(0.0)
                bad_sfx.set_volume(0.0)








# ESCENA  MENU IN GAME,(PAUSED SCREEN)---------------------

def options_in_game():
    global Paused
    options_in_game = True
    pygame.display.set_caption("Pausa // Opciones")
    while options_in_game:
        if pygame.mixer.music.get_volume() > 0:
            mixer.music.set_volume(0.1)
        elif pygame.mixer.music.get_volume() ==(0.0):
            mixer.music.set_volume(0)

        screen.fill((COLOR_FONDO))
        Mute_ingame.draw()
        unmute_ingame.draw()
        Mute_sfx_ingame.draw()
        #UnMute_sfx_ingame.draw()
        Back_ingame.draw()

        Text= font.render('OPCIONES', True,Soft_pink)
        screen.blit(Text,((screen.get_width()/2-Text.get_width()/2),60+ math.sin(time.time()*5)*5 - 25))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key== K_ESCAPE:
                    Paused = True
                    pause_menu()
                    options_in_game = False
                if event.key== K_DELETE:
                    Paused = True
                    pause_menu()
                    options_in_game = False

            if Mute_ingame.draw() and pygame.mixer.music.get_volume() > 0:
                #mixer.music.fadeout(2000)
                mixer.music.set_volume(0)

            if unmute_ingame.draw() and pygame.mixer.music.get_volume() == (0.0):
                mixer.music.set_volume(0.2)

            if Mute_sfx_ingame.draw():
                click.set_volume(0.0)
                type.set_volume(0.0)
                okay_sfx.set_volume(0.0)
                bad_sfx.set_volume(0.0)



            if Back_ingame.draw():
                options_in_game = False
                click.play()
                Paused = True
                pause_menu()


    pygame.display.update()
    gameClock.tick(60)




# ESCENA PAUSA MENU IN GAME -------------------------------------
Paused = False
def pause_menu():
    global Paused
    pygame.display.set_caption("Pausa")

    while Paused:
        if pygame.mixer.music.get_volume() > 0:
            mixer.music.set_volume(0.1)
        elif pygame.mixer.music.get_volume() ==(0.0):
            mixer.music.set_volume(0)

        screen.fill((COLOR_FONDO))

        pause_Text= font.render('EN PAUSA',True,Soft_pink)
        screen.blit(pause_Text,(screen.get_width()/2-pause_Text.get_width()/2,60 + math.sin(time.time()*5)*5 - 25))

        Continue.draw()
        Options.draw()
        Back_to_menu.draw()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key== K_ESCAPE:
                    Paused = False
            if Continue.draw():
                click.play()
                Paused = False

            if Options.draw():
                click.play()
                Paused = False
                options_in_game()
            if Back_to_menu.draw():
                click.play()
                #mixer.music.fadeout(2000)
                #mixer.music.set_volume(0.2)
                fade(ANCHO, ALTO)
                Paused = False
                main_menu()

    pygame.display.update()
    gameClock.tick(60)




# MAIN JUEGO----------------------------------------------







tiempoMenu = 20
puntos = 0
segundos = TIEMPO_MAX
def main():
    global puntos, last_score, puntaje_mas_alto, Paused, segundos, running, tiempoMenu

    pygame.init()
    count_down()
    #Preparar la ventana
    pygame.display.set_caption("El juego de las silabas...")

    palabra = ""
    #puntos = 0
    lemarioEnSilabas=[]
    listaPalabrasDiccionario=[]


    #lectura del diccionario
    archivo= open("src/data/lemario.txt","r",encoding='utf-8')
    lectura(archivo, listaPalabrasDiccionario)
    #elige una al azar
    palabraEnPantalla= nuevaPalabra(listaPalabrasDiccionario)
    palabraEnPantallaAnterior=""
    dibujar(screen, palabra, palabraEnPantalla,palabraEnPantallaAnterior, puntos , segundos)

    while segundos > 0:

       #Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():
            #QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            #Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                type.play()
                letra = dameLetraApretada(e.key)
                palabra += letra #es la palabra que escribe el usuario
                if e.key == K_ESCAPE:
                    Paused = True
                    pause_menu()

                if e.key == K_BACKSPACE:
                    palabra = palabra[0:len(palabra)-1]

                if e.key == K_RETURN:
                    #pasa la palabra a silabas
                    palabraEnPantallaEnSilabas=palabraTOsilaba(palabraEnPantalla)
                    print(palabraEnPantallaEnSilabas)
                    print(silabasTOpalabra(palabra))
                    palabraEnPantallaAnterior= palabraEnPantallaEnSilabas
                    if esCorrecta(palabraEnPantallaEnSilabas, palabra):
                        okay_sfx.play()
                        puntos+=puntaje(palabra)
                    else:
                        bad_sfx.play()
                        puntos-=5
                    #elige una al azar


                    palabraEnPantalla = nuevaPalabra(listaPalabrasDiccionario)
                    palabra = ""

        segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000 + tiempoMenu

        #Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)
        #Dibujar de nuevo todo
        dibujar(screen, palabra, palabraEnPantalla,palabraEnPantallaAnterior, puntos,segundos)
        gameClock.tick(60)
        pygame.display.update()
        pygame.display.flip()



    while 1:
        end_screen()
    archivo.close()




#END// GAME OVER SCREEN ----------------------------------------------------

def end_screen():
    global Puntos, segundos, TIEMPO_MAX
    End = True
    pygame.display.set_caption("Juego Terminado")

    radius = 800
    while End:

        # Animacion del circulo
        dt = gameClock.tick(60)/1000
        circle_speed = 1100
        radius -= circle_speed * dt
        if radius < 0:
            radius = 0
        x, y = int(ANCHO/2), int(ALTO/2)
        pygame.draw.circle(screen,((255,255,255)),(x,y),int(radius))
        pygame.display.flip()
        screen.fill((COLOR_FONDO))


        Time_over= font.render('SE ACABO EL TIEMPO',True,(255,0,0))
        screen.blit(Time_over,((screen.get_width()/2-Time_over.get_width()/2),30))

        Score = font.render('Puntos: ' + str(puntos), True, (255,255,255))
        screen.blit(Score,((screen.get_width()/2-Score.get_width()/2),90))

        #Score_highest = font.render('Puntaje Mas Alto: ' + str(puntaje_mas_alto), True, (255,255,255))
        #screen.blit(Score_highest,((screen.get_width()/2-Score_highest.get_width()/2),150))

        Retry = font.render('Presiona Espacio Para Reintentar', True, (255,255,255))
        screen.blit(Retry,(((screen.get_width()/2-Retry.get_width()/2) - math.sin(time.time()*5)*5 + 20),200))


        Menu = font.render('Presiona ESC para ir al menu principal', True, (255,255,255))
        screen.blit(Menu,(((screen.get_width()/2-Menu.get_width()/2) + math.sin(time.time()*5)*5 + 20),300))


        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key == K_SPACE:
                    if segundos <=0:
                        print(segundos)
                        fade(ANCHO, ALTO)

                        segundos = 60
                        End = False

                        main()

                    #puntos = 0

                if event.key== K_ESCAPE:
                    fade(ANCHO, ALTO)
                    End = False
                    segundos = 60
                    main_menu()
    pygame.display.update()
    gameClock.tick(60)


#Programa Principal ejecuta Main

if __name__== '__main__':
    start_screen()
