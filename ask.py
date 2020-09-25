from random import randint

class ask:
	def __init__(self):
		self.good = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."] # 1 2 3 5 4 3 6 3 4 1 2
		self.maybe = ["Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again."] # 5 5 3 10 1
		self.no = ["My reply is no.", "My sources say no.", "Outlook not so good.", "Don't count on it.", "Very doubtful."] # 2 2 4 5 7
	def choose(self):
		choice = randint(0, 2)
		if choice == 0:
			option = randint(0, 37)
			if option == 0:
				#print(self.good[0])
				return(self.good[0])
			elif option >= 1 and option <= 2:
				#print(self.good[1])
				return(self.good[1])
			elif option >= 3 and option <= 5:
				#print(self.good[2])
				return(self.good[2])
			elif option >= 6 and option <= 9:
				#print(self.good[3])
				return(self.good[3])
			elif option >= 10 and option <= 14:
				#print(self.good[4])
				return(self.good[4])
			elif option >= 15 and option <= 18:
				#print(self.good[5])
				return(self.good[5])
			elif option >= 19 and option <= 21:
				#print(self.good[6])
				return(self.good[6])
			elif option >= 22 and option <= 27:
				#print(self.good[7])
				return(self.good[7])
			elif option >= 28 and option <= 30:
				#print(self.good[8])
				return(self.good[8])
			elif option >= 31 and option <= 34:
				#print(self.good[9])
				return(self.good[9])
			elif option == 35:
				#print(self.good[10])
				return(self.good[10])
			elif option >= 36 and option <= 37:
				#print(self.good[11])
				return(self.good[11])
			else:
				print("Error. 8 Ball is out of service.")
				exit()
		elif choice == 1:
			option = randint(0, 23)
			if option >= 0 and option <= 4:
				#print(self.maybe[0])
				return(self.maybe[0])
			elif option >= 5 and option <= 9:
				#print(self.maybe[1])
				return(self.maybe[1])
			elif option >= 10 and option <= 12:
				#print(self.maybe[2])
				return(self.maybe[2])
			elif option >= 13 and option <= 22:
				#print(self.maybe[3])
				return(self.maybe[3])
			elif option == 23:
				#print(self.maybe[4])
				return(self.maybe[4])
			else:
				print("Error. 8 Ball is out of service.")
				exit()
		elif choice == 2:
			option = randint(0, 19)
			if option >= 0 and option <= 1:
				#print(self.no[0])
				return(self.no[0])
				return(self.no[3])
			elif option >= 2 and option <= 3:
				#print(self.no[1])
				return(self.no[1])
			elif option >= 4 and option <= 7:
				#print(self.no[2])
				return(self.no[2])
			elif option >= 8 and option <= 12:
				#print(self.no[3])
				return(self.no[3])
			elif option >= 13 and option <= 19:
				#print(self.no[4])
				return(self.no[4])
			else:
				print("Error. 8 Ball is out of service.")
				exit()
