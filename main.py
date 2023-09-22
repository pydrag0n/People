import pygame
import random
import time
pygame.init()

class Game():
    def __init__(self, window_height=1000, window_width=675, size_player=40):
        
        self.window_height = window_height
        self.window_width = window_width
        # КОНСТАНТЫ
        DEFAULT_PLAYER_CORD_X = 10
        self.DEFAULT_PLAYER_CORD_Y = 544
        DEFAULT_PLAYER_SPEED_DOWN_MOVE = 10
        
        DEFAULT_PLAYER_JAMP_HEIGHT = 200
        DEFAULT_PLAYER_ASSETS = ["PlayerAssets\Walk_1.png", 
                              "PlayerAssets\Walk_2.png", 
                              "PlayerAssets\Walk_3.png", 
                              "PlayerAssets\Walk_4.png", 
                              "PlayerAssets\Walk_5.png", 
                              "PlayerAssets\Walk_6.png", 
                              "PlayerAssets\Walk_7.png", 
                              "PlayerAssets\Walk_8.png"]
        
        
        
        DEFAULT_BOT_CORD_X = 1000
        self.DEFAULT_BOT_SPEED = 10
        

        # ------------
        
       
        # player
        self.score = 0
        self.window = pygame.display.set_mode((self.window_height, self.window_width))
        self.player_size= size_player
        self.up = False # разрешенно прыгать
        self.clock = pygame.time.Clock()
        self.player_x = DEFAULT_PLAYER_CORD_X
        self.player_y = self.DEFAULT_PLAYER_CORD_Y
        self.player_speed_down_move = DEFAULT_PLAYER_SPEED_DOWN_MOVE
        self.player_jump_height = DEFAULT_PLAYER_JAMP_HEIGHT
        self.game_over_menu = False 
        self.bg_imgX = 0
        self.nb = 1
        self.default_player_assets = DEFAULT_PLAYER_ASSETS
        
        # ------------
        
        # bot
        self.botX = DEFAULT_BOT_CORD_X
        self.botSpeed = self.DEFAULT_BOT_SPEED
        
    def fon(self, img):
        
        background_image = pygame.image.load(img)
        self.window.blit(background_image, (self.bg_imgX, 0))
        self.window.blit(background_image, (self.bg_imgX+1248, 0))
        self.bg_imgX -= 1
        if self.bg_imgX <= -1250:
            self.bg_imgX = 0
        
        
    def game_over(self):
        f1 = pygame.font.Font('Roboto\Roboto-Black.ttf',36)
        text1 = f1.render('press r for restart', 1, (223, 44, 100))
        text2 = f1.render('press q for quit', 1, (223, 44, 100))
        self.window.blit(text1, (10, 50))
        self.window.blit(text2, (10, 100))
        pygame.display.update()
        
        
    def monster(self):
        self.botX -= self.botSpeed
        if self.botX <= -50:
            self.botX = self.window_height + 25
            self.bot_sizeX = random.randint(10, 30)
            self.bot_sizeY = random.randint(10, 30)
            if random.randint(1, 5)==5:
                self.botSpeed += 1
        
        self.draw_bot = pygame.draw.rect(self.window, (211, 33, 121), [self.botX, 544, 25, 25]) 
        return self.draw_bot

        
    def player(self):
        if self.player_y >= 544:
            self.up = False #  разрешенно
        elif self.up:
            self.player_y += self.player_speed_down_move
        self.img_player = pygame.image.load(f"{self.default_player_assets[self.nb]}")
        self.nb += 1
        if self.nb == 8:
            self.nb = 1
        self.window.blit(self.img_player, (self.player_x, self.player_y))                           
       
    def main(self):
        run = True
        while run:
            if self.game_over_menu == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and not self.up:
                            self.player_y -= self.player_jump_height
                            self.up = True # не разрешенно прыгать 
                        elif event.key == pygame.K_DOWN:
                            self.player_y = self.DEFAULT_PLAYER_CORD_Y
                self.img_player_rect = pygame.draw.rect(self.window, (0,0,0), [self.player_x+10, 
                                                                       self.player_y+3, 17,30])  
                self.fon('fon.jpg')
                self.monster()
                self.player()
                
                self.clock.tick(30)
                
                if self.draw_bot.colliderect(self.img_player_rect):
                    self.game_over_menu = True
                    
                
                pygame.display.update()
                
                
            elif self.game_over_menu:
                while self.game_over_menu:
                    self.game_over()
                    self.clock.tick(10)
                    
                    for ev in pygame.event.get():
                        if ev.type == pygame.QUIT:
                            self.game_over_menu = False
                            run = False
                        if ev.type == pygame.KEYDOWN:
                            if ev.key == pygame.K_r:
                                self.game_over_menu = False
                                self.botX = self.window_width
                                self.botSpeed = self.DEFAULT_BOT_SPEED
        
Game().main()