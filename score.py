from pygame import font
class Score:
	def __init__(self,ai_game):
		self.score=0
		self.screen=ai_game.screen
		self.screen_rect=self.screen.get_rect()
		self.font=font.SysFont('寒蝉点阵体',40)
		self.scores=self.font.render(str(self.score),True,(85,255,0))
	def update1(self):
		self.score=self.score+5
		self.scores=self.font.render(str(self.score),True,(85,255,0))
	def update2(self):
		self.score=self.score+10
		self.scores=self.font.render(str(self.score),True,(85,255,0))
	def update3(self):
		self.score=self.score+20
		self.scores=self.font.render(str(self.score),True,(85,255,0))
	def update4(self):
		self.score=self.score+50
		self.scores=self.font.render(str(self.score),True,(85,255,0))
	def blitme(self):
		self.screen.blit(self.scores,(100,100))
	def clear(self):
		self.score=0
		self.scores=self.font.render(str(self.score),True,(85,255,0))