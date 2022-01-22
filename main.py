import sys
from tracemalloc import start
from turtle import window_width
import pygame
import pymunk
import components.func as fc
import components.ball as ball
from components.game_over import Gameover
from components.main_ball import Main_Ball
from stage.stage import Stage
from stage.stage_01 import Stage_01
import components.goal as goal
import components.colors as colors
from pymunk.vec2d import Vec2d
import pymunk.pygame_util
from stage.stage_02 import Stage_02
from stage.stage_03 import Stage_03
from stage.stage_04 import Stage_04
from stage.stage_05 import Stage_05
from stage.stage_06 import Stage_06
from components.start import Start
from pygame import mixer

from stage.stage_07 import Stage_07
from stage.stage_08 import Stage_08


# 1, 2,3,4 -> ball, wall, brick, goal

pygame.init()

# window width, height
win_width = 1500
win_heght = 800

trial = 0
stage_num = 1
num_of_stage = 8
# start_button_flag = False


size = (win_width, win_heght)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ball In One")

# mixer.init()
mixer.music.load('sound/BFL_Base_Games_BGM.wav')


space = pymunk.Space()

start_button_flag = True

die = False

stages = [Stage(space, screen) for i in range(num_of_stage)]


def stage_select(stg_num):
    # re = stages[stg_num]

    if stg_num == 1:
        return Stage_01(space, screen)
    elif stage_num == 2:
        return Stage_02(space, screen)
    elif stage_num == 3:
        return Stage_03(space, screen)
    elif stage_num == 4:
        return Stage_04(space, screen)
    elif stage_num == 5:
        return Stage_05(space, screen)
    elif stage_num == 6:
        return Stage_06(space, screen)
    elif stage_num == 7:
        return Stage_07(space, screen)
    elif stage_num == 8:
        return Stage_08(space, screen)
    return Stage(space, screen)
    

def game_main(st1):
    global trial, start_button_flag, stage_num, space, die, num_of_stage
    # main_ball = st1.main_ball
    goal_1 = st1.goal_1
    
    # space.gravity = 0, 500
    gravity_flag = False

    FPS = 80

    # mouse position
    mouse_down_pos = (0, 0)
    mouse_up_pos = (0, 0)
    mouse_pos = (0, 0)

    running = True
    mouse_drag = False
    mouse_drag_end = False
    debug_draw = False

    clock = pygame.time.Clock()

    # goal_1 = goal.Goal(1300.0, 760.0, 4, 15)
    # space.add(goal_1.body, goal_1.shape)
    ball_y = 800 -st1.bottom_img.get_height() * 0.5 - 10
    main_ball = ball.Ball(space, 40.0, ball_y, 1, 1)
    

    # collision handler
    colliede_handler = space.add_collision_handler(1, 4)
    colliede_handler.post_solve = goal_1.finished
    # print(colliede_handler.post_solve)
    
    while running:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                running = False # Flag that we are done so we exit this loop
                die = True
                sys.exit()
                return False

            # Restart the stage
            if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_SPACE:
                        # ball 
                        space.remove(main_ball.body)
                        space.remove(main_ball.shape)
                        #
                        # st1 = Stage_02(space, screen)
                        # main_ball = ball.Ball(space, 40.0, 775.0, 1, 1)
                        main_ball = ball.Ball(space, 40.0, ball_y, 1, 1)
                        # main_ball = ball.Ball(40.0, 775.0, 1, 1)
                        # space.add(main_ball.body, main_ball.shape)
                        gravity_flag = False
                        mouse_drag = False
                        mouse_drag_end = False
                        # increase the score
                    if event.key == pygame.K_d:
                        debug_draw = not debug_draw

            # mouse clicked
            if event.type == pygame.MOUSEBUTTONDOWN and not start_button_flag:
                mouse_down_pos = pygame.mouse.get_pos()
                mouse_pos = pygame.mouse.get_pos()
                mouse_drag = True

                #
                # start_button_flag = False
                # print("mouse down")
            
            if event.type == pygame.MOUSEBUTTONUP and not start_button_flag:
                mouse_up_pos = pygame.mouse.get_pos()
                mouse_drag = False
                mouse_drag_end = True
                trial += 1

            if event.type == pygame.MOUSEMOTION and mouse_drag:
                mouse_pos = pygame.mouse.get_pos()

        # calculate the velocity of the ball after the mouse drag
        if mouse_drag_end and gravity_flag == False:
            if main_ball.drag_mouse_vel(space, mouse_up_pos, mouse_down_pos):
                mouse_drag_end = False
                # gravity is set after the launch 
                gravity_flag = True
                space.gravity = 0, 500

        
        screen.fill(colors.LIGHT_SKY)
        # screen.blit(special_flags=B)

        

        st1.updating(screen, trial, stage_num) # updating scores and stage num
        st1.update(screen)
        st1.late_updating(screen, trial, stage_num)

        # show the direction of the ball drag
        if mouse_drag:
            # screen.blit(w1,mouse_pos)
            power_line_vec = fc.tup_mul(fc.tup_sub(mouse_pos ,mouse_down_pos), 0.5)
            post_vec = main_ball.body.position
            for i in range(20):
                if i % 2 == 0:
                    ball_vec = fc.tup_add((post_vec), fc.tup_mul(power_line_vec, 1/20))
                    pygame.draw.line(screen, colors.COLOR_LIGHT ,post_vec, ball_vec, 2)
                else:
                    ball_vec = fc.tup_add((post_vec), fc.tup_mul(power_line_vec, 1/50))
                post_vec = ball_vec
        
        
        main_ball.update(screen)

        # options = pymunk.pygame_util.DrawOptions(screen)
        # if(debug_draw):
        #     space.debug_draw(options)

        
        if goal_1.complete:
            stage_num += 1
            scaled_star = pygame.transform.scale(goal_1.explosion_img, (30, 30))
            goal_rec = scaled_star.get_rect(center = goal_1.body.position)
            # print('log:', scaled_star, goal_rec)
            screen.blit(scaled_star, goal_rec)
            
            for i in range(50):
                pygame.display.update()
            
            return
        
        pygame.display.update()
        clock.tick(FPS)
        if(gravity_flag):
            space.step(1/FPS)

st = Start(screen, win_width, win_heght)
start_button_flag = st.running(screen)


mixer.music.play(-1)
# count = 1
# while not die and count <= num_of_stage:
#     # play bgm
#     game_main(stage_select(stage_num))
#     space = pymunk.Space()
#     count += 1

die = False
if not die:
    mixer.music.stop()
    gg = Gameover(screen, win_width, win_heght, trial)
    restart = gg.running(screen)


# print(trial)
pygame.quit()