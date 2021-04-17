try:
    file_name = "names2.txt"
    with open(file_name, 'r') as input:
        lines = input.readlines()
        for line in lines:
            print(line) 
except FileNotFoundError: 
    print("The file ", file_name, " was not found.", sep="")
    user_input = input("Would you like to create the file? Enter Y for yes or N for No: ")
    if user_input == "Y": 
        file_name = "names2.txt"
        name = input("Please enter a name: ")
        with open(file_name, 'w') as output:
            while name != "":
                output.write(name + "\n")
                name = input("Please enter a name: ")
            output.close()
        with open(file_name, 'r') as input:
            lines = input.readlines()
            print("The file consists of:")
            for line in lines:
                print(line) 
    else: 
        print("Thank you, have a nice day.")
        exit()
    

