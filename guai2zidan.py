from pygame import image
from pygame.sprite import Sprite
class Guai2_Zidan(Sprite):
	def __init__(self,ai_game,guai2_rect):
		super().__init__()
		self.screen=ai_game.screen
		self.image=image.load("_internal\\Image\\怪子弹2.png")
		self.rect=self.image.get_rect()
		self.player_rect_x=ai_game.player.rect.x+25
		self.player_rect_y=ai_game.player.rect.y+25
		self.rect.midbottom=guai2_rect.midbottom#ZeroDivisionError
		self.rect.x=guai2_rect.midbottom[0]
		self.rect.y=guai2_rect.midbottom[1]
		self.x=float(self.rect.x)
		self.y=float(self.rect.y)
		self.init_x=self.x
		self.init_y=self.y
		self.speed=0.6		#可设置怪1的子弹速度
		self.long_x=abs(((self.init_x-self.player_rect_x)**2+\
					(self.init_y-self.player_rect_y)**2)**0.5)
		try:
			self.k=float((self.player_rect_y-self.y)/  \
					(self.player_rect_x-self.x))
			self.b=float(self.y-self.x*self.k)
		except ZeroDivisionError:
			self.k="error"
			self.b=float(self.player_rect_y-self.y)
		try:
			self.slow_y=abs(self.init_y-self.player_rect_y)*self.speed/self.long_x
		except ZeroDivisionError:
			self.slow_y=self.speed
	def update(self):
		if self.k!=0 and self.k!="error":
			if self.init_y<self.player_rect_y:
				self.y+=self.slow_y
				self.x=(self.y-self.b)/self.k
				self.rect.x=self.x
				self.rect.y=self.y
			elif self.init_y>self.player_rect_y:
				self.y-=self.slow_y
				self.x=(self.y-self.b)/self.k
				self.rect.x=self.x
				self.rect.y=self.y
		elif self.k=="error":
			self.y+=self.speed
			self.rect.y=self.y
		elif self.k==0:
			self.x+=self.speed
			self.rect.x=self.x
	def blitme(self):
		self.screen.blit(self.image,self.rect)