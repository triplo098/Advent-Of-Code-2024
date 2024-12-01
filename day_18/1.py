
readInput = True #deciding between demo or input

if readInput == True:
    fileNameToRead = "input.txt"
else:
    fileNameToRead = "demo_input.txt"

data = open(fileNameToRead, "r").read()

print(data)
