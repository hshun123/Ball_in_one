import pygame
import pymunk
import components.ball as ball
from stage.stage import Stage
import components.walls as walls
import components.goal as goal
import components.obstacles as obstacles
import components.colors as colors

class Stage_02(Stage):
    def __init__(self, space, screen):

        super().__init__(space, screen)
        # obsticles
        self.ob = obstacles.Obsticle(550.0, 760, 70, 490, 0, 5)
        space.add(self.ob.body, self.ob.shape)

        self.ob2 = obstacles.Obsticle(800.0, 250.0, 70, 490, 0, 5)
        space.add(self.ob2.body, self.ob2.shape)

        # images
        self.ob_img = pygame.image.load("images/block_slim_long.png")

        self.scaled_img = pygame.transform.scale(self.ob_img, (70, 460))

        self.scaled_img_2 = pygame.transform.scale(self.ob_img, (70,490))

        # show the goal
        goal_y = 800 - self.bottom_img.get_height() * 0.5 - 15
        self.goal_1 = goal.Goal(screen, 1300.0, goal_y, 4, 15)
        # self.goal_1 = goal.Goal(1300.0, 760.0, 4, 15)
        space.add(self.goal_1.body, self.goal_1.shape)

        self.goal_img = pygame.image.load(r'images/star.png')

    def update(self, screen):
        rec = self.scaled_img.get_rect(center = (550, 760))
        screen.blit(self.scaled_img, rec)
        rec_2 = self.scaled_img_2.get_rect(center = (800.0, 250))
        screen.blit(self.scaled_img_2, rec_2)
        # pygame.draw.circle(screen, colors.RED, (self.goal_1.body.position[0], self.goal_1.body.position[1]), 15)
         # goal image
        scaled_goal = pygame.transform.scale(self.goal_img, (30, 30))
        goal_rec = scaled_goal.get_rect(center = self.goal_1.body.position)
        screen.blit(scaled_goal, goal_rec)