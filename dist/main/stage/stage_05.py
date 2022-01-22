import math
import pygame
import pymunk
import components.ball as ball
from components.brick import Brick
from stage.stage import Stage
import components.walls as walls
import components.goal as goal
import components.obstacles as obstacles
import components.colors as colors

class Stage_05(Stage):
    def __init__(self, space, screen):

        super().__init__(space, screen)
        # obsticles
        self.ob = obstacles.Obsticle(800.0, 760, 140, 512, 0, 5)
        space.add(self.ob.body, self.ob.shape)

        # # bricks
        self.brick_1 = Brick(1000, 400, 64, 64,320, 3)
        space.add(self.brick_1.body, self.brick_1.shape)

        self.brick_2 = Brick(550, 250, 64, 64,50, 3)
        space.add(self.brick_2.body, self.brick_2.shape)

        # images
        self.ob_img = pygame.image.load("images/block_long.png")
        brick_1_img = pygame.image.load("images/block_corner.png")

        self.scaled_img = pygame.transform.scale(self.ob_img, (140, 512))

        # # brick 1
        self.rotated_brick = pygame.transform.rotate(brick_1_img, -math.degrees(self.brick_1.body.angle))
        

        self.rotated_brick2 = pygame.transform.rotate(brick_1_img, -math.degrees(self.brick_2.body.angle))
        

        # show the goal
       # pygame.draw.circle(screen, colors.RED, (goal_1.body.position[0], goal_1.body.position[1]), 15)
        # self.goal_1 = goal.Goal(1300.0, 760.0, 4, 15)
        # space.add(self.goal_1.body, self.goal_1.shape)
        # show the goal
        goal_y = 800 - self.bottom_img.get_height() * 0.5 - 15
        self.goal_1 = goal.Goal(screen, 1300.0, goal_y, 4, 15)
        # self.goal_1 = goal.Goal(1300.0, 760.0, 4, 15)
        space.add(self.goal_1.body, self.goal_1.shape)

        self.goal_img = pygame.image.load(r'images/star.png')
        # obstacle


    def update(self, screen):
        rec = self.scaled_img.get_rect(center = (800, 760))
        screen.blit(self.scaled_img, rec)

        # pygame.draw.circle(screen, colors.RED, (self.goal_1.body.position[0], self.goal_1.body.position[1]), 15)
         # goal image
        scaled_goal = pygame.transform.scale(self.goal_img, (30, 30))
        goal_rec = scaled_goal.get_rect(center = self.goal_1.body.position)
        screen.blit(scaled_goal, goal_rec)

        screen.blit(self.rotated_brick, self.brick_1.scale_back(self.rotated_brick))
        screen.blit(self.rotated_brick2, self.brick_2.scale_back(self.rotated_brick2))