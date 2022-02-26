from random import randint as rd, choice as ch
from os import system as sys
import pygame
from math import *
from os.path import abspath as tdir



class Green():

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.is_atk = False
		self.color = (0, 255, 0)
		self.pos = (self.x, self.y, 10, 10)
		self.is_dead = False

	def go(self, users):
		for user in users:
			if (user.x == self.x)&(user.y == self.y)&(user.tar_x == self.x)&(user.tar_y == self.y):
				self.is_atk = True
				self.dead = True
				self.color = (0,0,0)
				break



class Red():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.is_mutate = False
		self.speed = 10
		self.tar_num = None
		self.tar_x = None
		self.tar_y = None
		self.dead = False
		self.heals = 100
		self.none_cikl = 0
		self.color = (255, 0, 0)
		self.old_pos = (0,0, 10, 10)
		self.pos = (self.x, self.y, 10, 10)

	def go(self):
		if self.none_cikl >= 100:
			self.heals = 0
		if self.pos == self.old_pos:
			self.none_cikl += 1
		else:
			self.none_cikl = 0
		self.old_pos = self.pos
		self.heals -= 1
		if self.heals > 0:
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
						self.heals += 10
						if self.heals > 150:
							self.heals = 150
						self.tar_x = None
						self.tar_y = None
		else:
			self.color = (255, 255, 255)
			self.dead = True
		
		self.pos = (self.x, self.y, 10, 10)



def db():
	file = open(f'{tdir(__file__)}/data.txt'.replace('\\', '/').replace('main.py/', ''), 'r', encoding = 'utf-8')
	k = file.read().split(' ')
	file.close()
	return int(k[0])



def re_db(k):
	file = open(f'{tdir(__file__)}/data.txt'.replace('\\', '/').replace('main.py/', ''), 'w', encoding = 'utf-8')
	file.write(k)
	file.close()



sc = pygame.display.set_mode((1500, 900))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
FPS = 75
mln = 10000000
num = 0

r = 50

reds = []
for i in range(r):
	reds.append(Red(rd(0, 149)*10, rd(0, 89)*10))



def check_red():
	global reds
	if [x for x in reds if x.dead == False]:
		return True
	else:
		return False



greens = []
def get_greens():
	global greens, Green
	greens = []
	mas = [(0,0)]
	for i in range(500):
		x = rd(0, 149)*10
		y = rd(0, 89)*10
		if (x,y) in mas:
			while (x, y) in mas:
				x = rd(0, 149)*10
				y = rd(0, 89)*10
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



def search_eat(greens, reds):
	global mln, num
	x1 = greens[i].x # x и y цели
	y1 = greens[i].y
	x2 = reds[user_num].x # x и y хищника
	y2 = reds[user_num].y

	# нужно сравнить расстояние от цели до хищника
	l1 = max(x1,x2)-min(x1,x2)
	l2 = max(y1,y2)-min(y1,y2)
	ln = sqrt(l1**2 + l2**2)

	if ln<mln:
		mln = ln
		num = i



def mutate():
	global reds
	speeds = (1, 2, 5, 10)
	for i in range(3):
		k = rd(0, len(reds))
		if reds[k].is_mutate == False:
			reds[k].speed = ch(speeds)
			reds[k].is_mutate = True



simulation = 0
flag = True
cikl = 0
running = True
while running:
	if check_red():
		clock.tick(FPS)
		if check_go(greens) == False:
			get_greens()
			for user in reds:
				user.tar_x = None
				user.tar_y = None
			reds = [x for x in reds if x.dead == False]
			#mutate()
			cikl += 1
			sys('cls')
			print(cikl)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		sc.fill((0,0,0))
		k = [x.tar_num for x in reds if x.dead == True] # позволяем выбирать цели мертвых красных
		for i in k:
			greens[i].is_atk = False

		if check_greens(greens, reds):
			for user_num in range(len(reds)):
				if (reds[user_num].tar_x == None): # если нужна новая цель

					for git in greens:
						if git.is_atk == False:
							flag = True
							break

					if flag: # если есть свободные цели
						mln = 1000000
						for i in range(len(greens)):
							
							if (greens[i].is_atk == False): # если цель свободна
								search_eat(greens, reds)

						reds[user_num].tar_x = greens[num].x
						reds[user_num].tar_y = greens[num].y
						reds[user_num].tar_num = num
						greens[num].is_atk = True
						#print('Найдена новая цель с id: ' + str(num) + ' heals: ' + str(reds[user_num].heals))
						mln = 0
						ln = 0

				reds[user_num].go()
				pygame.draw.circle(sc, reds[user_num].color, (reds[user_num].pos[0], reds[user_num].pos[1]), 5)


			for i in range(len(greens)):
				greens[i].go(reds)
				for user in reds:
					if (user.x == greens[i].x)&(user.y == greens[i].y):
						greens[i].is_dead = True
				if not(greens[i].is_dead):
					pygame.draw.circle(sc, greens[i].color, (greens[i].pos[0], greens[i].pos[1]), 5)

			pygame.display.update()
	else:
		reds = []
		for i in range(r):
			reds.append(Red(rd(0, 149)*10, rd(0, 89)*10))
		if cikl > db():
			re_db(str(cikl) + " " + str(simulation))
		get_greens()
		cikl = 0
		simulation += 1


pygame.quit()