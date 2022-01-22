import pygame
import pymunk
import components.ball as ball
from stage.stage import Stage
import components.walls as walls
import components.goal as goal
import components.obstacles as obstacles
import components.colors as colors

class Stage_04(Stage):
    def __init__(self, space, screen):

        super().__init__(space, screen)
        self.slim_width = 80
        self.slim_height = 512

        # obsticles
        self.ob = obstacles.Obsticle(550.0, 760, self.slim_width, self.slim_height, 0, 5)
        space.add(self.ob.body, self.ob.shape)

        self.ob2 = obstacles.Obsticle(550.0, 100.0, self.slim_width, self.slim_height, 0, 5)
        space.add(self.ob2.body, self.ob2.shape)

        self.ob3 = obstacles.Obsticle(1300.0, 800, self.slim_width, self.slim_height, 0, 5)
        space.add(self.ob3.body, self.ob3.shape)

        # images
        self.ob_img = pygame.image.load("images/block_slim_long.png")

       

        self.scaled_img = pygame.transform.scale(self.ob_img, (self.slim_width, self.slim_height))

        self.scaled_img_2 = pygame.transform.scale(self.ob_img, (self.slim_width,self.slim_height))

        self.scaled_img3 = pygame.transform.scale(self.ob_img, (self.slim_width, self.slim_height))
        # show the goal

        # # Goal
        self.goal_1 = goal.Goal(screen, 1300.0, 485.0, 4, 15)
        space.add(self.goal_1.body, self.goal_1.shape)

        self.goal_img = pygame.image.load(r'images/star.png')

        # obstacle


    def update(self, screen):
        rec = self.scaled_img.get_rect(center = (550, 760))
        screen.blit(self.scaled_img, rec)
        rec_2 = self.scaled_img_2.get_rect(center = (550.0, 100))
        screen.blit(self.scaled_img_2, rec_2)

        rec3 = self.scaled_img3.get_rect(center = (1300, 800))
        screen.blit(self.scaled_img3, rec3)
        # show the goal
        # pygame.draw.circle(screen, colors.RED, (self.goal_1.body.position[0], self.goal_1.body.position[1]), 15)
         # goal image
        scaled_goal = pygame.transform.scale(self.goal_img, (30, 30))
        goal_rec = scaled_goal.get_rect(center = self.goal_1.body.position)
        screen.blit(scaled_goal, goal_rec)