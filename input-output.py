# Demonstrate input and output        
file_name = "names.txt"

name = input("Please enter a name: ")

with open(file_name, 'w') as output:
    while name != "":
        output.write(str(name) + "\n")
        name = input("Please enter a name: ")

output.close()


with open(file_name) as input:
    lines = input.readlines()
    for line in lines:
        print(line)   
