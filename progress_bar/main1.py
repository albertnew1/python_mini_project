#imports
import pygame,sys,threading

pygame.init()
#screen and font
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Loading Bar")

FONT = pygame.font.SysFont("Roboto",100)

#clock
CLOCK = pygame.time.Clock()

#work
WORK = 10000000 #this is the latency if you want to reduce the bar width's speed

#loading background
LOADING_BG = pygame.image.load("Loading Bar Background.png")
LOADING_BG_RECT = LOADING_BG.get_rect(center=(640,360))

#loading bars and variables
loading_bar = pygame.image.load("Loading Bar.png")
loading_bar_rect = loading_bar.get_rect(midleft=(280,360))
loading_finished = False
loading_progress = 0
loading_bar_width = 8 #pixels

def doWork():
    #do some math WORK amount times
    global loading_finished, loading_progress

    for i in range(WORK):
        math_equation = 523678 / 789456 * 89456 #this is how the bar width work
        loading_progress = i
    loading_finished = True

#finished text (optional)
finished = FONT.render("Done", True, "white")
finished_rect = finished.get_rect(center=(640, 360))

#thread
threading.Thread(target=doWork).start()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("#0d0e2e")

    if not loading_finished: 
        loading_bar_width = loading_progress / WORK * 720 #pixel
        loading_bar = pygame.transform.scale(loading_bar,(int(loading_bar_width),150))
        loading_bar_rect = loading_bar.get_rect(midleft=(280,360))

        screen.blit(LOADING_BG, LOADING_BG_RECT)
        screen.blit(loading_bar, loading_bar_rect)
    else:
        screen.blit(finished, finished_rect)

    pygame.display.update()
    CLOCK.tick(60)

