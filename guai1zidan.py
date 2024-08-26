from pygame import image
from pygame.sprite import Sprite
class Guai1_Zidan(Sprite):
	def __init__(self,ai_game,guai1_rect):
		super().__init__()
		self.screen=ai_game.screen
		self.image=image.load("_internal\\Image\\怪子弹1.png")
		self.rect=self.image.get_rect()
		self.rect.x=guai1_rect.midbottom[0]
		self.rect.y=guai1_rect.midbottom[1]
		self.speed=0.8
	def update(self):
			self.rect.y=self.rect.y+float(self.speed)
	def blitme(self):
		self.screen.blit(self.image,self.rect)