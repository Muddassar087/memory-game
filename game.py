import pygame, sys, random
from collections import Counter

screen = pygame.display.set_mode((440, 540))
clock = pygame.time.Clock()

MARGIN = 10
Run = True
list_blocks = []
colors = [(100,100,200), (150,200, 100) , (230,111, 121), (111, 222, 150) ,(101, 255, 255)]
revealed = 0
colorsFound = []

tries = 11
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 20)
textsurface = myfont.render('Tries - {0}'.format(tries), False, (255,255,255))

def addFoundColor(color):
    colorsFound.append(color)
    x = Counter(colorsFound)
    return checkWon(x)

def reveal(revealed=0):
    p = list_blocks
    if revealed == 0:
        for i in p:
            random.shuffle(p)
            for k in i:
                rect = k[0]
                rect.width = 0
                rect.height = 0
                rect.x = 0
                rect.y = 0
            pygame.display.update()
            clock.tick(1)


def make_gird(rowBlocks = 7, colBlocks = 7):
    YR = 50
    XR = 12
    random.shuffle( colors )
    for x in range(rowBlocks):
        row = []
        for y in range(colBlocks):
            random.shuffle( colors )
            rect = pygame.Rect(XR, YR, 50, 50)
            shape = pygame.Rect(XR+13, YR+13, 25, 25)
            row.append([rect, (255, 255, 255), shape, (colors[0])])
            XR+=50+MARGIN
        XR = 12
        YR += 50+MARGIN
        list_blocks.append(row)


make_gird()

def getBlock(rect):
    rect.height = 0
    rect.width = 0
    rect.x = 0
    rect.y = 0
    return rect


def fillBoxes():
    for i in list_blocks:
        for k in i:
            rect = j[0]
            rect.width = 50
            rect.height = 50

i = 0

def checkWon(dict):

    for values in dict.values():
        if values == 3:
            print("you won")
            return True
    return False


def main(textsurface, run):
    tries = 20
    won = False
    RUN = run
    while RUN:
        mx, my = (0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                tries -= 1
                mx,my = pygame.mouse.get_pos()
                for i in list_blocks:
                    for j in i:
                        rect, col = j[0], j[1]
                        if rect.collidepoint((mx,my)):
                            j[0] = getBlock(rect)
                            if addFoundColor(j[3]):
                                RUN = False
        if tries == 0:
            sys.exit()

        screen.fill( (100,100,100) )
        screen.blit(textsurface, (10,5))
        textsurface = myfont.render( 'Tries - {0}'.format( tries ), False, (255, 255, 255) )
        for i in list_blocks:
            for j in i:
                rect, color = j[0], j[1]
                shape, col = j[2], j[3]
                pygame.draw.rect( screen, col, shape)
                pygame.draw.rect(screen,color, rect)

        pygame.display.update()

    return won

if __name__ == '__main__':
    main( textsurface=textsurface, run=True)
