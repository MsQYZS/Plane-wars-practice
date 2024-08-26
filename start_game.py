import pygame
from json import load,dumps
from os import makedirs,path
from player import Player
from zidan import Zidan
from guai1 import Guai1
from guai2 import Guai2
from guai3 import Guai3
from guai4 import Guai4
from score import Score
from creation_guai import creation
from guai1zidan import Guai1_Zidan
from guai2zidan import Guai2_Zidan
from guai3zidan import Guai3_Zidan
from mp3_music import Music
from hp import Hp
class Main_game:
	def __init__(self):
		pygame.init()
		self.screen_fliename='_internal\\Image\\7.jpeg'
		self.screen=pygame.display.set_mode((1520,800),pygame.FULLSCREEN)#pygame.FULLSCREEN
		self.screen_image=pygame.image.load(self.screen_fliename)
		pygame.display.set_caption("清羽&浊思")
		self.player_hp=3  #可修改玩家血量
		self.player=Player(self,self.player_hp)
		self.zidans=pygame.sprite.Group()
		self.guais1=pygame.sprite.Group()
		self.guai1_zidans=pygame.sprite.Group()
		self.guai2_zidans=pygame.sprite.Group()
		self.guai3_zidans=pygame.sprite.Group()
		self.guais2=pygame.sprite.Group()
		self.guais3=pygame.sprite.Group()
		self.guais4=pygame.sprite.Group()
		self.music=Music()
		self.screen_rect=self.screen.get_rect()
		self.score=Score(self)
		self.player_hp_draw=Hp(self,self.player.hp,40,750,150,30,3)
		self.stop=True
		self.fps=420	#可设置总体FPS
		self.init_fps=self.fps
		self.max_guai=6  #可设置最大出怪量
		self.guai1_fps=840		#怪物1的攻击频率
		self.guai2_fps=840
		self.guai3_fps=840
		self.init_guai1_fps=self.guai1_fps
		self.init_guai2_fps=self.guai2_fps
		self.init_guai3_fps=self.guai3_fps
		self.dis_fin_score=False
	def run(self):
		while self.fps>=0:
			while self.stop:
				self._stop_screen()
				self._check_events()
			while not self.stop:
				self._check_events()
				self._update_zidan()
				self._creation_guai()
				self._update_guai()
				self._creation_guai_zidan()
				self._update_player_hp()
				self._update_screen()
				self._fps_timer()
	def _fps_timer(self):
		self.fps-=1
		self.guai1_fps-=1
		self.guai2_fps-=1
		self.guai3_fps-=1
		if self.fps==0:
			self.fps=self.init_fps
	def _check_events(self):
		for event in pygame.event.get():
			if event.type==pygame.QUIT or \
			event.type==pygame.MOUSEBUTTONUP \
			and 580<=event.pos[0]<=940 \
			and 580<=event.pos[1]<=620 and self.stop:
				pygame.quit()
			elif event.type==pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type==pygame.KEYUP:
				self._check_keyup_events(event)
			if event.type==pygame.MOUSEBUTTONUP \
			and 680<=event.pos[0]<=840 \
			and 380<=event.pos[1]<=420 :
				self.stop=False
	def _check_keydown_events(self,event):
		if self.player_hp_draw.hp>0 and not self.stop:
			if event.key==pygame.K_d:
				self.player.moveing_right=True
			if event.key==pygame.K_a:
				self.player.moveing_left=True
			if event.key==pygame.K_w:
				self.player.moveing_up=True
			if event.key==pygame.K_s:
				self.player.moveing_down=True
			if event.key==pygame.K_j:
				if len(self.zidans)<3:
					new_zidan=Zidan(self)
					self.music.player()
					self.zidans.add(new_zidan)
		if event.key==pygame.K_ESCAPE:
			pygame.quit()
	def _check_keyup_events(self,event):
		if not self.stop:
			if event.key==pygame.K_d:
				self.player.moveing_right=False
			if event.key==pygame.K_a:
				self.player.moveing_left=False
			if event.key==pygame.K_w:
				self.player.moveing_up=False
			if event.key==pygame.K_s:
				self.player.moveing_down=False
		if event.key==pygame.K_r:
			if self.player_hp_draw.hp==0:
				self.player_hp_draw.hp=self.player_hp
				self.player_hp_draw._meta_update()
				self.player_hp_draw.blitme()
				self.guais1.empty()
				self.guais2.empty()
				self.guais3.empty()
				self.guais4.empty()
				self.guai1_zidans.empty()
				self.guai2_zidans.empty()
				self.guai3_zidans.empty()
				self.score.clear()
				del self.player
				self.player=Player(self,self.player_hp)
				self.dis_fin_score=False
	def _update_zidan(self):
		self.zidans.update()
		for zidan_s in self.zidans.copy():
			if zidan_s.rect not in self.screen_rect:
				self.zidans.remove(zidan_s)
	def _creation_guai(self):
		while len(self.guais1)+len(self.guais2)+len(self.guais3)+len(self.guais4)<self.max_guai:
			new_guai_color=creation()
			if new_guai_color[0]=="绿色":
				new_guai=Guai1(self)
				self.guais1.add(new_guai)
			elif new_guai_color[0]=="蓝色":
				new_guai=Guai2(self)
				self.guais2.add(new_guai)
			elif new_guai_color[0]=="黄色":
				new_guai=Guai3(self)
				self.guais3.add(new_guai)
			elif new_guai_color[0]=="红色":
				new_guai=Guai4(self)
				self.guais4.add(new_guai)#添加怪到组guais
	def _update_guai(self):
		self._update_guai1()
		self._update_guai2()
		self._update_guai3()
		self._update_guai4()
	def _update_guai1(self):
		for guai_1 in self.guais1.copy():	#抄书的，不懂copy和不copy的区别，毕竟结果好像一样。。。
			if guai_1.rect.y>=self.screen_rect.bottom:	#碰到屏幕低端后移除怪
				self.guais1.remove(guai_1)
			if pygame.sprite.groupcollide(self.zidans,self.guais1,1,1):
				self.score.update1()
		self.guais1.update()
	def _update_guai2(self):
		for guai_2 in self.guais2.copy():
			if guai_2.rect.y>=self.screen_rect.bottom:	#碰到屏幕低端后移除怪
				self.guais2.remove(guai_2)
			if pygame.sprite.groupcollide(self.zidans,self.guais2,1,1):
				self.score.update2()
		self.guais2.update()
	def _update_guai3(self):
		for guai_3 in self.guais3.copy():
			if guai_3.rect.y>=self.screen_rect.bottom:	#碰到屏幕低端后移除怪
				self.guais3.remove(guai_3)
			if pygame.sprite.groupcollide(self.zidans,self.guais3,1,1):
				self.score.update3()
		self.guais3.update()
	def _update_guai4(self):
		for guai_4 in self.guais4.copy():
			if guai_4.rect.y>=self.screen_rect.bottom:	#碰到屏幕低端后移除怪
				self.guais4.remove(guai_4)
			if pygame.sprite.groupcollide(self.zidans,self.guais4,1,1):
				self.score.update4()
				self.player_hp_draw.update_add()
		self.guais4.update()
	def _creation_guai_zidan(self):
		self._creation_guai1_zidan()
		self._update_guai1_zidan()
		self._creation_guai2_zidan()
		self._update_guai2_zidan()
		self._creation_guai3_zidan()
		self._update_guai3_zidan()
	def _update_player_hp(self):
		if self.dis_fin_score==False:
			if self.player_hp_draw.hp>1:
				if pygame.sprite.spritecollide(self.player,self.guai1_zidans,1) or\
				pygame.sprite.spritecollide(self.player,self.guai2_zidans,1) or\
				pygame.sprite.spritecollide(self.player,self.guai3_zidans,1):
					self.player_hp_draw.update()
			if self.player_hp_draw.hp==1:
				if pygame.sprite.spritecollide(self.player,self.guai1_zidans,0):
					self.player.update_dead()
					self.player_hp_draw.update()
					pygame.sprite.spritecollide(self.player,self.guai1_zidans,1)
				if pygame.sprite.spritecollide(self.player,self.guai2_zidans,0):
					self.player.update_dead()
					self.player_hp_draw.update()
					pygame.sprite.spritecollide(self.player,self.guai2_zidans,1)
				if pygame.sprite.spritecollide(self.player,self.guai3_zidans,0):
					self.player.update_dead()
					self.player_hp_draw.update()
					pygame.sprite.spritecollide(self.player,self.guai3_zidans,1)
			elif self.player_hp_draw.hp==0:
				self._show_fin_score()
	def _show_fin_score(self):
		self.set_finaly_score_rect=(510,250)
		self.font=pygame.font.SysFont('华文隶书',90)
		self.font_1=pygame.font.SysFont('ink free',100)
		self.font_2=pygame.font.SysFont("ink free",60)
		self.font_3=pygame.font.SysFont('华文彩云',50)
		self.font6=self.font.render("游戏结束了~",True,(170,125,25))
		self.font3=self.font.render("你的分数是",True,(100,255,255))
		self.font4=self.font_1.render(str(self.score.score),True,(250,255,0))
		self.font7=self.font_3.render("按r重新开始",True,(42,13,191))
		self.font8=self.font_3.render("按ESC退出",True,(255,1,1))
		self.screen.blit(self.font3,self.set_finaly_score_rect)
		self.screen.blit(self.font4,(self.set_finaly_score_rect[0]+200,self.set_finaly_score_rect[1]+120))
		self.screen.blit(self.font6,(self.set_finaly_score_rect[0],self.set_finaly_score_rect[1]-150))
		self.screen.blit(self.font7,(self.set_finaly_score_rect[0]+100,self.set_finaly_score_rect[1]+300))
		self.screen.blit(self.font8,(self.set_finaly_score_rect[0]+120,self.set_finaly_score_rect[1]+420))
		i_L=[self.score.score]
		try:
			with open("_internal\\PlayerScore\\score_list.json",'r',encoding="UTF-8") as score_:
				i1=load(score_)
				for h in i1.values():
					for n in h:
						i_L.append(n)
			with open("_internal\\PlayerScore\\score_list.json",'w',encoding="UTF-8") as score:
				score={'score':i_L}
				s_json=dumps(score,ensure_ascii=False,indent=4,separators=(',',':'))
				score.write(s_json)
		except :
			score={'score':i_L}
			s_json=dumps(score,ensure_ascii=False,indent=4,separators=(',',':'))
			with open("_internal\\PlayerScore\\score_list.json",'w',encoding="UTF-8") as score:
				score.write(s_json)
		finally:
				i_L.sort(reverse=True)
				if len(i_L)<=9:
					for i in range(len(i_L)):
						locals()[f"self.font_list{i}"]=\
						self.font_2.render\
						(str(i_L[i]),True,(255,0,200))
						self.screen.blit\
						(locals()[f"self.font_list{i}"],\
							(self.set_finaly_score_rect[0]+630,\
								self.set_finaly_score_rect[1]-200+70*i))
				else:
					for i in range(10):
						locals()[f"self.font_list{i}"]=\
						self.font_2.render\
						(str(i_L[i]),True,(255,0,200))
						self.screen.blit\
						(locals()[f"self.font_list{i}"],\
							(self.set_finaly_score_rect[0]+630,\
								self.set_finaly_score_rect[1]-200+70*i))
		self.font=pygame.font.SysFont('华文隶书',30)
		self.font5=self.font.render("历史最高前十分为:",True,(0,255,72))
		self.screen.blit\
		(self.font5,(self.set_finaly_score_rect[0]+550,\
			self.set_finaly_score_rect[1]-230))
		self.dis_fin_score=True
	def _creation_guai1_zidan(self):
		if self.guai1_fps==0:
			for guai1_rect in self.guais1:
				guai1_zidan=Guai1_Zidan(self,guai1_rect.rect)
				self.guai1_zidans.add(guai1_zidan)
			self.guai1_fps=self.init_guai1_fps
	def _creation_guai2_zidan(self):
		if self.guai2_fps==200:
			for guai2_rect in self.guais2:
				guai2_zidan=Guai2_Zidan(self,guai2_rect.rect)
				self.guai2_zidans.add(guai2_zidan)
			self.guai2_fps=self.init_guai2_fps
	def _creation_guai3_zidan(self):
		if self.guai3_fps==420:
			for guai3_rect in self.guais3:
				for i in range(4):
					guai3_zidan=Guai3_Zidan(self,guai3_rect.rect,i)
					self.guai3_zidans.add(guai3_zidan)
			self.guai3_fps=self.init_guai3_fps
	def _update_guai1_zidan(self):
		self.guai1_zidans.update()
		for guai1_zidan in self.guai1_zidans.copy():
			if guai1_zidan.rect not in self.screen_rect:
				self.guai1_zidans.remove(guai1_zidan)
	def _update_guai2_zidan(self):
		self.guai2_zidans.update()
		for guai2_zidan in self.guai2_zidans.copy():
			if guai2_zidan.rect not in self.screen_rect:
				self.guai2_zidans.remove(guai2_zidan)
	def _update_guai3_zidan(self):
		self.guai3_zidans.update()
		for guai3_zidan in self.guai3_zidans.copy():
			if guai3_zidan.rect not in self.screen_rect:
				self.guai3_zidans.remove(guai3_zidan)
	def _blitme_guai_zidan(self):
		self._blitme_guai1_zidan()
		self._blitme_guai2_zidan()
		self._blitme_guai3_zidan()
	def _blitme_guai1_zidan(self):
		for guai1_zidan in self.guai1_zidans.sprites():
			guai1_zidan.blitme()
	def _blitme_guai2_zidan(self):
		for guai2_zidan in self.guai2_zidans.sprites():
			guai2_zidan.blitme()
	def _blitme_guai3_zidan(self):
		for guai3_zidan in self.guai3_zidans.sprites():
			guai3_zidan.blitme()
	def _update_screen(self):
		if self.dis_fin_score==False:
			self.screen.blit(self.screen_image,(0,0))
			self.player.update()
			self.player.blitme()
			for guai in self.guais1.sprites():
				guai.blitme()
			for guai in self.guais2.sprites():
				guai.blitme()
			for guai in self.guais3.sprites():
				guai.blitme()
			for guai in self.guais4.sprites():
				guai.blitme()
			for zidan in self.zidans.sprites():
				zidan.blitme()
			self.score.blitme()
			self.player_hp_draw.blitme()
			self._blitme_guai_zidan()
		pygame.display.update()
	def _stop_screen(self):
		self.set_start_rect=(680,380)
		self.set_quit_rect=(580,580)
		fliename='_internal\\Image\\9.jpg'
		screen_image=pygame.image.load(fliename)
		self.screen.blit(screen_image,(0,0))
		self.font=pygame.font.SysFont('寒蝉点阵体',40)
		self.font1=self.font.render("开始游戏",True,(0,255,0))
		self.font2=self.font.render("退出游戏，或按ESC",True,(0,255,0))
		start_botton_rect=pygame.draw.rect(self.screen,(255,255,0),(self.set_start_rect,(160,40)),3)
		self.screen.blit(self.font1,self.set_start_rect)
		self.screen.blit(self.font2,self.set_quit_rect)
		quit_botton_rect=pygame.draw.rect(self.screen,(0,255,255),(self.set_quit_rect,(360,40)),3)
		pygame.display.update()
if __name__=="__main__":
	def makefile(file_name):
		if not path.exists(file_name):
			makedirs(file_name)
		else:
			pass
	makefile('_internal\\PlayerScore')
	ai=Main_game()
	ai.run()