import re

def main():
	
	readFile = open('logOutput.txt', 'r')
	gitRe = re.compile(r'^(\d+)\s*(\d+)')
	dateRe = re.compile(r'Date:\s*([\d\w\s:]*) ')
	insertions = []
	deletions = []

	for line in readFile:
		date = re.search(dateRe, line)
		info = re.search(gitRe, line)
		if info:
			print(info.groups())
			#insertions.append(info.group(1))
			#deletions.append(info.group(2))

	print(insertions)
	print(deletions)	

main()
