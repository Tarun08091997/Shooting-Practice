import pygame
from constants import *
from Database import *
pygame.init()



class ending_frame:
    pygame.init()
    def __init__(self,screen):
        self.screen = screen

        pass
    def draw(self):
        self.screen.blit(con.ending_frame, (300, 200))
        self.screen.blit(con.countnumber_txt, (490, 263))
        self.screen.blit(con.time_txt, (480, 305))
        self.screen.blit(con.missshotnumber_txt, (490, 340))
        self.screen.blit(con.misscountnumber_txt, (490, 385))


    def draw_Easy(self,hit_points,time_points,shotmiss_point,targetmiss_point):
        self.hit_points = hit_points
        hitpoint_txt = con.bold_font.render("+"+str(con.Count*hit_points),True,(0,255,0))
        timepoint_txt = con.bold_font.render("-"+str(con.minute*time_points),True,(255,0,0))
        shotmisspoint_txt = con.bold_font.render("-"+str(con.miss_shoot*shotmiss_point),True,(255,0,0))
        targetmisspoint_txt = con.bold_font.render("-"+str(con.miss_count*targetmiss_point),True,(255,0,0))

        totalPoints_txt = con.bold_font.render(str(con.points),True,(255,255,255))

        self.screen.blit(hitpoint_txt,(670,263))
        self.screen.blit(timepoint_txt,(670,305))
        self.screen.blit(shotmisspoint_txt,(670,340))
        self.screen.blit(targetmisspoint_txt,(670,385))
        self.screen.blit(totalPoints_txt,(680,440))





    def easy_end(self,game_type):

        """hit + 5, missshoot - 1, misstarget - 2, minute inc - 3 points"""
        self.draw()
        self.draw_Easy(5,3,1,2)
        check_data(con.Count, con.minute + con.seconds/100, game_type)
        ############# print HighScore
        datalist = load_data()
        data = {}
        if game_type == 1:
            data = datalist[0]
        elif game_type == 2:
            data = datalist[1]
        elif game_type == 3:
            data = datalist[2]

        points = int(data['highscore']) * self.hit_points
        time =   '{:.2f}'.format(float(data['time']))

        hitpoint_txt = con.bold_font.render(str(points), True, (0, 255, 0))
        time_txt = con.bold_font.render(str(time), True, (255, 0, 0))

        self.screen.blit(hitpoint_txt, (890, 263))
        self.screen.blit(time_txt, (890, 305))

        pygame.display.update()

    pass