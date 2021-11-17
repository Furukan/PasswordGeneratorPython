import random
import itertools
import threading
import time
import sys
import string


# 1 : Easy
# 2 : Medium
# 3 : Hard

DifficultyOfPassword = 3


print("Welcome to Furukan's PasswordGenerator Please Wait A Little Time\n\n")

LoadingIsDone = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']): 

        if LoadingIsDone:
            break

        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
	


t = threading.Thread(target=animate)
t.start()


time.sleep(3)
LoadingIsDone = True


print("\rDone!")


BigLetters = list(string.ascii_uppercase)

TinyLetters = list(string.ascii_lowercase)

Numbers = list(string.digits)

Symbols = list(string.punctuation)

Easy = BigLetters + TinyLetters
Medium = Easy + Numbers
Hard = Medium + Symbols

if (DifficultyOfPassword != 1 and DifficultyOfPassword != 2 and DifficultyOfPassword != 3):

	print("Programı Bozmaya Çalışma :<")
	exit()


DifficultyList = [None, Easy, Medium, Hard]
Characters = DifficultyList[DifficultyOfPassword]

def GenerateRandomPassword():
	random.shuffle(Characters)

	time.sleep(1)

	answer = input("\n\nLenght of the password : ")

	try:
		lenght = int(answer)
	except ValueError:
		print("\n\nWhy you are trying to set the password lenght a normal number ?")

		time.sleep(5)

		exit()


	password = []
	for i in range(lenght):
		password.append(random.choice(Characters))

	random.shuffle(password)
	random.shuffle(password)
	random.shuffle(password)
	random.shuffle(password)
	random.shuffle(password)
	random.shuffle(password)
	random.shuffle(password)
	random.shuffle(password)


	password = "".join(password)

	return password

while True:
	print(GenerateRandomPassword())
	time.sleep(1)
