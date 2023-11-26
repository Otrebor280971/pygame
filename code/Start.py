  
import pygame,sys


screen = pygame.display.set_mode((1200, 704))
pygame.display.set_caption("Solar Bastions")

pygame.font.init()
font = pygame.font.Font("graphics/ui/Letra_1.ttf", 90)
font_t = pygame.font.Font("graphics/ui/Letra_1.ttf", 110)

pygame.mixer.init()
pygame.mixer.music.load('audio/City of Tears.mp3')
pygame.mixer.music.play(-1)

background = pygame.image.load("graphics/decoration/start_screen.png")
background = pygame.transform.scale(background, (1200, 704))

scene = 1

color = 'white'


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            mpos = pygame.mouse.get_pos()
            if 450 <= mpos[0] <= 750 and 500 <= mpos[1] <= 650:
                color = 'grey50'


    screen.blit(background, (0, 0))

    title = font_t.render("Solar Bastions", True, 'white')
    title_rect = title.get_rect()
    title_rect.center = (650, 120)
    screen.blit(title, title_rect)

    pygame.draw.rect(screen, color, (450, 500, 300, 150), 0)
    start = font.render("Start", True, 'black')
    start_rect = start.get_rect()
    start_rect.center = (600, 575)
    screen.blit(start, start_rect)

    pygame.display.flip()