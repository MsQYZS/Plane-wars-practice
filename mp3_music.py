from pygame import mixer
class Music:
	def __init__(self):
		filname="_internal\\Music\\background_music.mp3"
		mixer.music.load(filname)
		mixer.music.play(-1)
	def player(self):
		filname="_internal\\Music\\子弹射击声音.mp3"
		s=mixer.Sound(filname)
		s.play()