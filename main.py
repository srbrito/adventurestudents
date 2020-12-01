import pygame, sys, random, math
from pygame.locals import *
from grid import *

from imports import images

from phases import science_phase
DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

logo = pygame.image.load("Menu/logo.png")

playhover = pygame.image.load("Menu/playhover.png")
play = pygame.image.load("Menu/play.png")

fecharhover = pygame.image.load("Menu/fecharhover.png")
fechar = pygame.image.load("Menu/fechar.png")

fundo3 = pygame.image.load("Menu/fundo3.jpg")

som = pygame.image.load("Menu/som.png")
somhover = pygame.image.load("Menu/somhover.png")

cjogar = pygame.image.load("Menu/comojogar.png")
cjogarhover = pygame.image.load("Menu/comojogarhover.png")

# PERSONAGEM
fundo_perso = pygame.image.load("menu/fundo3.jpg")
logotela = pygame.image.load("Menu/logo2.png")
masc = pygame.image.load("menu/enzo.png")
maschover = pygame.image.load("menu/enzohover.png")
fem = pygame.image.load("menu/valentina.png")
femhover = pygame.image.load("menu/valentinahover.png")
nick = pygame.image.load("menu/nickgame.png")

pygame.mixer.music.load('Menu/music/fundo_jogo.mp3')
pygame.mixer.music.play(-1)

# COMOJOGAR

cjogar_sair = pygame.image.load("menu/fechar.png")
cjogar_sair_hover = pygame.image.load("menu/fecharhover.png")
cjogar_play = pygame.image.load("menu/play.png")
cjogar_play_hover = pygame.image.load("menu/playhover.png")
cjogar_fundo = pygame.image.load("menu/cjogar_fundo.png")


def comojogar():

    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 1000 + 121 > mouse[0] > 900 and 35 + 122 > mouse[1] > 35:
            DISPLAYSURFACE.blit(cjogar_sair, (1000, 35))
            if pygame.mouse.get_pressed()[0]:
                menu()

        else:
            DISPLAYSURFACE.blit(cjogar_sair_hover, (1000, 35))

        if 550 + 117 > mouse[0] > 550 and 450 + 119 > mouse[1] > 450:
            DISPLAYSURFACE.blit(cjogar_play, (550, 450))
            if pygame.mouse.get_pressed()[0]:
                perso()

        else:
            DISPLAYSURFACE.blit(cjogar_play_hover, (550, 450))

        if 330 + 121 > mouse[0] > 330 and 440 + 122 > mouse[1] > 440:
            DISPLAYSURFACE.blit(cjogar_fundo, (160, 0))
            if pygame.mouse.get_pressed()[0]:
                comojogar()

        else:
            DISPLAYSURFACE.blit(cjogar, (330, 440))

def menu():
    DISPLAYSURFACE.blit(fundo3, (0, 0))
    DISPLAYSURFACE.blit(logo, (200, 0))
    DISPLAYSURFACE.blit(play, (550, 400))
    DISPLAYSURFACE.blit(cjogar, (330, 440))
    DISPLAYSURFACE.blit(som, (1185, 50))
    DISPLAYSURFACE.blit(fechar, (810, 440))

    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 550 + 172 > mouse[0] > 550 and 400 + 168 > mouse[1] > 400:
            DISPLAYSURFACE.blit(playhover, (550, 400))
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.music.pause()
                perso()

        else:
            DISPLAYSURFACE.blit(play, (550, 400))

        if 810 + 117 > mouse[0] > 810 and 440 + 119 > mouse[1] > 440:
            DISPLAYSURFACE.blit(fecharhover, (810, 440))
            if pygame.mouse.get_pressed()[0]:
                quit()

        else:
            DISPLAYSURFACE.blit(fechar, (810, 440))

        if 330 + 121 > mouse[0] > 330 and 440 + 122 > mouse[1] > 440:
            DISPLAYSURFACE.blit(cjogarhover, (330, 440))
            if pygame.mouse.get_pressed()[0]:
                comojogar()


        else:
            DISPLAYSURFACE.blit(cjogar, (330, 440))

        if 1185 + 56 > mouse[0] > 1185 and 50 + 58 > mouse[1] > 50:
            DISPLAYSURFACE.blit(somhover, (1185, 50))
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.music.stop()
                DISPLAYSURFACE.blit(somhover, (1185, 50))
        else:
            DISPLAYSURFACE.blit(som, (1185, 50))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()

def perso():
    # IMAGENS
    DISPLAYSURFACE.blit(fundo_perso, (0, 0))
    DISPLAYSURFACE.blit(masc, (330, 360))
    DISPLAYSURFACE.blit(fem, (750, 360))
    DISPLAYSURFACE.blit(logotela, (200, 0))
    DISPLAYSURFACE.blit(nick, (290, 270))

    # nom()

    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():
        mouse = pygame.mouse.get_pos()

        if 340 + 166 > mouse[0] > 340 and 360 + 194 > mouse[1] > 360:
            if pygame.mouse.get_pressed()[0]:
                print('personagem masculino escolhido')
                nom("enzo")
        else:
            pass

        if 750 + 174 > mouse[0] > 750 and 360 + 194 > mouse[1] > 360:
            if pygame.mouse.get_pressed()[0]:
                print('personagem feminino escolhido')
                nom("valentina")
        else:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


font_name = pygame.font.match_font('berlin sans FB', True, True)


def text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def nom(escolhido):
    font_dig = pygame.font.Font(font_name, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(550, 280, 100, 35)
    color_inactive = pygame.Color(0, 200, 0, )
    color_active = pygame.Color(0, 150, 0)
    color = color_inactive
    active = False
    nome = ''
    done = False

    
    somhover = pygame.image.load("Menu/somhover.png")
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(nome)
                        nome = ''
                        hp = 8
                        science_phase.SciencePhase(hp, escolhido)
                    elif event.key == pygame.K_BACKSPACE:
                        nome = nome[:-1]
                    else:
                        nome += event.unicode

        # DISPLAYSURFACE.fill((30, 30, 30))
        # Render the current nome.
        txt_surface = font_dig.render(nome, True, color)
        # Resize the box if the nome is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the nome.
        DISPLAYSURFACE.blit(txt_surface, (input_box.x + 5, input_box.y))
        # Blit the input_box rect.
        pygame.draw.rect(DISPLAYSURFACE, color, input_box, 2)

        pygame.display.flip()

menu()
quit()