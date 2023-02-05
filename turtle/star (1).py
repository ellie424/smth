from turtle import *

def make_star():
	color('purple', 'pink')
	begin_fill()
	while True:
		forward(200)
		left(170)
		if abs(pos()) < 1:
			break
	end_fill()
	done()