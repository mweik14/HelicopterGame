import pygame
import time
from random import randint,randrange
###pygame logs keypresses, mouse location- allows more focus on game logic
#define colors used
black = (0,0,0)
white = (255,255,255)

sunset = (253,72,47)

greenyellow = (184,255,0)
brightblue = (47,228,253)
orange = (255,113,0)
yellow = (255,236,0)
purple = (252,67,255)

colorChoices = [greenyellow,brightblue,orange,yellow,purple]

#initializes pygame
pygame.init()


#define surface variable:set_mode currently setting resolution
surfaceWidth = 800
surfaceHeight = 500
imageHeight = 43
imageWidth = 100
surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
#title
pygame.display.set_caption('Helicopter')
#measure and set FPS
clock = pygame.time.Clock()

#functions
def helicopter(x, y, image):
    surface.blit(img, (x,y))
    
#define image of heli
img = pygame.image.load('Helicopter.png')
#function for scoring
def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: "+str(count), True, white)
    surface.blit(text,[0,0])

#creating function and variables for gaps for avoiding
def blocks(x_block, y_block, block_width, block_height, gap, colorChoice):
    pygame.draw.rect(surface, colorChoice, [x_block,y_block,block_width,block_height])
    pygame.draw.rect(surface, colorChoice, [x_block,y_block+block_height+gap,block_width, surfaceHeight])
#function for quiting or not after game over
def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        
        return event.key

#fuinctions for making text box
def makeTextObjs(text, font):
    textSurface = font.render(text, True, sunset)
    return textSurface, textSurface.get_rect()


#defines msgSurface for messages to user
def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)
    #creates message boxes
    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)
    #instructs user to press any key
    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)


    pygame.display.update()
    #givers time for extra press to not close text
    time.sleep(1)
    #allows player to exit game
    while replay_or_quit() == None:
        clock.tick()

    main()     

#defines game over functions
def gameOver():
    #send message to user
    msgSurface('Kaboom!')


#game loop
def main():
    #starting coordinates for heli
    x = 150
    y = 200

    #Heli constantly move down
    y_move = 5

    #block definitions
    x_block = surfaceWidth
    y_block = 0

    block_width = 75
    block_height = randint(0, (surfaceHeight / 2))
    gap = imageHeight * 3
        #speed of block move
    block_move = 4
    #initial score
    current_score = 0

    blockColor = colorChoice = colorChoices[randrange(0,len(colorChoices))]
    
    game_over = False

    while not game_over:
       #check for events, changes variables,  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                # moves heli up
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
                #  moves heli down
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                        y_move = 5

        y += y_move

        #paints surface black
        surface.fill(black)
        #adds heli to display
        helicopter(x, y, img)
        #adds blocks to dislay
        blocks(x_block, y_block, block_width, block_height, gap, blockColor)
        x_block -= block_move
        #establish score
        score(current_score)        
        #game logic
        #Settting boundaries for heli(image is 40px)
        if y > surfaceHeight-40 or y < 0:
            gameOver()
        #Brings in new blocks and new gap 
        if x_block < (-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0, (surfaceHeight/ 2))
            blockColor = colorChoices[randrange(0,len(colorChoice))]
            current_score += 1
        #Boundaries for blocks/success or failure passing block
        if x + imageWidth > x_block:
            if x < x_block + block_width:
##                print('possibly within the boundaries of x upper')
                if y < block_height:
##                    print('Y crossover UPPER!')
                    if x - imageWidth < block_width + x_block:
##                        print('Game over with Upper')
                        gameOver()
        # lower block
        if x + imageWidth > x_block:
##            print('X crossover')
            if y + imageHeight > block_height+gap:
##                print('Y crossover lower')
                if x < block_width + x_block:
##                    print('game over lower!')
                    gameOver()
       #logic for score 
        ##if x_block < (x - block_width) < x_block + block_move:
            ##current_score += 1

        if 3 <= current_score < 5:
            block_move = 5.5
            gap = imageHeight * 2.9
        if 5 <= current_score < 10:
            block_move = 6
            gap = imageHeight * 2.8
        if 10 <= current_score < 15:
            block_move = 6.5
            gap = imageHeight * 2.7
        #game code
            #updates specific items
        pygame.display.update()
        #FPS
        clock.tick(60)
main()
#exits game
pygame.quit()
#complete exit
quit()
    
