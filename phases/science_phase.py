import pygame
from lib import heroes, items
from grid import *
from key_events import KeyEvents

#vidas
#vida8
vida8 = pygame.image.load("Image/vidas/8.png")
vida8_rect = vida8.get_rect()
vida8_rect.center = (2.5 * TILESIZE, 0.50 * TILESIZE)

#vida7
vida7 = pygame.image.load("Image/vidas/7.png")
vida7_rect = vida7.get_rect()
vida7_rect.center = (2.5 * TILESIZE, 0.50 * TILESIZE)

#vida6
vida6 = pygame.image.load("Image/vidas/6.png")
vida6_rect = vida6.get_rect()
vida6_rect.center = (2.5 * TILESIZE, 0.50 * TILESIZE)

#vida5
vida5 = pygame.image.load("Image/vidas/5.png")
vida5_rect = vida5.get_rect()
vida5_rect.center = (2.5 * TILESIZE, 0.50 * TILESIZE)

#vida4
vida4 = pygame.image.load("Image/vidas/4.png")
vida4_rect = vida4.get_rect()
vida4_rect.center = (2.5 * TILESIZE, 0.50 * TILESIZE)

#vida3
vida3 = pygame.image.load("Image/vidas/3.png")
vida3_rect = vida3.get_rect()
vida3_rect.center = (2.5 * TILESIZE, 0.50 * TILESIZE)

#vida2
vida2 = pygame.image.load("Image/vidas/2.png")
vida2_rect = vida2.get_rect()
vida2_rect.center = (2.5 * TILESIZE, 0.50 * TILESIZE)

#vida1
vida1 = pygame.image.load("Image/vidas/1.png")
vida1_rect = vida1.get_rect()
vida1_rect.center = (2.5 * TILESIZE, 0.50 * TILESIZE)

#gameover
gameover = pygame.image.load("Image/vidas/gameover.png")
gameover_rect = gameover.get_rect()
gameover_rect.center = (10 * TILESIZE, 4.9 * TILESIZE)


#vocevenceu
vocevenceu = pygame.image.load("Image/vidas/vocevenceu.png")
vocevenceu_rect = gameover.get_rect()
vocevenceu_rect.center = (10 * TILESIZE, 4.9 * TILESIZE)

#personagens
enzo = pygame.image.load("Image/vidas/iconenzo.png")
enzo_rect = enzo.get_rect()
enzo_rect.center = (1 * TILESIZE, 0.50 * TILESIZE)

valentina = pygame.image.load("Image/vidas/iconvalentina.png")
valentina_rect = valentina.get_rect()
valentina_rect.center = (1 * TILESIZE, 0.50 * TILESIZE)

#portais

portal1 = pygame.image.load("sprites/textures/portal.png")
portal1_rect = portal1.get_rect()
portal1_rect.center = (2.5 * TILESIZE, 5 * TILESIZE)

portal2 = pygame.image.load("sprites/textures/portal.png")
portal2_rect = portal2.get_rect()
portal2_rect.center = (5 * TILESIZE, 2.6 * TILESIZE)

portal3 = pygame.image.load("sprites/textures/portal.png")
portal3_rect = portal3.get_rect()
portal3_rect.center = (7 * TILESIZE, 5 * TILESIZE)

portal4 = pygame.image.load("sprites/textures/portal.png")
portal4_rect = portal4.get_rect()
portal4_rect.center = (9.5 * TILESIZE, 3.6 * TILESIZE)

portal5 = pygame.image.load("sprites/textures/portal.png")
portal5_rect = portal5.get_rect()
portal5_rect.center = (11.5 * TILESIZE, 7.5 * TILESIZE)

portal6 = pygame.image.load("sprites/textures/portal.png")
portal6_rect = portal6.get_rect()
portal6_rect.center = (13.5 * TILESIZE, 5 * TILESIZE)

portal7 = pygame.image.load("sprites/textures/portal.png")
portal7_rect = portal7.get_rect()
portal7_rect.center = (16 * TILESIZE, 5 * TILESIZE)

portal8 = pygame.image.load("sprites/textures/portal.png")
portal8_rect = portal8.get_rect()
portal8_rect.center = (19 * TILESIZE, 5 * TILESIZE)

#Perguntas
pergunta_fechar = pygame.image.load("perguntas/pergunta1/x.png")
pergunta_fundo = pygame.image.load("perguntas/pergunta8/fundo.png")


pergunta1_fundo = pygame.image.load("perguntas/pergunta1/fundo.png")
resposta1a_fundo = pygame.image.load("perguntas/pergunta1/a.png")
resposta1b_fundo = pygame.image.load("perguntas/pergunta1/b.png")
resposta1c_fundo = pygame.image.load("perguntas/pergunta1/c.png")
resposta1d_fundo = pygame.image.load("perguntas/pergunta1/d.png")

#2
pergunta2_fundo = pygame.image.load("perguntas/pergunta2/fundo.png")
resposta2a_fundo = pygame.image.load("perguntas/pergunta2/a.png")
resposta2b_fundo = pygame.image.load("perguntas/pergunta2/b.png")
resposta2c_fundo = pygame.image.load("perguntas/pergunta2/c.png")
resposta2d_fundo = pygame.image.load("perguntas/pergunta2/d.png")

#3
pergunta3_fundo = pygame.image.load("perguntas/pergunta3/fundo.png")
resposta3a_fundo = pygame.image.load("perguntas/pergunta3/a.png")
resposta3b_fundo = pygame.image.load("perguntas/pergunta3/b.png")
resposta3c_fundo = pygame.image.load("perguntas/pergunta3/c.png")
resposta3d_fundo = pygame.image.load("perguntas/pergunta3/d.png")

#4
pergunta4_fundo = pygame.image.load("perguntas/pergunta4/fundo.png")
resposta4a_fundo = pygame.image.load("perguntas/pergunta4/a.png")
resposta4b_fundo = pygame.image.load("perguntas/pergunta4/b.png")
resposta4c_fundo = pygame.image.load("perguntas/pergunta4/c.png")
resposta4d_fundo = pygame.image.load("perguntas/pergunta4/d.png")

#5
pergunta5_fundo = pygame.image.load("perguntas/pergunta5/fundo.png")
resposta5a_fundo = pygame.image.load("perguntas/pergunta5/a.png")
resposta5b_fundo = pygame.image.load("perguntas/pergunta5/b.png")
resposta5c_fundo = pygame.image.load("perguntas/pergunta5/c.png")
resposta5d_fundo = pygame.image.load("perguntas/pergunta5/d.png")

#6 
pergunta6_fundo = pygame.image.load("perguntas/pergunta6/fundo.png")
resposta6a_fundo = pygame.image.load("perguntas/pergunta6/a.png")
resposta6b_fundo = pygame.image.load("perguntas/pergunta6/b.png")
resposta6c_fundo = pygame.image.load("perguntas/pergunta6/c.png")
resposta6d_fundo = pygame.image.load("perguntas/pergunta6/d.png")

#7 
pergunta7_fundo = pygame.image.load("perguntas/pergunta7/fundo.png")
resposta7a_fundo = pygame.image.load("perguntas/pergunta7/a.png")
resposta7b_fundo = pygame.image.load("perguntas/pergunta7/b.png")
resposta7c_fundo = pygame.image.load("perguntas/pergunta7/c.png")
resposta7d_fundo = pygame.image.load("perguntas/pergunta7/d.png")

#8 
pergunta8_fundo = pygame.image.load("perguntas/pergunta8/fundo.png")
resposta8a_fundo = pygame.image.load("perguntas/pergunta8/a.png")
resposta8b_fundo = pygame.image.load("perguntas/pergunta8/b.png")
resposta8c_fundo = pygame.image.load("perguntas/pergunta8/c.png")
resposta8d_fundo = pygame.image.load("perguntas/pergunta8/d.png")

class SciencePhase():

    def __init__(self, hp, escolhido):
        self.hp = hp
        self.game_over = False
        self.game_win = False

        self.question_dictionary = {
            "its_on_a_question": False,
            "questions": {
                1: False,
                2: False,
                3: False,
                4: False,
                5: False,
                6: False,
                7: False,
                8: False,
            }
        }

        def update_questions(action, question, answer):
            if action == "open":
                self.question_dictionary["its_on_a_question"] = True

            elif action == "answered":
                self.question_dictionary["questions"].update({question: True})
                count = 0
                if not answer:
                    print("Resposta incorreta")
                    self.hp -= 1
                    if self.hp == 0:
                        game_end("game_over")

                else:
                    print("Resposta correta")
                for index in self.question_dictionary["questions"]:
                    if not self.question_dictionary["questions"][index]:
                        count += 1
                if count == 0:
                    game_end("game_win")

                self.question_dictionary["its_on_a_question"] = False

        def game_end(type):
            if type == "game_over":
                print("Game Over")
                self.game_over = True
                pygame.mixer.music.load('Menu/music/perdeu.mp3')
                pygame.mixer.music.play(-1)
            else:
                print("Você Venceu!")
                self.game_win = True
                pygame.mixer.music.load('Menu/music/ganhou.mp3')
                pygame.mixer.music.play(-1)

        ## Instanciandos as dependencias dos objetos
        if escolhido == "enzo":
            PLAYER = heroes.ENZO()
        else:
            PLAYER = heroes.VALENTINA()
        key_events = KeyEvents(PLAYER, escolhido)

        GAME_OVER = False

        # Início do loop do jogo
        while not GAME_OVER:
            
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                key_events.global_events()

                if (keys[pygame.K_ESCAPE]):
                    key_events.quit()

                # Condição das movimentações dos personagens
                if (keys[pygame.K_w]) and PLAYER.PLAYER_POS[1] > 0 and self.question_dictionary["its_on_a_question"] == False:
                    key_events.key_up()
                elif (keys[pygame.K_d]) and PLAYER.PLAYER_POS[0] < MAPWIDTH - 1 and self.question_dictionary["its_on_a_question"] == False:
                    key_events.key_right()
                elif (keys[pygame.K_s]) and PLAYER.PLAYER_POS[1] < MAPHEIGHT - 1 and self.question_dictionary["its_on_a_question"] == False:
                    key_events.key_down()
                elif (keys[pygame.K_a]) and PLAYER.PLAYER_POS[0] > 0 and self.question_dictionary["its_on_a_question"] == False:
                    key_events.key_left()

            # Renderização do Mapa
            for row in range(MAPHEIGHT):
                for column in range(MAPWIDTH):
                    DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))

            if not self.question_dictionary["questions"][1]:
                portal1_screen = DISPLAYSURFACE.blit(portal1, portal1_rect)
            if not self.question_dictionary["questions"][2]:
                portal2_screen = DISPLAYSURFACE.blit(portal2, portal2_rect)
            if not self.question_dictionary["questions"][3]:
                portal3_screen = DISPLAYSURFACE.blit(portal3, portal3_rect)
            if not self.question_dictionary["questions"][4]:
                portal4_screen = DISPLAYSURFACE.blit(portal4, portal4_rect)
            if not self.question_dictionary["questions"][5]:
                portal5_screen = DISPLAYSURFACE.blit(portal5, portal5_rect)
            if not self.question_dictionary["questions"][6]:
                portal6_screen = DISPLAYSURFACE.blit(portal6, portal6_rect)
            if not self.question_dictionary["questions"][7]:
                portal7_screen = DISPLAYSURFACE.blit(portal7, portal7_rect)
            if not self.question_dictionary["questions"][8]:
                portal8_screen = DISPLAYSURFACE.blit(portal8, portal8_rect)

            # Renderização do personagem
            player = DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))

            #Renderização de vidas
            if self.hp == 8:
                DISPLAYSURFACE.blit(vida8, vida8_rect)
            elif self.hp == 7:
                DISPLAYSURFACE.blit(vida7, vida7_rect)
            elif self.hp == 6:
                DISPLAYSURFACE.blit(vida6, vida6_rect)
            elif self.hp == 5:
                DISPLAYSURFACE.blit(vida5, vida5_rect)
            elif self.hp == 4:
                DISPLAYSURFACE.blit(vida4, vida4_rect)
            elif self.hp == 3:
                DISPLAYSURFACE.blit(vida3, vida3_rect)
            elif self.hp == 2:
                DISPLAYSURFACE.blit(vida2, vida2_rect)
            elif self.hp == 1:
                DISPLAYSURFACE.blit(vida1, vida1_rect)

            #Icons
            if escolhido == "enzo":
                DISPLAYSURFACE.blit(enzo, enzo_rect)
            else:
                DISPLAYSURFACE.blit(valentina, valentina_rect)

            #GameEnd
            if self.game_over:
                DISPLAYSURFACE.blit(gameover, gameover_rect)
                mouse = pygame.mouse.get_pos()
                #print(mouse)
                # if 1000 + 121 > mouse[0] > 900 and 35 + 122 > mouse[1] > 35:
                #     if pygame.mouse.get_pressed()[0]:
                #         quit()

            elif self.game_win:
                DISPLAYSURFACE.blit(vocevenceu, vocevenceu_rect)

            else:
                # Questão 1
                if self.question_dictionary["questions"][1] == False:
                    if player.colliderect(portal1_screen):
                        update_questions("open", False, False)

                        DISPLAYSURFACE.blit(pergunta1_fundo,(180,0))
                        DISPLAYSURFACE.blit(resposta1a_fundo,(365,310))
                        DISPLAYSURFACE.blit(resposta1b_fundo,(365,375))
                        DISPLAYSURFACE.blit(resposta1c_fundo,(365,440))
                        DISPLAYSURFACE.blit(resposta1d_fundo,(365,505))
                        DISPLAYSURFACE.blit(pergunta_fechar,(1130,10))
                        mouse = pygame.mouse.get_pos()

                        if 365+566>mouse[0]>365 and 310+57>mouse[1]>310:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 1, True)
                                for row in range(MAPHEIGHT):
                                    for column in range(MAPWIDTH):
                                        DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))

                            DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))
                        elif 365+566>mouse[0]>365 and 375+57>mouse[1]>375:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 1, False)
                        elif 365+566>mouse[0]>365 and 440+57>mouse[1]>440:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 1, False)
                        elif 365+566>mouse[0]>365 and 505+57>mouse[1]>505:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 1, False)

                # Questão 2
                if self.question_dictionary["questions"][2] == False:
                    if player.colliderect(portal2_screen):
                        update_questions("open", False, False)
                        DISPLAYSURFACE.blit(pergunta2_fundo, (180, 0))
                        DISPLAYSURFACE.blit(resposta2a_fundo, (365, 310))
                        DISPLAYSURFACE.blit(resposta2b_fundo, (365, 375))
                        DISPLAYSURFACE.blit(resposta2c_fundo, (365, 440))
                        DISPLAYSURFACE.blit(resposta2d_fundo, (365, 505))
                        DISPLAYSURFACE.blit(pergunta_fechar, (1130, 10))
                        mouse = pygame.mouse.get_pos()

                        if 365 + 566 > mouse[0] > 365 and 310 + 57 > mouse[1] > 310:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 2, False)
                        elif 365 + 566 > mouse[0] > 365 and 375 + 57 > mouse[1] > 375:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 2, False)
                        elif 365 + 566 > mouse[0] > 365 and 440 + 57 > mouse[1] > 440:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 2, False)
                        elif 365 + 566 > mouse[0] > 365 and 505 + 57 > mouse[1] > 505:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 2, True)

                # Questão 3
                if self.question_dictionary["questions"][3] == False:
                    if player.colliderect(portal3_screen):
                        update_questions("open", False, False)

                        DISPLAYSURFACE.blit(pergunta3_fundo,(180,0))
                        DISPLAYSURFACE.blit(resposta3a_fundo,(365,310))
                        DISPLAYSURFACE.blit(resposta3b_fundo,(365,375))
                        DISPLAYSURFACE.blit(resposta3c_fundo,(365,440))
                        DISPLAYSURFACE.blit(resposta3d_fundo,(365,505))
                        DISPLAYSURFACE.blit(pergunta_fechar,(1130,10))
                        mouse = pygame.mouse.get_pos()

                        if 365+566>mouse[0]>365 and 310+57>mouse[1]>310:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 3, False)
                        elif 365+566>mouse[0]>365 and 375+57>mouse[1]>375:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 3, True)
                        elif 365+566>mouse[0]>365 and 440+57>mouse[1]>440:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 3, False)
                        elif 365+566>mouse[0]>365 and 505+57>mouse[1]>505:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 3, False)

                # Questão 4
                if self.question_dictionary["questions"][4] == False:
                    if player.colliderect(portal4_screen):
                        update_questions("open", False, False)
                        DISPLAYSURFACE.blit(pergunta4_fundo,(180,0))
                        DISPLAYSURFACE.blit(resposta4a_fundo,(365,310))
                        DISPLAYSURFACE.blit(resposta4b_fundo,(365,375))
                        DISPLAYSURFACE.blit(resposta4c_fundo,(365,440))
                        DISPLAYSURFACE.blit(resposta4d_fundo,(365,505))
                        DISPLAYSURFACE.blit(pergunta_fechar,(1130,10))
                        mouse = pygame.mouse.get_pos()

                        if 365+566>mouse[0]>365 and 310+57>mouse[1]>310:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 4, False)
                        elif 365+566>mouse[0]>365 and 375+57>mouse[1]>375:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 4, True)
                        elif 365+566>mouse[0]>365 and 440+57>mouse[1]>440:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 4, False)
                        elif 365+566>mouse[0]>365 and 505+57>mouse[1]>505:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 4, False)

                # Questão 5
                if self.question_dictionary["questions"][5] == False:
                    if player.colliderect(portal5_screen):
                        update_questions("open", False, False)
                        DISPLAYSURFACE.blit(pergunta5_fundo,(180,0))
                        DISPLAYSURFACE.blit(resposta5a_fundo,(365,310))
                        DISPLAYSURFACE.blit(resposta5b_fundo,(365,375))
                        DISPLAYSURFACE.blit(resposta5c_fundo,(365,440))
                        DISPLAYSURFACE.blit(resposta5d_fundo,(365,505))
                        DISPLAYSURFACE.blit(pergunta_fechar,(1130,10))
                        mouse = pygame.mouse.get_pos()

                        if 365+566>mouse[0]>365 and 310+57>mouse[1]>310:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 5, False)
                        elif 365+566>mouse[0]>365 and 375+57>mouse[1]>375:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 5, False)
                        elif 365+566>mouse[0]>365 and 440+57>mouse[1]>440:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 5, False)
                        elif 365+566>mouse[0]>365 and 505+57>mouse[1]>505:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 5, True)

                # Questão 6
                if self.question_dictionary["questions"][6] == False:
                    if player.colliderect(portal6_screen):
                        update_questions("open", False, False)
                        DISPLAYSURFACE.blit(pergunta6_fundo,(180,0))
                        DISPLAYSURFACE.blit(resposta6a_fundo,(365,310))
                        DISPLAYSURFACE.blit(resposta6b_fundo,(365,375))
                        DISPLAYSURFACE.blit(resposta6c_fundo,(365,440))
                        DISPLAYSURFACE.blit(resposta6d_fundo,(365,505))
                        DISPLAYSURFACE.blit(pergunta_fechar,(1130,10))
                        mouse = pygame.mouse.get_pos()

                        if 365+566>mouse[0]>365 and 310+57>mouse[1]>310:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 6, False)
                        elif 365+566>mouse[0]>365 and 375+57>mouse[1]>375:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 6, False)
                        elif 365+566>mouse[0]>365 and 440+57>mouse[1]>440:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 6, False)
                        elif 365+566>mouse[0]>365 and 505+57>mouse[1]>505:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 6, True)

                #Questão 7
                if self.question_dictionary["questions"][7] == False:
                    if player.colliderect(portal7_screen):
                        update_questions("open", False, False)
                        DISPLAYSURFACE.blit(pergunta7_fundo,(180,0))
                        DISPLAYSURFACE.blit(resposta7a_fundo,(365,310))
                        DISPLAYSURFACE.blit(resposta7b_fundo,(365,375))
                        DISPLAYSURFACE.blit(resposta7c_fundo,(365,440))
                        DISPLAYSURFACE.blit(resposta7d_fundo,(365,505))
                        DISPLAYSURFACE.blit(pergunta_fechar,(1130,10))
                        mouse = pygame.mouse.get_pos()

                        if 365+566>mouse[0]>365 and 310+57>mouse[1]>310:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 7, False)
                        elif 365+566>mouse[0]>365 and 375+57>mouse[1]>375:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 7, False)
                        elif 365+566>mouse[0]>365 and 440+57>mouse[1]>440:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 7, True)
                        elif 365+566>mouse[0]>365 and 505+57>mouse[1]>505:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 7, False)

                #Questão 8
                if self.question_dictionary["questions"][8] == False:
                    if player.colliderect(portal8_screen):
                        update_questions("open", False, False)
                        DISPLAYSURFACE.blit(pergunta8_fundo,(180,0))
                        DISPLAYSURFACE.blit(resposta8a_fundo,(365,310))
                        DISPLAYSURFACE.blit(resposta8b_fundo,(365,375))
                        DISPLAYSURFACE.blit(resposta8c_fundo,(365,440))
                        DISPLAYSURFACE.blit(resposta8d_fundo,(365,505))
                        DISPLAYSURFACE.blit(pergunta_fechar,(1130,10))
                        mouse = pygame.mouse.get_pos()

                        if 365+566>mouse[0]>365 and 310+57>mouse[1]>310:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 8, True)
                        elif 365+566>mouse[0]>365 and 375+57>mouse[1]>375:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 8, False)
                        elif 365+566>mouse[0]>365 and 440+57>mouse[1]>440:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 8, False)
                        elif 365+566>mouse[0]>365 and 505+57>mouse[1]>505:
                            if pygame.mouse.get_pressed()[0]:
                                update_questions("answered", 8, False)

            # Update do jogo
            
            pygame.display.update()
        # Final do loop do jogo
