file = open('log.txt', 'r')
lines = file.readlines()

word = input("what are you searching for?: ")
lineNumber = 0

for line in lines:
    if (word in line):
        print (f"{word} is in line: {lineNumber} {line}")
    lineNumber += 1    
file.close()