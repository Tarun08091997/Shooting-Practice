### this file will create a pygame window for one dimention shooting perpose



import sys

import pygame
from sprites_involved import *
from end_part import *

from tkinter.messagebox import askyesno


pygame.init()


class Easy:


    def __init__(self,crosshair_type):
        pygame.init()
        con.crosshair_type = crosshair_type
        screen = pygame.display.set_mode((con.screen_Width, con.screen_Height))
        pygame.display.set_caption("Shooting Practice")
        screen.blit(con.Bg,(0,0))
        pygame.mouse.set_visible(False)
        end = ending_frame(screen)




        ### Define cursor##########################
        aim = aim_cursor(crosshair_type)
        cursor_group = pygame.sprite.Group()
        cursor_group.add(aim)

        ### define target############################
        target = Target(con.Target1)
        target_gp = pygame.sprite.Group()
        target_gp.add(target)





        clock = pygame.time.Clock()
        con.minute = 0
        con.seconds = 0
        ################################## Starting Screen ############################
        starting_scene = True
        while(starting_scene):
            screen.blit(con.easy_start,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    starting_scene = False
            pass






        ############################################loop ####################################
        running = True
        while(running):

            clock.tick(con.FPS)
            screen.blit(con.Bg,(0,0))
            con.seconds += (1/con.FPS)
            if con.seconds >= 60:
                con.minute += 1
                con.seconds = 0
                con.points -= 1

            con.time_txt = con.bold_font.render(str(con.minute) + ":" + str(int(con.seconds)), True, (255, 255, 255))
            con.Remainingcountnumber_txt = con.bold_font.render(str(int(con.no_of_targets) - con.target_no_variable), True, (0, 255, 0))
            con.countnumber_txt = con.bold_font.render(str(con.Count), True, (200, 255, 100))
            con.misscountnumber_txt = con.bold_font.render(str(con.miss_count), True, (255, 255, 0))
            con.missshotnumber_txt = con.bold_font.render(str(con.miss_shoot), True, (255, 0, 0))

            screen.blit(con.count_txt, (10, 10))
            screen.blit(con.Remainingcountnumber_txt,(130,7))
            screen.blit(con.misscount_txt,(1150,10))
            screen.blit(con.misscountnumber_txt, (1250, 7))
            screen.blit(con.missshot_txt, (300, 10))
            screen.blit(con.missshotnumber_txt, (390, 7))
            screen.blit(con.time_txt, (800, 10))






           ### define target
            """ This code checks if target apperence exceeds the limit_time or user hit the targe
                if it id either of then then create a new Target else just show the Target
                
                if user hit the target in time limit than inc Hit count, decrease the time limit to a minimum
                extent slowly.
                else increase the miss count
                
                hit +5 , missshoot -1, misstarget -2, min inc -3 points
            
            
            """
            if con.Target_timer >= con.Target_maxtimer or aim.is_collision():
                target = Target(con.Target1)
                target_gp = pygame.sprite.Group()
                target_gp.add(target)
                con.Target_timer = 0
                con.target_no_variable += 1

                if aim.is_collision():
                   con.Count += 1
                   con.points += 5
                   if con.Target_maxtimer > con.Target_mintimer :
                      con.Target_maxtimer -= .5
                   elif con.Target_maxtimer > 15:
                      con.Target_maxtimer -= .1
                else:
                    con.miss_count += 1
                    con.points -= 3
                aim.list = []
            else:
                target.show()
                target_gp.draw(screen)
                con.Target_timer += 1


            #### update cross hair#############################################
            x,y = pygame.mouse.get_pos()
            aim.update(x,y)
            cursor_group.draw(screen)
           ############################Win sign#############################
            """
            player complete the game when he complete 100 shots and reult will be shown on a rec
            with play again sign
            time ele[psed
            sot miss
            target miss
            """

            pygame.display.update()


           ######## controls############################################################

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        aim.shoot(target_gp)
                        if not aim.is_collision():
                            con.miss_shoot += 1
                            con.points -= 1

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_TAB:
                        if crosshair_type < 11 :
                            crosshair_type += 1
                        else:
                            crosshair_type = 0
                         ### redefine aim cursor
                        aim = aim_cursor(crosshair_type)
                        cursor_group = pygame.sprite.Group()
                        cursor_group.add(aim)

                    if event.key == pygame.K_ESCAPE:
                        answer = askyesno(message="Are you sure you want to Exit ???")
                        if answer:
                            con.reset()
                            con.no_of_targets = con.datalist[3]
                            con.target_no_variable = 0
                            con.minute = 0
                            con.seconds = 0
                            pygame.display.quit()
                            running = False








            ###########ENding Game#################################
            if con.points <= 0 or con.target_no_variable >= int(con.no_of_targets) :
                running = False
                end_running = True
                while end_running:

                    end.easy_end(1)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            self.running = False
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                end_running = False
                                con.reset()
                                con.target_no_variable = 0
                                con.no_of_targets = con.datalist[3]
                                con.minute = 0
                                con.seconds = 0
                                Easy(con.crosshair_type)

                            if event.key == pygame.K_ESCAPE:

                                ########### to reinitialize pygame as pygame.quit will have some pb with
                                ## fonts so u may use pygame.display.quit but you will come back on the same screen
                                answer = askyesno(message="Are you sure you want to Exit ???")
                                if answer:
                                      pygame.display.quit()
                                      con.reset()
                                      con.no_of_targets = con.datalist[3]
                                      con.target_no_variable = 0
                                      con.minute = 0
                                      con.seconds = 0
                                      self.running = False
                                      end_running = False




                pass

    pass
