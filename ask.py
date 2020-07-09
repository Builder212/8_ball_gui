from random import randint

def choose():
	good = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."] # 1 2 3 5 4 3 6 3 4 1 2
	maybe = ["Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again."] # 5 5 3 10 1
	no = ["My reply is no.", "My sources say no.", "Outlook not so good.", "Don't count on it.", "Very doubtful."] # 2 2 4 5 7
	choice = randint(0, 2)
	if choice == 0:
		option = randint(0, 37)
		if option == 0:
			print(good[0])
			return(good[0])
		elif option >= 1 and option <= 2:
			print(good[1])
			return(good[1])
		elif option >= 3 and option <= 5:
			print(good[2])
			return(good[2])
		elif option >= 6 and option <= 9:
			print(good[3])
			return(good[3])
		elif option >= 10 and option <= 14:
			print(good[4])
			return(good[4])
		elif option >= 15 and option <= 18:
			print(good[5])
			return(good[5])
		elif option >= 19 and option <= 21:
			print(good[6])
			return(good[6])
		elif option >= 22 and option <= 27:
			print(good[7])
			return(good[7])
		elif option >= 28 and option <= 30:
			print(good[8])
			return(good[8])
		elif option >= 31 and option <= 34:
			print(good[9])
			return(good[9])
		elif option == 35:
			print(good[10])
			return(good[10])
		elif option >= 36 and option <= 37:
			print(good[11])
			return(good[11])
		else:
			print("Error. 8 Ball is out of service.")
			exit()
	elif choice == 1:
		option = randint(0, 23)
		if option >= 0 and option <= 4:
			print(maybe[0])
			return(maybe[0])
		elif option >= 5 and option <= 9:
			print(maybe[1])
			return(maybe[1])
		elif option >= 10 and option <= 12:
			print(maybe[2])
			return(maybe[2])
		elif option >= 13 and option <= 22:
			print(maybe[3])
			return(maybe[3])
		elif option == 23:
			print(maybe[4])
			return(maybe[4])
	elif choice == 2:
		option = randint(0, 19)
		if option >= 0 and option <= 1:
			print(no[0])
			return(no[0])
		elif option >= 2 and option <= 3:
			print(no[1])
			return(no[1])
		elif option >= 4 and option <= 7:
			print(no[2])
			return(no[2])
		elif option >= 8 and option <= 12:
			print(no[3])
			return(no[3])
		elif option >= 13 and option <= 19:
			print(no[4])
			return(no[4])