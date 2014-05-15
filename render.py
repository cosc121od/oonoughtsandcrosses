from tkinter import *
from tkinter.ttk import *

class Render:
    
    def __init__(self):
        self.window = Tk()
        self.button_grid = [[Canvas(self.window, width=50, height=50) for x in range(3)] for y in range(3)]
        for y in range(len(self.button_grid)):
            for x in range(len(self.button_grid[0])):
                button = self.button_grid[x][y]
                button.grid(row=x, column=y)
                button.create_line(0,0,100,100)
        self.window.mainloop()