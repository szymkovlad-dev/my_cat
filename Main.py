import random
import pygame

#initialize pygame
pygame.init()

#set display surface
WINDOW_WIDTH = 1300
WINDOW_HIGH = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGH))
pygame.display.set_caption("My cat")

#set game value
PLAYER_VELOCITY = 10
PLAYER_STARTING_LIVES = 9
FISH_STARTING_VELOCITY = 5
BUFFER_DISTANCE = 100
weight = 0.0
player_lives = PLAYER_STARTING_LIVES
fish_velocity = FISH_STARTING_VELOCITY
FISH_ACCELERATION = 0.15

#colours
GREEN = (0,255,0)
DARK_GREEN = (10,50,10)
WHITE = (255,255,255)
BLACK = (0,0,0)
COLOR_FOR_GIRLS = (232, 17, 144)
KHAKI = (97,131,88)
BLUE =  (0,0,255)

#Set fonds
font = pygame.font.Font("resources/fonds/Cookiemonster-gv11.ttf",32)

#set text
weight_text = font.render("Weight: " + str(weight) + "KG",True, GREEN, DARK_GREEN)
weight_text_rect = weight_text.get_rect()
weight_text_rect.topleft = (10,10)

title_text = font.render("My cat",True, GREEN, WHITE)
title_text_rect = title_text.get_rect()
title_text_rect.centerx = WINDOW_WIDTH // 2
title_text_rect.centery = 20

player_lives_text = font.render("Lives" + str(player_lives),True, GREEN, DARK_GREEN)
player_lives_rect = player_lives_text.get_rect()
player_lives_rect.topright = (WINDOW_WIDTH - 50, 10)

game_over_text = font.render("Game Over" ,True, GREEN, DARK_GREEN)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WINDOW_WIDTH //2 , WINDOW_HIGH //2)

continue_text = font.render("Press any key to restart" ,True, GREEN, DARK_GREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH //2 , WINDOW_HIGH //2 + 32)

#set fps and clock
FPS = 60
clock = pygame.time.Clock()

#Set images
player = pygame.image.load("resources/Images/dronPlusCat.png")
player = pygame.transform.scale(player, (70, 70))  # ширина, высота
player_rect = player.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HIGH //2

fish = pygame.image.load("resources/Images/Fishy.png")
fish = pygame.transform.scale(fish, (70, 70))  # ширина, высота
fish_rect = fish.get_rect()
fish_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
fish_rect.y = random.randint(64, WINDOW_HIGH - 32)

#set background
background = pygame.image.load("resources/Images/Background.png")
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HIGH))
background_rect = background.get_rect()
background_rect.topleft = (0,0)


#Main game loop
running = True
while running:
    for event in pygame.event.get():

        #quit game
        if event.type == pygame.QUIT:
            running = False

    #check to see if user wants to move
    keys = pygame.key.get_pressed()
    if keys [pygame.K_UP] and player_rect.top > 64 :
        player_rect.y -= PLAYER_VELOCITY
    if keys [pygame.K_DOWN] and player_rect.bottom < WINDOW_HIGH :
        player_rect.y += PLAYER_VELOCITY
    # if keys[pygame.K_RIGHT] and player_rect.right > WINDOW_WIDTH:
    #     player_rect.x += PLAYER_VELOCITY
    # if keys[pygame.K_LEFT] and player_rect.bottom < 0:
    #     player_rect.x -= PLAYER_VELOCITY

    #move the fishy
    if fish_rect.x < 0:
        #player missed the fishy
        player_lives -= 1
        fish_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        fish_rect.y = random.randint(64, WINDOW_HIGH - 32)
    else:
        #move the fishy
        fish_rect.x -= fish_velocity

    #check the collisions
    if player_rect.colliderect(fish_rect):
        weight += 0.5
        fish_velocity += FISH_ACCELERATION
        fish_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        fish_rect.y = random.randint(64, WINDOW_HIGH - 32)


    #update HUD
    weight_text = font.render("Weight: " + str(weight) + " KG",True, GREEN, DARK_GREEN)
    player_lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARK_GREEN)

    #Check for game over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_text_rect)
        display_surface.blit(continue_text, continue_text_rect)
        pygame.display.update()

        #pause the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.K_DOWN:
                    weight = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_lives_rect.y = WINDOW_HIGH //2
                    fish_velocity = FISH_STARTING_VELOCITY
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused == False
                    running = False
    #blit background
    display_surface.blit(background, background_rect)

    #fill the display
    # display_surface.fill()

    #blit the HUD to screen
    display_surface.blit(weight_text, weight_text_rect)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(player_lives_text, player_lives_rect)



    #blit assets to screen
    display_surface.blit(player,player_rect)
    display_surface.blit(fish,fish_rect)

    #update the display
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()

