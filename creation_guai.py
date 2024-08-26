#结果实例('蓝色', {'scores': 10, 'speed': 0.3})
from random import randint
def creation():
	guai_list=["绿色","蓝色","黄色","红色"]
	guai_dict={\
	"红色":{'scores':50,'speed':1.1},\
	"黄色":{'scores':20,'speed':0.5},\
	"蓝色":{'scores':10,'speed':0.3},\
	"绿色":{'scores':5,'speed':0.2}\
	}
	i=randint(0,101)
	if 0<=i<44:
		a=guai_list[0]
	elif 44<=i<80:
		a=guai_list[1]
	elif 80<=i<96:
		a=guai_list[2]
	else:
		a=guai_list[3]
	for guais in guai_dict.items():
		if guais[0]==a:
			return guais