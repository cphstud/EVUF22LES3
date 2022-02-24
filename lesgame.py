from random import randint
import pygame
import sys

#variabler
width=600
height=400
delta=int(width/10)

xpos_bird=width-delta
ypos_bird=delta
xpos_tree=100
ypos_tree=100

speed_bird=1
framerate=120
birds=[]

def give_birds (antal):
    bird = []

    for tal in range(antal):
        name = f'bird_{tal}'
        ypos_bird = randint(20, height/2)
        xpos_bird = randint(width-40, width-20)
        speed_bird = randint(1,3)
        counter = tal
        link = pygame.image.load("resources/bird.png")
        bird={"link": link, "name": name, "count": counter, "xpos": xpos_bird, "ypos": ypos_bird, "speed": speed_bird}
        birds.append(bird)
    return(birds)


#pygame initialization
pygame.init()
clock=pygame.time.Clock()
birdlist=give_birds(5)

#set up screen
screen=pygame.display.set_mode((600,400))

#load images into Pygame
background=pygame.image.load("resources/green2.png")
bird=pygame.image.load("resources/bird.png")
tree=pygame.image.load("resources/tree2.png")

#start loop
while True:
    #tjek events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    #make bird move


    #put items on screen
    screen.blit(background,(0,0))


    for bird in birdlist:
        bird["xpos"] = bird["xpos"] - bird["speed"]
        screen.blit(bird["link"],(bird["xpos"], (bird["ypos"])))

    screen.blit(tree, (200, 100))
    clock.tick(60)
    pygame.display.update()
