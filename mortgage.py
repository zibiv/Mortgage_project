import numpy as np

years =  20#int(input("How many years do you need to pay loan? "))
# salePrice =  int(input("Purchase price: "))
borrowed = 150000# int(input("Borrowed: "))
interestRate = 0.05 #float(input("Interest Rate: "))
months = years * 12
true_rate = interestRate / 12

def paidEveryMonth(interestRate, months, borrowed):
    total_pem = (borrowed * true_rate * ((true_rate + 1)**months)) / ((true_rate + 1)**months - 1)
    return total_pem
def totalSumm(total_pem):
    return round((total_pem * months), 2)
def totalInterest(totalSumm):
    return round((totalSumm - borrowed), 2)
def fullReport(total_pem, borrowed):
    fmt = '{0:2d} -> {1:8.2f} | {2:8.2f} | {3:8.2f}'
    for index in range(1, months + 1):
        interest = borrowed * interestRate / 12
        principal = total_pem - interest
        borrowed -= principal
        print(fmt.format(index, principal, interest, borrowed))


print("Loan amout:%7.2f"%borrowed)
print(f"Loan duration in months: {months}")
print(f"Annunal Interest rate in percent: {interestRate*100}")
tmp = paidEveryMonth(interestRate, months, borrowed)
print(f"Total Monthly Payment: {tmp}")
print(f"Total of {months} payments: {totalSumm(tmp)}")
print(f"Total Interest Paid: {totalInterest(totalSumm(tmp))}")
whantFullReport = input("Do you want to make full report? (y/n)")
if whantFullReport == "y":
    fullReport(tmp, borrowed)
else:
    pass



