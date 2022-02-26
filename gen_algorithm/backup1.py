from random import randint as rd, choice as ch
from os import system as sys
import pygame



class Green():

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.is_atk = False
		self.color = (0, 255, 0)
		self.pos = (self.x, self.y, 10, 10)
		self.type = 'green'
		self.is_dead = False

	def go(self, users):
		for user in users:
			if (user.x == self.x)&(user.y == self.y):
				self.is_atk = True
				self.color = (0,0,0)
				break



class Red():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.speed = 10
		self.tar_x = None
		self.tar_y = None
		self.color = (255, 0, 0)
		self.pos = (self.x, self.y, 10, 10)
		self.type = 'red'

	def go(self):
		if self.tar_x != None:
			if (self.tar_x != None)&(self.tar_y != None):
		
				if (self.x != self.tar_x)&(self.y != self.tar_y):
					var = rd(0,2)
					if var: # по х
						if self.x < self.tar_x:
							self.x += self.speed
						elif self.x > self.tar_x:
							self.x -= self.speed
					if not(var): # по y
						if self.y < self.tar_y:
							self.y += self.speed
						elif self.y > self.tar_y:
							self.y -= self.speed

				elif (self.x != self.tar_x):
					if self.x < self.tar_x:
						self.x += self.speed
					elif self.x > self.tar_x:
						self.x -= self.speed

				elif (self.y != self.tar_y):
					if self.y < self.tar_y:
						self.y += self.speed
					elif self.y > self.tar_y:
						self.y -= self.speed

				elif (self.x == self.tar_x)&(self.y == self.tar_y):
					self.tar_x = None
					self.tar_y = None
		
		self.pos = (self.x, self.y, 10, 10)
		


sc = pygame.display.set_mode((700, 500))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
FPS = 75



reds = []
for i in range(15):
	reds.append(Red(rd(0, 69)*10, rd(0, 49)*10))



def mutate():
	global reds
	k = (rd(0, 10), rd(0, 10), rd(0, 10),)
	for i in k:
		reds[i].speed = ch((1, 2, 5, 10))



greens = []
def get_greens():
	global greens, Green
	greens = []
	mas = [(0,0)]
	for i in range(1000):
		x = rd(0, 69) * 10
		y = rd(0, 49) * 10
		if (x,y) in mas:
			while (x, y) in mas:
				x = rd(0, 69) * 10
				y = rd(0, 49) * 10
		greens.append(Green(x,y))
get_greens()



def check_greens(greens, reds):
	flag = False
	flag2 = False
	for gre in greens:
		if gre.is_atk == False:
			flag = True
	for red in reds:
		if (red.x != red.tar_x) or (red.y != red.tar_y):
			flag2 = True
	if flag or flag2:
		return True
	else:
		return False



def check_go(greens):
	flag = False
	for i in greens:
		if i.is_dead == False:
			flag = True
	return flag == True



flag = True
cikl = 0
running = True
while running:
	clock.tick(FPS)
	if check_go(greens) == False:
		get_greens()
		mutate()
		cikl += 1
		sys('cls')
		print(cikl)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	sc.fill((0,0,0))

	if check_greens(greens, reds):
		for user_num in range(len(reds)):
			if (reds[user_num].tar_x == None):
				for git in greens:
					if git.is_atk == False:
						flag = True
						break
				if flag:
					for i in range(len(greens)):
						if (greens[i].is_atk == False):
							reds[user_num].tar_x = greens[i].x
							reds[user_num].tar_y = greens[i].y
							greens[i].is_atk = True
							break
				else:
					reds[user_num].tar_x = 340
					reds[user_num].tar_y = 240

			reds[user_num].go()
			pygame.draw.rect(sc, reds[user_num].color, reds[user_num].pos)


		for i in range(len(greens)):
			greens[i].go(reds)
			for user in reds:
				if (user.x == greens[i].x)&(user.y == greens[i].y):
					greens[i].is_dead = True
			if not(greens[i].is_dead):
				pygame.draw.rect(sc, greens[i].color, greens[i].pos)

		pygame.display.update()

pygame.quit()