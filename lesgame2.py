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
        xpos_bird = randint(width-20, width+200)
        speed_bird = randint(1,4)
        counter = tal
        link = pygame.image.load("resources/bird.png")
        bird={"link": link, "name": name, "count": counter, "xpos": xpos_bird, "ypos": ypos_bird, "speed": speed_bird}
        birds.append(bird)
    return(birds)


#pygame initialization
pygame.init()
clock=pygame.time.Clock()
birdlist=give_birds(20)

#set up screen
screen=pygame.display.set_mode((600,400))

#load images into Pygame
background=pygame.image.load("resources/blue.jpg")
bird=pygame.image.load("resources/bird.png")
tree=pygame.image.load("resources/tree2.png")
tree2=pygame.image.load("resources/tree2.png")
tree3=pygame.image.load("resources/tree2.png")
sigtekorn=pygame.image.load("resources/sigtekorn2.png")
sigtekornrect=sigtekorn.get_rect(center=(width/2, height/2))
birdrect=bird.get_rect(center=(width/2, height/2))

pos=(100,100)
#start loop
while True:
    #tjek events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEMOTION:
            #print(event.pos)
            pos=event.pos

    #make bird move
    xpos_bird=xpos_bird-1


    #put items on screen
    screen.blit(background,(0,0))
    screen.blit(tree, (150, 180))
    screen.blit(tree2, (350, 180))

    birdrect = bird.get_rect(center=(xpos_bird, ypos_bird))
    screen.blit(bird, birdrect)
    sigtekornrect = sigtekorn.get_rect(center=(pos))
    screen.blit(sigtekorn,sigtekornrect)
    if sigtekornrect.colliderect(birdrect) == True:
        #print("collision")
        xpos_bird=width+100

    #for bird in birdlist:
    #   bird["xpos"] = bird["xpos"] - bird["speed"]
    #   screen.blit(bird["link"],(bird["xpos"], (bird["ypos"])))

    screen.blit(tree3, (50, 20))
    clock.tick(20)
    pygame.display.update()
