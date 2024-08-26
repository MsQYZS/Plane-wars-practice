from pygame import image
from pygame.sprite import Sprite
class Guai3_Zidan(Sprite):
	def __init__(self,ai_game,guai3_rect,i):
		super().__init__()
		self.screen=ai_game.screen
		self.image=image.load("_internal\\Image\\怪子弹3.png")
		self.rect=self.image.get_rect()
		self.i=i
		self.speed=0.7 #可设置怪3的子弹速度
		if self.i==0:
			self.rect.x=float(guai3_rect.midbottom[0])-guai3_rect.width*1.5
			self.rect.y=float(guai3_rect.midbottom[1])
		if self.i==1:
			self.rect.x=float(guai3_rect.midbottom[0])+guai3_rect.width
			self.rect.y=float(guai3_rect.midbottom[1])
		if self.i==2:
			self.rect.x=float(guai3_rect.midbottom[0])-guai3_rect.width*0.2
			self.rect.y=float(guai3_rect.midbottom[1])
		if self.i==3:
			self.rect.x=float(guai3_rect.midbottom[0])+guai3_rect.width*0.2
			self.rect.y=float(guai3_rect.midbottom[1])
	def update(self):
		if self.i==0 or self.i==1:
			self.rect.y=self.rect.y+self.speed
		if self.i==2:
			self.rect.y=self.rect.y+float(self.speed)
			self.rect.x=self.rect.x-float(self.speed)
		if self.i==3:
			self.rect.y=self.rect.y+float(self.speed)
			self.rect.x=self.rect.x+float(self.speed)
	def blitme(self):
		self.screen.blit(self.image,self.rect)