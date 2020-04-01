from tkinter import *

window = Tk()
window.geometry ('300x300')

def get_coord(event):
	get_coord_x = event.x
	get_coord_y = event.y
	print(f'x: {get_coord_x}  y: {get_coord_y}')





window.bind('<Button-1>', get_coord)
window.mainloop()