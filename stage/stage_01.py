import pygame
import pymunk
import components.ball as ball
from stage.stage import Stage
import components.walls as walls
import components.goal as goal
import components.obstacles as obstacles
import components.colors as colors

class Stage_01(Stage):
    def __init__(self, space, screen):

        super().__init__(space, screen)
        # obsticles
        self.ob = obstacles.Obsticle(600.0, 560, 180, 410, 0, 5)
        space.add(self.ob.body, self.ob.shape)

        
        # images
        self.ob_img = pygame.image.load("images/block_large2.png")
        
        self.scaled_img = pygame.transform.scale(self.ob_img, (180, 410))

        # show the goal
        # pygame.draw.circle(screen, colors.RED, (goal_1.body.position[0], goal_1.body.position[1]), 15)
        goal_y = 800 - self.bottom_img.get_height() * 0.5 - 15
        self.goal_1 = goal.Goal(screen,1300.0, goal_y, 4, 15)
        space.add(self.goal_1.body, self.goal_1.shape)

        self.goal_img = pygame.image.load(r'images/star.png')


    def update(self, screen):
        rec = self.scaled_img.get_rect(center = (600, 560))
        screen.blit(self.scaled_img, rec)
        
        # pygame.draw.circle(screen, colors.RED, (self.goal_1.body.position[0], self.goal_1.body.position[1]), 15)
        # goal image
        scaled_goal = pygame.transform.scale(self.goal_img, (30, 30))
        goal_rec = scaled_goal.get_rect(center = self.goal_1.body.position)
        screen.blit(scaled_goal, goal_rec)