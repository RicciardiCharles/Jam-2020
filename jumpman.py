import pygame
from pygame.locals import *
from pygame_functions import *
import os, sys
import time

def jumpman_game():
	pygame.init()

	clock = pygame.time.Clock()
	fps = 60

	screen_width = 1920
	screen_height = 1080

	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption('Platformer')

	#define game variables
	tile_size = 55
	game_over = 0
	count_jump = 0
	maximator = 0
	fly = 0
	guymaximator = 0
	win = 0

	#load images
	sun_img = pygame.image.load('img/sun.png')
	bg_img = pygame.image.load('img/sky.png')
	restart_img = pygame.image.load('img/restart_btn.png')
	exit_img = pygame.image.load('img/exit_btn.png')
	win_img = pygame.image.load('img/win.png')


	class Button():
		def __init__(self, x, y, image):
			self.image = image
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y
			self.clicked = False

		def draw(self):
			action = False

			#get mouse position
			pos = pygame.mouse.get_pos()

			#check mouseover and clicked conditions
			if self.rect.collidepoint(pos):
				if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
					action = True
					self.clicked = True

			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False


			#draw button
			screen.blit(self.image, self.rect)

			return action


	class Player():
		def __init__(self, x, y, guymaximator):
			self.reset(x, y, guymaximator)



		def update(self, game_over, count_jump, maximator, fly, guymaximator, win):
			dx = 0
			dy = 0
			walk_cooldown = 5

			if game_over == 0:
				#get keypresses
				key = pygame.key.get_pressed()
				if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
					self.vel_y = -15
					self.jumped = True
					count_jump = 0
				if maximator == 1:
					if self.in_air == True and self.jumped == False and key[pygame.K_SPACE] and count_jump == 0:
						self.vel_y = -15
						count_jump = 1
				if fly == 1:
					if self.in_air == True and self.jumped == False and key[pygame.K_SPACE]:
						self.vel_y = -15
				if key[pygame.K_SPACE] == False:
					self.jumped = False
				if key[pygame.K_LEFT]:
					dx -= 15
					self.counter += 1
					self.direction = -1
				if key[pygame.K_RIGHT]:
					dx += 15
					self.counter += 1
					self.direction = 1
				if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
					self.counter = 0
					self.index = 0
					if self.direction == 1:
						self.image = self.images_right[self.index]
					if self.direction == -1:
						self.image = self.images_left[self.index]


				#handle animation
				if self.counter > walk_cooldown:
					self.counter = 0	
					self.index += 1
					if self.index >= len(self.images_right):
						self.index = 0
					if self.direction == 1:
						self.image = self.images_right[self.index]
					if self.direction == -1:
						self.image = self.images_left[self.index]


				#add gravity
				self.vel_y += 1.5
				# if self.vel_y > 10:
				# 	self.vel_y = 10
				dy += self.vel_y

				#check for collision
				self.in_air = True
				for tile in world.tile_list:
					#check for collision in x direction
					if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
						dx = 0
					#check for collision in y direction
					if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
						#check if below the ground i.e. jumping
						if self.vel_y < 0:
							dy = tile[1].bottom - self.rect.top
							self.vel_y = 0
						#check if above the ground i.e. falling
						elif self.vel_y >= 0:
							dy = tile[1].top - self.rect.bottom
							self.vel_y = 0
							self.in_air = False


				#check for collision with enemies
				if pygame.sprite.spritecollide(self, blob_group, False):
					game_over = -1

				#check if character goes over map
				if dy > 50:
					game_over = -1

				#check for collision with lava
				if pygame.sprite.spritecollide(self, lava_group, False):
					game_over = -1

				#check if character drinks maximator
				if pygame.sprite.spritecollide(self, fake_dirt_maximator_group, False):
					maximator = 1
					guymaximator = 1
					player.reset(60, screen_height - 330, guymaximator)

				#check if character reach the CHOUFFE GANG
				if pygame.sprite.spritecollide(self, final_groupe, False):
					win = 1

				#check if character try to be a lopette
				if pygame.sprite.spritecollide(self, fake_final_groupe, False):
					game_over = -1


				#update player coordinates
				self.rect.x += dx
				self.rect.y += dy


			elif game_over == -1:
				self.image = self.dead_image
				if self.rect.y > 200:
					self.rect.y -= 5

			#draw player onto screen
			screen.blit(self.image, self.rect)
			# pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

			return (game_over, count_jump, maximator, guymaximator, win)


		def reset(self, x, y, guymaximator):
			self.images_right = []
			self.images_left = []
			self.index = 0
			self.counter = 0
			for num in range(1, 5):
				if (guymaximator == 1):
					img_right = pygame.image.load(f'img/guy{num}_maximated.png')
				if (guymaximator == 0):
					img_right = pygame.image.load(f'img/guy{num}.png')
				img_right = pygame.transform.scale(img_right, (40, 80))
				img_left = pygame.transform.flip(img_right, True, False)
				self.images_right.append(img_right)
				self.images_left.append(img_left)
			self.dead_image = pygame.image.load('img/KO.png')
			self.image = self.images_right[self.index]
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y
			self.width = self.image.get_width()
			self.height = self.image.get_height()
			self.vel_y = 0
			self.jumped = False
			self.direction = 0
			self.in_air = True



	class World():
		def __init__(self, data):
			self.tile_list = []

			#load images
			dirt_img = pygame.image.load('img/dirt.png')
			grass_img = pygame.image.load('img/grass.png')
			invisible_block_img = pygame.image.load('img/invisible_block.png')

			row_count = 0
			for row in data:
				col_count = 0
				for tile in row:
					if tile == 1:
						img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
						img_rect = img.get_rect()
						img_rect.x = col_count * tile_size
						img_rect.y = row_count * tile_size
						tile = (img, img_rect)
						self.tile_list.append(tile)
					if tile == 2:
						img = pygame.transform.scale(grass_img, (tile_size, tile_size))
						img_rect = img.get_rect()
						img_rect.x = col_count * tile_size
						img_rect.y = row_count * tile_size
						tile = (img, img_rect)
						self.tile_list.append(tile)
					if tile == 8:
						img = pygame.transform.scale(invisible_block_img, (tile_size, tile_size))
						img_rect = img.get_rect()
						img_rect.x = col_count * tile_size
						img_rect.y = row_count * tile_size
						tile = (img, img_rect)
						self.tile_list.append(tile)
					if tile == 7:
						final_var = final(col_count * tile_size, row_count * tile_size)
						final_groupe.add(final_var)
					if tile == 9:
						fake_final_var = fake_final(col_count * tile_size, row_count * tile_size)
						fake_final_groupe.add(fake_final_var)	
					if tile == 4:
						fake_dirt_var = fake_dirt(col_count * tile_size, row_count * tile_size)
						fake_dirt_group.add(fake_dirt_var)
					if tile == 5:
						fake_dirt_maximator_var = fake_dirt_maximator(col_count * tile_size, row_count * tile_size)
						fake_dirt_maximator_group.add(fake_dirt_maximator_var)
					if tile == 3:
						blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
						blob_group.add(blob)
					if tile == 6:
						lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
						lava_group.add(lava)

					col_count += 1
				row_count += 1

		def draw(self):
			for tile in self.tile_list:
				screen.blit(tile[0], tile[1])
				# pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

	class Enemy(pygame.sprite.Sprite):
		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load('img/blob2.png')
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y + 3
			self.move_direction = 1
			self.move_counter = 0

		def update(self):
			self.rect.x += self.move_direction
			self.move_counter += 1
			if abs(self.move_counter) > 50:
				self.move_direction *= -1
				self.move_counter *= -1

	class fake_dirt(pygame.sprite.Sprite):
		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			img = pygame.image.load('img/dirt.png')
			self.image = pygame.transform.scale(img, (tile_size, tile_size))
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y

	class final(pygame.sprite.Sprite):
		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			img = pygame.image.load('img/final.png')
			self.image = pygame.transform.scale(img, (tile_size, tile_size))
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y

	class fake_final(pygame.sprite.Sprite):
		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			img = pygame.image.load('img/fake_final.png')
			self.image = pygame.transform.scale(img, (40, 100))
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y - 45

	class fake_dirt_maximator(pygame.sprite.Sprite):
		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			img = pygame.image.load('img/dirt.png')
			self.image = pygame.transform.scale(img, (tile_size, tile_size))
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y

	class Lava(pygame.sprite.Sprite):
		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			
			for num in range(1, 11):
				img = pygame.image.load(f'img/lava/lava{num}.png')
			self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y + 1
			self.move_direction = 1
			self.move_counter = 0
			
		

	world_data = [
	[1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1], 
	[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
	[1, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 7, 1, 1, 1], 
	[1, 0, 0, 2, 1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1], 
	[1, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
	[1, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
	[1, 1, 2, 2, 2, 2, 1, 0, 0, 0, 3, 0, 3, 0, 0, 0, 2, 0, 1, 0, 1, 2, 2, 6, 6, 6, 2, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
	[4, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 4, 4, 1], 
	[5, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 4, 4, 1], 
	[1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 1], 
	[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 4, 1], 
	[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 2, 1, 1, 4, 1], 
	[1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 1, 1, 1, 4, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 2, 6, 6, 6, 6, 6, 6, 2, 1, 1, 1, 1, 0, 0, 1, 1, 1, 4, 1], 
	[1, 2, 6, 6, 6, 6, 2, 6, 6, 6, 6, 6, 2, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 4, 4, 4, 1], 
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 1], 
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 9, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]

	player = Player(70, screen_height - 330, guymaximator)

	blob_group = pygame.sprite.Group()
	lava_group = pygame.sprite.Group()
	fake_dirt_group = pygame.sprite.Group()
	fake_dirt_maximator_group = pygame.sprite.Group()
	final_groupe = pygame.sprite.Group()
	fake_final_groupe = pygame.sprite.Group()

	world = World(world_data)

	#create buttons for restart
	restart_button = Button(screen_width // 2 - 350, screen_height // 2 + 100, restart_img)

	#create buttons for exit
	exit_button = Button(screen_width // 2 + 350, screen_height // 2 + 100, exit_img)

	run = True
	while run:

		clock.tick(fps)

		screen.blit(bg_img, (0, 0))
		screen.blit(sun_img, (250, 50))

		world.draw()

		if game_over == 0:
			blob_group.update()
		lava_group.update()
		

		#cheat code for double jump permanently
		# maximator = 1

		#cheat code for fly
		# fly = 1

		blob_group.draw(screen)
		lava_group.draw(screen)
		fake_dirt_group.draw(screen)
		fake_dirt_maximator_group.draw(screen)
		final_groupe.draw(screen)
		fake_final_groupe.draw(screen)

		tmp = player.update(game_over, count_jump, maximator, fly, guymaximator, win)
		game_over = tmp[0]
		count_jump = tmp[1]
		maximator = tmp[2]
		guymaximator = tmp[3]
		win = tmp[4]
		
		if (win == 1):
			screen.blit(win_img, (500, 300))
			if exit_button.draw():
				run = False
				return (1)

		#if player has died
		if game_over == -1:
			if restart_button.draw():
				player.reset(60, screen_height - 330, guymaximator)
				game_over = 0
				maximator = 0
				guymaximator = 0
			if exit_button.draw():
				run = False
				return (0)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()

	pygame.quit()