'''
Let's decide!
Input different things to choose from
The code outputs a decision for you
'''
import random

#list of str choices
choices = []
#inputed choice
choice = ""

print("Let's decide!\n")
while choice.lower() != "stop":
	choice = str(input('Enter choice. If you want to remove your last choice, enter \"remove\". If you are done, enter \"stop\". \n'))
	if (choice != "stop") and (choice != "") and (choice != "remove"):
		choices.append(choice)
	elif choice == "":
		print("Whoops, you entered a blank. Enter a valid choice.")
	elif choice == "remove":
		choices.pop()
		print("Poof! It's gone")
	else:
		break
	print()

print("\nThe random generator has spoken. It decided on:", choices[random.randint(0, len(choices)-1)])