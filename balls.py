from tkinter import *
from random import randint

WIDTH = 500
HEIGHT = 500



def get_coord(event):
	x = event.x
	y = event.y
	print(f'x: {event.x}  y: {event.y}')
	return x, y


class Ball:
	def __init__(self):
		self.R =randint(10,50)
		self.x = randint(self.R, WIDTH - self.R)
		self.y = randint(self.R, HEIGHT - self.R)
		self.dx, self.dy = (randint(-20,20),randint(-20,20))
		if self.dx == 0:
			self.dx = randint(1, 10)
		if self.dy == 0:
			self.dy = randint(1, 10)
		self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R, self.x + self.R, self.y + self.R , fill = 'green')

	def move(self):
		self.x += self.dx
		self.y += self.dy
		if self.x + self.R > WIDTH or self.x - self.R <= 0:
			self.dx = -self.dx
		if self.y + self.R > HEIGHT or self.y - self.R <= 0:
			self.dy = -self.dy

	def show(self):
		canvas.move(self.ball_id, self.dx, self.dy)

	def check_inside(self,x,y):
		if x == self.x + self.R or x == self.x - self.R and y == self.y +self.R or y == self.y - self.R:
			return True
		else:
			return False


def tick():
	for ball in balls:
		ball.move()
		ball.show()
	window.after(50, tick)


def main():
	global window, canvas, balls

	window = Tk()
	window.geometry(str(WIDTH) + "x" + str(HEIGHT))
	canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = 'black')
	canvas.pack(anchor = "nw", fill = BOTH)
	canvas.bind('<Button-1>', get_coord)
	balls = [Ball() for i in range(randint(1,20))]
	tick()
	window.mainloop()


if __name__ == '__main__':
	main()
