#Get details of lon

money_owed = float(input('how much money do yo owe, in dollars?')) #$50,000
apr = float(input('what is th annual percentage rate of th loan?')) #3%
payment = float(input('How much will you pay off each month in dollars?')) #$1,000
months = int(input('How many months do you want to see the result for?')) #24

monthly_rate = apr/100/12

intest_paid = money_owed*monthly_rate

money_owed= money_owed + intest_paid

money_owed = money_owed -payment

print ('Paid', payment, 'of which', intest_paid,'was interest')
print('Now I owe', money_owed)