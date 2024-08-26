#输入血量，初始rect（（x,x），（x,x）），厚度
from pygame import draw
class Hp:
	def __init__(self,ai_game,how_hp,rect_x,rect_y,rect_width,rect_height,rect_thick):
		self.hp=how_hp
		try :
			self.percentage_hp=float(1/self.hp)
		except ZeroDivisionError:
			self.percentage_hp=0
		self.rect_x=rect_x
		self.rect_y=rect_y
		self.rect_width=rect_width
		self.rect_height=rect_height
		self.rect_thick=rect_thick
		self.init_rect=((self.rect_x,self.rect_y),(self.rect_width,self.rect_height))
		self.hp_rect=((self.rect_x+rect_thick,self.rect_y+rect_thick),(self.rect_width-rect_thick*2,self.rect_height-rect_thick*2))
		self.screen=ai_game.screen
		self.color=(255,0,0)
	def update(self):
		self._hp_update()
		self._meta_update()
	def update_add(self):
		if 1<=self.hp<3:
			self.hp=self.hp+1
		self._meta_update()
	def _hp_update(self):
		self.hp=self.hp-1
	def _meta_update(self):
		self.rect_xy=(self.rect_x+self.rect_thick,self.rect_y+self.rect_thick)
		self.hp_rect_width=(self.rect_width-self.rect_thick*2)*self.percentage_hp*self.hp
		self.hp_rect_height=self.rect_height-self.rect_thick*2
		self.hp_rect=(self.rect_xy,(self.hp_rect_width,self.hp_rect_height))
	def blitme(self):
		draw.rect(self.screen,(0,0,0),self.init_rect,self.rect_thick)
		draw.rect(self.screen,self.color,self.hp_rect)