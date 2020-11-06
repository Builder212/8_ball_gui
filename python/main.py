from tkinter import *
import sys
from tk_gui import TK_GUI

gui_style = int(input("Would you like to see the gui using tkinter, kivy, or pyqt. (tkinter=0, kivy=1, pyqt=2)\n"))
if gui_style == 0:
	root = Tk()
	eight_ball_gui = TK_GUI(root)
	root.mainloop()
