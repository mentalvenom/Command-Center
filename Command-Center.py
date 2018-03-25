from termcolor import colored
from time import sleep


def clearone():
	print('\n' * 100)


def cleartwo():
	print('\n' * 10)


cleartwo()

start = input(colored("Press Enter to Start the Program!", "magenta"))
clearone()

sleep(3.5)

print(
    colored("""Booting Command Center...
This May Take a Few Seconds...
Please Be Patient...
""", "red"))

print('')

sleep(5.5)

print(colored("""Almost Done...
Command Center is Loading...""", "red"))

print('')

sleep(8)

print(
    colored("""Thank you for waiting...
Command Center is Fully Loaded...
I hope You Enjoy!""", "yellow"))

sleep(5.5)

print('')

text_file = open('commands.txt', 'r')

line_list = text_file.readlines()

for line in line_list:
	print(line)

print('')
print('')
print('')
advance = input(colored("Press Enter to Continue ", "magenta"))
clearone()

print('')


def cmd():
	command = input(
	    colored(
	        "Enter a Command (Commands are located in the commands.txt file): \n",
	        "yellow"))

	print('')

	if command == "greet":
		greet = input(colored("Enter your Name: ", "magenta"))
		print('')
		print(
		    colored("Your name is " + greet +
		            "! You now know how to call a function!", "yellow"))

	elif command == "sing":
		print(
		    colored(''' 
        Twinkle, twinkle little star.
        How I wonder what you are.
        Up above the world so high.
        Like a diamond in the sky!
        Twinkle, twinkle little star
        How I wonder what you are
    
        When the blazing sun is gone
        When he nothing shines upon
        Then you show your little light
        Twinkle, twinkle, all the night
        Twinkle, twinkle, little star
        How I wonder what you are ''', "cyan"))
		print('')
		print(
		    colored("-------------------------------------------------",
		            "yellow"))
		print('')
		print(
		    colored("Great Job! You now know how to create string text!",
		            "cyan"))

	elif command == "date":
		import datetime
		date = (datetime.datetime.now().strftime("%x"))
		print(date)
	elif command == "month":
		import datetime
		month = (datetime.datetime.now().strftime("%B"))
		print(month)
	elif command == "time":
		import datetime
		time = (datetime.datetime.now().strftime("%X"))
		print(time)
	elif command == "year":
		import datetime
		year = (datetime.datetime.now().strftime("%Y"))
		print(year)
	elif command == "mirror":
		mirror = input(
		    colored("Enter text to be mirrored on the console: ", "yellow"))
		print('')
		print(colored("|" + mirror + "|", "cyan"))
		print('')
		print("--------------------------------")
		print('')
		print(
		    colored("Awesome! Now you know how to do basic input/output!",
		            "yellow"))
	elif command == "calc":

		def add(x, y):
			return x + y

		def subtract(x, y):
			return x - y

		def multiply(x, y):
			return x * y

		def divide(x, y):
			return x / y

		print(colored("Select operation.", "red"))
		print("")
		print(colored("1.Add", "magenta"))
		print(colored("2.Subtract", "magenta"))
		print(colored("3.Multiply", "magenta"))
		print(colored("4.Divide", "magenta"))

		print("")

		choice = input(colored("Enter choice(1/2/3/4):", "yellow"))

		print("")

		num1 = int(input(colored("Enter first number: ", "green")))
		num2 = int(input(colored("Enter second number: ", "green")))
		print("")

		if choice == '1':
			print(colored(num1, "+", num2, "=", add(num1, num2), "cyan"))

		elif choice == '2':
			print(colored(num1, "-", num2, "=", subtract(num1, num2), "cyan"))

		elif choice == '3':
			print(colored(num1, "*", num2, "=", multiply(num1, num2), "cyan"))

		elif choice == '4':
			print(colored(num1, "/", num2, "=", divide(num1, num2), "cyan"))
		else:
			print(colored("Invalid input", "red"))
	elif command == "password":
		import random

		s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
		passlen = int(input(colored("How long is your password: ", "yellow")))
		print('')
		p = "".join(random.sample(s, passlen))
		print(colored("Here is your password: " + p, "red"))

	elif command == "encrypt":
		text = input(colored("Enter decrypted text:\n", "yellow"))

		encrypted_text = ""
		for encrypt in text:
			x = ord(encrypt)
			x = x + 1
			encrypt = chr(x)
			encrypted_text = encrypted_text + encrypt
		print('')
		print(colored(encrypted_text, "red"))
	elif command == "decrypt":
		text = input(colored("Enter encrypted text:\n", "yellow"))
		decrypted_text = ""
		for decrypt in text:
			x = ord(decrypt)
			x = x - 1
			decrypt = chr(x)
			decrypted_text = decrypted_text + decrypt
		print('')
		print(colored(decrypted_text, "red"))
	elif command == "8ball":
		import random
		import time
		choices = [
		    "Definitely", "Yes", "Probably", "Maybe", "Probably Not", "No",
		    "Definitely Not", "I don't know", "Ask Later", "I'm too tired",
		    "If You Try Hard", "No Doubt About it", "If you Think so",
		    "I Think so", "In my eyes, yes", "In my eyes, no",
		    "Don't Ask Again", "That's a dumb thing to ask",
		    "Maybe you should ask someone else",
		    "I don't know about you, but I don't know"
		]
		input(colored("Ask the mighty 8-Ball a question\n", "magenta"))

		times = int(
		    input(
		        colored("how many times would you like to shake the 8-ball: ",
		                "magenta")))

		print('')

		for _ in range(times):
			print('')
			print(colored("Shaking...", "yellow"))
			print('')
			time.sleep(1.5)
			print(colored(random.choice(choices), "cyan"))


cmd()
