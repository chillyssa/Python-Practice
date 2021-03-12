# input
weather = float(input("What is the temperature today?\n"))

# process
if weather >= 80.0:
    message = "It's too hot out! \nStay inside!"
elif weather <= 55.0:
    message = "BRRR! It's cold out! \nStay warm!"
else:
    message = "Enjoy the outdoors!"

# output
print(message)