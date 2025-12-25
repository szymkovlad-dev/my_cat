import pygame

#initialize pygame
pygame.init()

#set display surface
WINDOW_WIDTH = 1000
WINDOW_HIGH = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGH))

#set game value
PLAYER_VELOCITY = 10

#colours
GREEN = (0,255,0)
DARK_GREEN = (10,50,10)
WHITE = (255,255,255)
BLACK = (0,0,0)
COLOR_FOR_GIRLS = (232, 17, 144)
KHAKI = (97,131,88)
BLUE =  (0,0,255)

#set fps and clock
FPS = 60
clock = pygame.time.Clock()

#Set images
player = pygame.image.load("resources/Images/dronPlusCat.png")
player = pygame.transform.scale(player, (70, 70))  # ширина, высота
player_rect = player.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HIGH //2

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

#fill the display
    # display_surface.fill()

#blit background
    display_surface.blit(background,background_rect)

#blit assets to screen
    display_surface.blit(player,player_rect)


#update the display
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()

