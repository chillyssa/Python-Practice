# Demonstrate input and output
# Actually, we'll do output then input

""" Files will be in the same folder as this program

    1. Create a new file with to write to called scores.txt
    2. Generate and write random numbers representing test scores
    3. Close the file
    4. Open the file for reading and create a list to hold scores
    5. Read each line and convert the score to integer
    6. Add the number to a list
    7. Loop to get the next score until scores are depleted
    8. Calculate and print the average score
    9. Close the input file
"""

import random

#1, #2

num_scores = 10        # Number of scores to generate
score_lo = 50          # Lowest  score to generate
score_hi = 100         # Highest score to generate
file_name = "scores.txt"
with open(file_name, 'w') as output:
    for i in range(num_scores):
        score = random.randint(score_lo,score_hi)
        output.write(str(score) + "\n")

#3
output.close()

#4
with open(file_name) as input:    # 'open' defaults to 'read'
    lines = input.readlines()

#5, #6, #7
all_scores = []
for line in lines:
    score = int(line.strip())     # Strip leading/trailing spaces
    all_scores.append(score)

#8
for score in all_scores:
    print(score)
average = round(sum(all_scores) / len(all_scores), 1)
print("The average of all", num_scores, "scores between", \
      score_lo, "and", score_hi, "is", average)

#9
input.close()
