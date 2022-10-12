import asyncio
import pygame, random, time, sys

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_icon(pygame.image.load("elmo.png"))
primus = pygame.image.load("primus_meest_creepy.png")
primus_dead = pygame.image.load("primus_dood.png")

window = pygame.display.set_mode((720, 720))
pygame.font.init()
pygame.display.set_caption("Flappy Primus")

async def main():

    font_small = pygame.font.Font("font/Pixeltype.ttf", 40)
    font_large = pygame.font.Font("font/Pixeltype.ttf", 95)

    title = font_large.render('Flappy Primus', True, (0, 0, 0), None)
    title_rect = title.get_rect(center = (300, 220))
    caption = font_small.render('Druk op de spatie om te starten', True, (0, 0, 0), None)
    caption_rect = caption.get_rect(center = (250, 500))
    cogent_logo = pygame.image.load("Logo_CollectievandeGentenaar.png")
    cogent_logo_rect = cogent_logo.get_rect(topleft = (20, 0))

    global start, vel, ypos, hscore, p1, p2, tscore, died
    start = False
    vel = 0
    ypos = 300
    hscore = 0
    pipe = [720, random.randint(0, 380)]
    tscore = 0
    died = False

    while True:
        window.fill((1, 165, 126))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if start == False:
                        ypos = 300
                        start = True
                    vel = 7.
        if start:
            window.blit(primus, (50, ypos))
            ypos = ypos - vel
            vel = vel - 0.5
            pygame.draw.rect(window, (234, 148, 170), (pipe[0], 0, 50, pipe[1]))
            pygame.draw.rect(window, (234, 148, 170), (pipe[0], pipe[1] + 300, 50, 720))
            window.blit(font_small.render('Score: ' + str(tscore), True, (0, 0, 0), None), (10, 10))
            pipe[0] = pipe[0] - 5
            if pipe[0] < -50:
                pipe[0] = 720
                pipe[1] = random.randint(0, 380)
                tscore = tscore + 1
                if tscore > hscore:
                    hscore = tscore
        else:
            if died:
                window.blit(primus_dead, (100, 500))
                window.blit(cogent_logo, cogent_logo_rect)
            window.blit(title, title_rect)
            window.blit(cogent_logo, cogent_logo_rect)
            window.blit(caption, (100, 300))
            window.blit(font_small.render('High score: ' + str(hscore), True, (0, 0, 0), None), (100, 400))
        if (pipe[0] < 164 and pipe[0] > 14) and (ypos + 192 > pipe[1] + 300 or ypos < pipe[1]):
            ypos = 528
        if ypos >= 528:
            ypos = 528
            caption = font_small.render('Game over', True, (0, 0, 0), None)
            start = False
            tscore = 0
            pipe[0] = 720
            died = True
        elif ypos < 0:
            ypos = 0
            vel = -abs(vel)
        clock.tick(60)

        pygame.display.flip()
        await asyncio.sleep(0)

asyncio.run(main())
