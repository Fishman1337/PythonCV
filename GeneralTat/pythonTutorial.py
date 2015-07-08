from sys import exit

def goldRoom():
	print "This room is full of gold coins.  How much would you like to take?"

	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Please enter a number!")

	if how_much < 50:
		print "Nice, you're not greedy!"
		exit(0)
	else:
		dead("You are so greedy")


def bearRoom():
	print "There is a bear here."
	print ""
	bearMoved = False

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("The Bear looks at you and then claws your face... off")
		elif choice == "taunt bear" and not bearMoved:
			print "The bear has moved from the door"
			bearMoved = True
		elif choice == "taunt bear" and bearMoved:
			dead("the bear ges pissed off and chews your leg")
		elif choice == "open door" and bearMoved:
			goldRoom()
		else:
			print "I got no idea what that means"

def cthulhuRoom():
	print "Here you see Cthulhu"

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("That was tasty!")
	else:
		cthulhuRoom()

def dead(why):
	print why, "good job!"
	exit(0)

def start():
	print "Are you are in a dark room"

	choice = raw_input("> ")

	if choice == "left":
		bearRoom()
	elif choice == "right":
		cthulhuRoom()
	else:
		dead("You stumble around the room and starve eventually.")

start()