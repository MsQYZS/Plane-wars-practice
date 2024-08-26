from pygame.sprite import Sprite
from pygame import image
from random import uniform
class Guai4(Sprite):
	def __init__(self,ai_game):
		super().__init__()
		self.color="红色"
		self.screen=ai_game.screen
		self.screen_rect=ai_game.screen.get_rect()
		self.scores=50
		self.speed=1.1
		self.image=image.load("_internal\\Image\\Diamond2.png")
		self.rect=self.image.get_rect()
		self.rect.x=float(uniform(0,self.screen_rect.width))-self.rect.width
		self.rect.y=float(uniform(-200,0))
		self.y=float(self.rect.y)
	def update(self):
		self.y+=self.speed
		self.rect.y=self.y
	def blitme(self):
		self.screen.blit(self.image,self.rect)