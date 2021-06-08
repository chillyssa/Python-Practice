# Input 

print("This program will tell you whether your words entered are anagrams")

usr_input1 = input("Please enter a word: ")
usr_input2 = input("Please enter a second word: ")


# Process 

if sorted(usr_input1) == sorted(usr_input2):
	message = "The two entries are anagrams!"
else:
	message = "The two entries are not anagrams :("
 
# Output 
print(message) 
