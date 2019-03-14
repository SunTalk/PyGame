import pygame
import time
import random

pygame.init()

display_width = 960
display_height = 600

white = (255,255,255)
black = (0,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('HW04')
clock = pygame.time.Clock()

announcement_font = pygame.font.Font('Regular.ttf',25)
mario = pygame.image.load('Mario.png')
mario = pygame.transform.scale(mario, (75,116))
goomba = pygame.image.load('goomba.png')
goomba = pygame.transform.scale(goomba,(60,80))
mushroom = pygame.image.load('mushroom.png')
mushroom = pygame.transform.scale(mushroom,(50,50))

background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background,(960,600))


def score(blood,goal):
	text_blood = announcement_font.render("Life: "+str(blood), True, black)
	gameDisplay.blit(text_blood,(10,0))
	text_goal = announcement_font.render("Score: "+str(goal), True, black)
	gameDisplay.blit(text_goal,(10,30))
### end score(blood,goal)

def mario_display(x,y):
	gameDisplay.blit(mario,(x,y))
def goomba_display(x,y):
	gameDisplay.blit(goomba,(x,y))
def mushroom_display(x,y):
	gameDisplay.blit(mushroom,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def message_display(text):
	largeText = pygame.font.Font('Regular.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()
	time.sleep(2)
	
def die():
	message_display('You Fail')


def gameloop():
	end = False
	mario_x = 440
	mario_y = 355
	x_change = 0
	blood = 3
	goal = 0
	speed = 1

	goomba_x = random.randrange(0,display_width-30)
	goomba_y = random.randrange(-100,-40)
	mushroom_x = random.randrange(0,display_width-50)
	mushroom_y = random.randrange(-300,-100)

	while not end:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
					x_change = 0
		mario_x += x_change

		if mario_x < 0 :
			mario_x = 0
		if mario_x > 885 :
			mario_x = 885

		speed = goal +5
		goomba_y += speed
		
		if goomba_y > display_height :
			goomba_x = random.randrange(0,display_width-30)
			goomba_y = random.randrange(-100,-40)
		mushroom_y += 5
		if mushroom_y > display_height :
			mushroom_x = random.randrange(0,display_width-50)
			mushroom_y = random.randrange(-300,-100)

		if goomba_x+30 > mario_x and goomba_x+30 < mario_x+75 and goomba_y+40 > mario_y and goomba_y+40 < mario_y+116:
			blood -= 1
			goomba_x = random.randrange(0,display_width-30)
			goomba_y = random.randrange(-100,-40)
		if mushroom_x+25 > mario_x and mushroom_x+25 < mario_x+75 and mushroom_y+25 > mario_y and mushroom_y+25 < mario_y+116:
			goal += 1
			mushroom_x = random.randrange(0,display_width-50)
			mushroom_y = random.randrange(-300,-100)


		gameDisplay.blit(background,(0,0))
		score(blood,goal)
		mario_display(mario_x,mario_y)
		goomba_display(goomba_x,goomba_y)
		mushroom_display(mushroom_x,mushroom_y)
		pygame.display.update()
		
		if blood == 0 :
			die()
			break;
			
		clock.tick(60)

### end gameloop()

if __name__ == '__main__':
	while True:
		gameloop()
	pygame.quit()
	quit()