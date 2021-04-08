import numpy_financial as npf
import numpy as np

#-->Variables
years =  int(input("How many years do you need to pay loan? "))
borrowed =  int(input("Borrowed: "))
interestRate =  float(input("Interest Rate: "))

months = years * 12
true_rate = interestRate / 12  #month's rate

#-->Functions
pmt = npf.pmt(true_rate, months, borrowed) #высчитывает непосредственно месячный платеж
# print(pmt)
nper = npf.nper(true_rate, pmt, borrowed) #высчитывает кол-во месяцев для погашения ипотеки с заданным месячным платежем
# print(np.round(nper))
ipmt = npf.ipmt(true_rate, np.arange(months) + 1, months, borrowed)#часть ежемесячного платежа которая приходится на выплату процентов, по месячно
# print(ipmt)
ppmt = npf.ppmt(true_rate, np.arange(months) + 1, months, borrowed)# часть которая приходится на выплату долга так же по месячно.
# print(ppmt)


def totalSumm(total_pem):
    return round((total_pem * months), 2)
def totalInterest(totalSumm):
    return round((totalSumm + borrowed), 2)

#-->Output
#---->General information
print("||||||||||||||||||||||||||||||||||||||||")
print("Loan amout:%7.2f"%borrowed)
print(f"Loan duration in months: {months}")
print(f"Annunal Interest rate in percent: {interestRate*100}")
#---->Calculations
print("Total Monthly Payment:%7.2f"%pmt)
print(f"Total of {months} payments: {totalSumm(pmt)}")
print(f"Over {months} months you will spend: {totalInterest(totalSumm(pmt))} in interest")
wantFullReport = input("Do you want to make full report? (y/n) ")
if wantFullReport == "y":
    print("||||||||||||||||||||||||||||||||||||||||")
    print("MONTH -> " + "  PRI | INTEREST| PRINCIPAL REMAINING")
    fmt = '{0:2d} -> {1:8.2f} | {2:8.2f} | {3:8.2f}'
    for payment in (np.arange(months) + 1):
        index = payment - 1
        borrowed = borrowed + ppmt[index]
        print(fmt.format(payment, ppmt[index], ipmt[index], borrowed))
