# expenses = [10.50, 8, 5, 15, 20, 5, 3]
# total = 0 

# for i in expenses:
#     total = total + i

# print("You spent $", total, " on lunch this week.", sep="") 

# can also use the built in sum function to achieve the same answer
# sum_total = sum(expenses)
# print("The sum total is $", sum_total, sep="")


#Adding input to the above program

total = 0 

expenses=[]
num_expenses = int(input("How many expenses do you have for this week?: "))

for i in range (num_expenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print("You spent $", total, sep="")