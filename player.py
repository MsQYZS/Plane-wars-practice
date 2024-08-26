from pygame import image
import time
class Player:
	def __init__(self,ai_game,hp):
		self.screen=ai_game.screen
		self.screen_rect=ai_game.screen.get_rect()
		self.image=image.load("_internal\\Image\\Angry_Bords_Running_Red_Bird1.png")
		self.rect=self.image.get_rect()
		self.rect.midbottom=self.screen_rect.midbottom
		self.moveing_right=False
		self.moveing_left=False
		self.moveing_up=False
		self.moveing_down=False
		self.speed=1
		self.hp=hp
	def blitme(self):
		self.screen.blit(self.image,self.rect)
	def update(self):
		if self.moveing_right and self.rect.right<self.screen_rect.right:
			self.rect.x+=self.speed
		if self.moveing_left and self.rect.left>self.screen_rect.left:
			self.rect.x-=self.speed
		if self.moveing_up and self.rect.top>self.screen_rect.top:
			self.rect.y-=self.speed
		if self.moveing_down and self.rect.bottom<self.screen_rect.bottom:
			self.rect.y+=self.speed
	def update_dead(self):
		self.imgae_dead=image.load("_internal\\Image\\12(1).png")
		self.image=self.imgae_dead
		time.sleep(1)