from pygame import image
from pygame.sprite import Sprite
class Zidan(Sprite):
	def __init__(self,ai_game):
		super().__init__()
		self.screen=ai_game.screen
		self.image=image.load("_internal\\Image\\星星子弹.png")
		self.rect=self.image.get_rect()
		self.rect.midtop=ai_game.player.rect.midtop
		self.y=float(self.rect.y)
		self.speed=0.8
#内存消耗起飞~A1		self.ai_game_zidans=ai_game.zidans
	def update(self):
		self.y-=self.speed
		self.rect.y=self.y
#A2		for zidan_s in self.ai_game_zidans.copy():
#A3			if zidan_s.rect.y==0:
#A4				self.ai_game_zidans.remove(zidan_s)
	def blitme(self):
		self.screen.blit(self.image,self.rect)