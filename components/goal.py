from json import load
import pygame
import pymunk
import random
from pygame import mixer

class Goal():
    def __init__(self, screen, x, y, collision_type, radius = 15):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = [x, y]
        # self.body.velocity = [0,0]
        # self.body.velocity = 0, up * 100
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.collision_type = collision_type
        # space.add(self.body, self.shape)

        # score
        self.trial = 0
        self.end = False
        self.complete = False
        self.screen = screen
        # sound
        self.goal_in_sound = pygame.mixer.Sound('sound/Small_Win.wav')
        
        # explosion image
        self.explosion_img = pygame.image.load('images/tank_explosion4.png')


    def finished(self, arbiter, space, data):
        # when the ball hit the goal for the first time
        if(not self.end): # only count the first collision
            print("Good Job")
            self.complete = True  # The stage is completed
            self.explode()
            self.goal_in_sound.play()
        # print(self.end)
        return True

    def explode(self):
        scaled_star = pygame.transform.scale(self.explosion_img, (30, 30))
        goal_rec = scaled_star.get_rect(center = self.body.position)
        print('log in goal:', scaled_star, goal_rec)
        self.screen.blit(scaled_star, goal_rec)
