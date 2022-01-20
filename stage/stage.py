import pygame
import pymunk
import components.ball as ball
import components.walls as walls
import components.colors as colors
import components.func as fc
class Stage:
    def __init__(self, space, screen):
        # # ball 
        # self.main_ball = ball.Ball(40.0, 775.0, 1, 1)
        # space.add(self.main_ball.body, self.main_ball.shape)

        # background image load
        # self.background_img = pygame.image.load(r'/Users/hshun123/Documents/eric_gamejam/image/PNG/Background/bg_layer1.png')
        # bottom image
        self.bottom_img = pygame.image.load(r'images/bottom.png')

        # top image
        self.top_img= pygame.image.load(r'images/top.jpg')

        # screen walls
        wall_top = walls.Wall(0,50,1500,50, 2)
        space.add(wall_top.body, wall_top.shape)

        wall_right = walls.Wall(1500,0,1500,800, 2)
        # space.add(wall_right.body, wall_right.shape)

        self.wall_bottom = walls.Wall(0,800,1500,800, 12, self.bottom_img.get_height()*0.5)
        space.add(self.wall_bottom.body, self.wall_bottom.shape)

        self.wall_left = walls.Wall(0,0,0,800, 2, 10)
        space.add(self.wall_left.body, self.wall_left.shape)

        # sound
        # self.bgm = pygame.mixer.music.load('sound/BFL_Base_Games_BGM.wav')
        

    def updating(self, screen, trial, stage_num):

        # # draw the ball
        # pygame.draw.circle(screen, colors.ORANGE, (self.main_ball.body.position[0], self.main_ball.body.position[1]), 10)
        # background
        # screen.blit(self.background_img, (0, 0))

       
        
        # top line
        # pygame.draw.line(screen, colors.WHITE, [0,50],[1500,50] ,5)
        # bottom line
        pygame.draw.line(screen, colors.WHITE, [0,800],[1500,800] ,2)
        # left line
        pygame.draw.line(screen, colors.WHITE, [0,0],[0,800] ,2)

        # display score and stage number
            #Display the score and the number of lives at the top of the screen
        

    def late_updating(self, screen, trial, stage_num):
        # bottom image
        screen.blit(self.bottom_img,(-1, 800 - self.bottom_img.get_height() * 0.5))

        # top image
        screen.blit(self.top_img,(-1, -self.top_img.get_height()*0.5))

        # font = pygame.font.SysFont('Corbel', 34)
        ft = pygame.font.Font('font/fofbb_reg.ttf', 34)
        text_try = ft.render("Try: " + str(trial), 1, colors.WHITE)
        screen.blit(text_try, (40,30))
        text_stage = ft.render("Stage: " + str(stage_num), 1, colors.WHITE)
        screen.blit(text_stage, (650,30))

        text_reset = ft.render("Press Space Bar to ReLaunch", 1, colors.WHITE)
        screen.blit(text_reset, ( 950, 30))

        