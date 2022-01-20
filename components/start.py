import sys
import components.colors as colors
import pygame

class Start():
    def __init__(self,screen, width, height) -> None:
        # self.small_font = pygame.font.SysFont('Corbel', 150)
        # self.title_font = pygame.font.SysFont('Corbel', 320)
        self.small_font = pygame.font.Font('font/fofbb_reg.ttf', 150)
        self.title_font = pygame.font.Font('font/fofbb_reg.ttf', 260)
        self.text = self.small_font.render('Game Start', True, colors.WHITE)
        self.title = self.title_font.render('Ball In One', True, colors.WHITE)
        self.width = width
        self.height = height
        self.start_button_width = 800
        self.start_button_height = 150

        self.bottom_img = pygame.image.load(r'images/bottom.png')

        # self.running(screen)

    def running(self, screen):
        width = self.width
        height = self.height
        start_button_width = self.start_button_width
        start_button_height = self.start_button_height
        start_button_pos_x = width * 0.5 - start_button_width * 0.5
        start_button_pos_y = height * 0.7 - start_button_height * 0.5

        title_text_pos_x = width * 0.5
        title_text_pos_y = height * 0.3

        while True: 
            for ev in pygame.event.get(): 
                
                if ev.type == pygame.QUIT: 
                    # pygame.quit()
                    sys.exit() 
                    
                #checks if a mouse is clicked 
                if ev.type == pygame.MOUSEBUTTONUP: 
                    
                    #if the mouse is clicked on the 
                    # button the game is terminated 
                    if start_button_pos_x <= mouse[0] <= start_button_pos_x + start_button_width and start_button_pos_y <= mouse[1] <= start_button_pos_y + start_button_height: 
                        # pygame.quit()
                        return False
                        
            # fills the screen with a color 
            screen.fill(colors.LIGHT_SKY) 

            # print("start page log")
            
            # stores the (x,y) coordinates into 
            # the variable as a tuple 
            mouse = pygame.mouse.get_pos() 
            
            # if mouse is hovered on a button it 
            # changes to lighter shade 
            if start_button_pos_x <= mouse[0] <= start_button_pos_x + start_button_width and start_button_pos_y <= mouse[1] <= start_button_pos_y + start_button_height: 
                pygame.draw.rect(screen,colors.COLOR_LIGHT,[start_button_pos_x, start_button_pos_y, start_button_width, start_button_height],0,20) 
                
            else: 
                pygame.draw.rect(screen,colors.COLOR_DARK,[start_button_pos_x, start_button_pos_y, start_button_width, start_button_height],0,20) 
            
            # superimposing the text onto our button 
            text_rect = self.text.get_rect(center = (start_button_pos_x + start_button_width * 0.5, start_button_pos_y + start_button_height * 0.5))
            screen.blit(self.text , text_rect)

            # superimposing the text onto our button 
            title_rect = self.title.get_rect(center = (title_text_pos_x, title_text_pos_y))
            screen.blit(self.title , title_rect)

            # bottom image
            screen.blit(self.bottom_img,(-1, 800 - self.bottom_img.get_height() * 0.5))
            pygame.display.update() 