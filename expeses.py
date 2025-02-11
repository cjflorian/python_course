expenses = []
total = 0

num_expenses = int(input("Enter th # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expese:")))

total = sum(expenses)
print ('You spent $', total, sep='')