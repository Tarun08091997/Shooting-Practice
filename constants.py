import os
import sys

import pygame
from tkinter import PhotoImage
pygame.init()




class constant:
    ## from main window settings

    crosshair_type = 0
    game_type = 1

    ending_frame = pygame.image.load(os.path.join('Files/Images','ending_frame.png'))

    cursor_List = [pygame.image.load(os.path.join('Files/Images','black_crosshair.png')),
                   pygame.image.load(os.path.join('Files/Images','aim3.png')),
                   pygame.image.load(os.path.join('Files/Images','black_sevecrosshair.png')),
                   pygame.image.load(os.path.join('Files/Images','blue_cursor.png')),
                   pygame.image.load(os.path.join('Files/Images','blue_holowcrosshair.png')),
                   pygame.image.load(os.path.join('Files/Images','blueCirculer_crosshair.png')),
                   pygame.image.load(os.path.join('Files/Images','bold_crosshair.png')),
                   pygame.image.load(os.path.join('Files/Images','circuler_holowcrosshair.png')),
                   pygame.image.load(os.path.join('Files/Images','cirulerblack_crosshair.png')),
                   pygame.image.load(os.path.join('Files/Images','dark_sievecrosshair.png')),
                   pygame.image.load(os.path.join('Files/Images','red_crosshair.png')),
                   pygame.image.load(os.path.join('Files/Images','red_hollowcrosshair.png'))
                   ]

    ### 0 to 11
    img_path = ['Files/Images/black_crosshair.png', 'Files/Images/aim3.png', 'Files/Images/black_sevecrosshair.png',
                'Files/Images/blue_cursor.png', 'Files/Images/blue_holowcrosshair.png',
                'Files/Images/blueCirculer_crosshair.png',
                'Files/Images/bold_crosshair.png', 'Files/Images/circuler_holowcrosshair.png',
                'Files/Images/cirulerblack_crosshair.png',
                'Files/Images/dark_sievecrosshair.png', 'Files/Images/red_crosshair.png',
                'Files/Images/red_hollowcrosshair.png'
                ]

    Target1 = pygame.image.load(os.path.join('Files/Images','target.png'))
    Target2 = pygame.image.load(os.path.join('Files/Images','target_2.png'))
    Bg = pygame.image.load(os.path.join('Files/Images','BackGround.jpg'))
    easy_start = pygame.image.load(os.path.join('Files/Images', 'easy_start.png'))
    medium_start = pygame.image.load(os.path.join('Files/Images', 'medium_start.png'))



    gun_sound = pygame.mixer.Sound(os.path.join('Files/Sounds','gun_sound.wav'))
    click_sound = pygame.mixer.Sound(os.path.join('Files/Sounds','Mouse_Click.wav'))




    FPS = 60
    screen_Width = 1366
    screen_Height = 767
    Target_maxtimer = 65
    Target_mintimer = 20
    Target_maxtimer_hard = 55
    Target_mintimer_hard = 15
    Target_timer = 0
    Count = 0
    miss_count = 0
    miss_shoot =0
    points = 10
    add_point = False

    def reset(self):
        self.Target_maxtimer = 65
        self.Target_mintimer = 20
        self.Target_maxtimer_hard = 30
        self.Target_mintimer_hard = 10
        self.Target_timer = 0
        self.Count = 0
        self.miss_count = 0
        self.miss_shoot = 0
        self.points = 10
        self.target_no_variable = 0


    font = pygame.font.SysFont('arial', 20)
    bold_font = pygame.font.SysFont('arial', 25,True)

    #############################txt initialize####################################
    count_txt = font.render("Remaining Hit:", True, (255, 255, 255))
    misscount_txt = font.render("Miss Count:", True, (255, 255, 255))
    missshot_txt = font.render("Miss Shot:", True, (255, 255, 255))



    time_txt = None
    Remainingcountnumber_txt = None
    countnumber_txt = None
    misscountnumber_txt = None
    missshotnumber_txt = None

    minute = 0
    seconds = 0
    start_time = 0


    no_of_targets = 5        ###### no of max target spawned

    target_no_variable = 0   ########## no of target spawned
    highscore = False

    datalist = []


