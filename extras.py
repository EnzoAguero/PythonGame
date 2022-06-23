#!/usr/bin/env python
import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == 59:
        return("ñ")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def dibujar(screen, palabraUsuario, palabraActual,palabraAnterior, puntos, segundos):
    font= pygame.font.Font('src/data/Pixeled.ttf', TAMANNO_LETRA)
    font2= pygame.font.Font('src/data/Pixeled.ttf', TAMANNO_LETRA_GRANDE)
    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-90) , (ANCHO, ALTO-90), 5)

    #muestra lo que escribe el jugador
    screen.blit(font.render(palabraUsuario, 1, COLOR_TEXTO), (ANCHO//2-len(palabraUsuario)*TAMANNO_LETRA//2,520))
    #muestra el puntaje
    screen.blit(font.render("SCORE: " + str(puntos), 1, COLOR_TEXTO), (660, 5))
    #screen.blit(font.render('HIGHSCORE: ' + str(puntaje_mas_alto),1,COLOR_TEXTO), (630,25))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos < 15):
        ren = font.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = font.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (5, 5))
    #muestra la palabra
    screen.blit(font2.render(palabraActual.upper(),1,Green), (ANCHO//2 -len(palabraActual)*TAMANNO_LETRA_GRANDE//2, ALTO-400))
    screen.blit(font.render(palabraAnterior.upper(),1,Pink), (ANCHO//2 -len(palabraAnterior)*TAMANNO_LETRA//2, ALTO-200))




# Variables para la funcion
color_speed = 5
color_direction= [-1,1,-1]
color_direction2= [0,1,0]
default_color= [220,140,100]
default_color2= [0,255,255]
minimum=0
maximum=255



def color_change(color,direction):
    for i in range(3):
        color[i]+= color_speed * direction[i]
        if color[i]>=maximum or color[i]<= minimum:
            direction[i] *= -1




# TRANSICION DE ESCENAS --------------------------------

def fade(ANCHO, ALTO):
    fade = pygame.Surface((ANCHO, ALTO))
    dt = gameClock.tick(60)/1000
    fade.fill((COLOR_FONDO))
    for alpha in range(0,300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)



# FUNCION ANIMACION START SCREEN --------------------------
def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)

# FUNCION QUE HACE UN COUNTDOWN PARA TRANSICION ENTRE ESCENAS --------------------------
def count_down():

    Count_down = True
    countdown = 3
    last_count = pygame.time.get_ticks()

    # mientras sea true
    while Count_down:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()


        # cuando el contador llegue a 0, valor= False, sale de esta escena
        if countdown == 0:
            Count_down = False


        # dibujo el contador, y voy reduciendo su valor
        else:
            screen.fill((0,0,0))
            Contador = font.render('EMPEZANDO...', True, (255,255,255))

            screen.blit(Contador,(ANCHO//2-Contador.get_width()/2,200))
            Contador1 = font.render(str(countdown), True,(255,255,255))
            screen.blit(Contador1,(ANCHO/2-Contador1.get_width()/2,250))
            count_timer = pygame.time.get_ticks()
            if count_timer-last_count > 1000:
                countdown-=1
                last_count=count_timer
                pygame.display.flip()
        pygame.display.update()