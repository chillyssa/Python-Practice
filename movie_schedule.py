# two ways to define a dictionary 

# current_movies = {}
# current_movies["The Grinch"] = "11:00am"
# current_movies["Rudolph"] = "1:00pm"
# current_movies["Frosty the Snowman"] = "3:00pm"
# current_movies["Christmas Vacation"] = "5:00pm"

current_movies ={
    "The Grinch": "11:00am", 
    "Rudolph": "1:00pm", 
    "Frosty the Snowman": "3:00pm", 
    "Christmas Vacation": "5:00pm"
}
print("We are showing the following movies:\n")

for key in current_movies:
    print(key, "\n")

movie = input("Which movie would you like the show time for? \n")

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested movie/showtime was not in the list.")
else:
    print(movie, "is playing at", showtime)