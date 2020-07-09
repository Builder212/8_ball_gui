from tkinter import *
from ask import choose as rand_reply

class eight_ball_GUI:
	def __init__(self, master):
		self.answer = ""
		self.root = root
		root.title("8 Ball")
		self.label = Label(root, text="Enter your question here!")
		self.label.pack()
		self.entry1 = Entry(root)
		self.entry1.pack()
		self.enter_button = Button(root, text="Enter", command=self.enter)
		self.enter_button.pack()
		self.close_button = Button(root, text="Close", command=master.quit)
		self.close_button.pack()

	def enter(self):
		self.label.destroy()
		self.entry1.delete(0, 'end')
		question = self.entry1.get()
		print(question)
		if question != False:
			self.answer = rand_reply()
			self.label = Label(root, text=self.answer)
			self.label.pack()
		else:
			self.label.destroy()
		

root = Tk()
my_gui = eight_ball_GUI(root)
root.mainloop()