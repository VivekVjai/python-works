expencess=[10000,11000,12000,13000]

for exp in expencess:

    print(exp)


#total_expenses

total_expenses=0

for exp in expencess:

    total_expenses+=exp

print(total_expenses)


#maximum_expense without using ma function

max_expence=0

for exp in expencess:

    if exp>max_expence:

        max_expence=exp

print(max_expence)