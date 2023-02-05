from turtle import *

def make_pattern():
	listy = ['purple', 'red', 'blue', 'orange', 'green']
	bgcolor('black')
	for i in range(200):
		color(listy[i%5])
		pensize(i/10+1)
		forward(i)
		left(70)