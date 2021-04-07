import numpy_financial as npf
import numpy as np
years =  int(input("How many years do you need to pay loan? "))
salePrice =  int(input("Purchase price: "))
borrowed =  int(input("Borrowed: "))
interestRate =  float(input("Interest Rate: "))

def paidThisMonth(interestRate, years, borrowed):
    ptm = npf.pmt(interestRate / 12, years * 12, borrowed)
    return ptm


pmt = paidThisMonth(interestRate, years, borrowed) #высчитывает непосредственно месячный платеж
print(pmt)
nper = npf.nper(interestRate/12, pmt, borrowed) #высчитывает кол-во месяцев для погашения ипотеки с заданным месячным платежем
print(np.round(nper))
ipmt = npf.ipmt(interestRate/12, np.arange(years * 12) + 1, years * 12, borrowed)#часть ежемесячного платежа которая приходится на выплату процентов, по месячно
print(ipmt)
ppmt = npf.ppmt(interestRate/12, np.arange(years * 12) + 1, years * 12, borrowed)# часть которая приходится на выплату долга так же по месячно.
print(ppmt)

# header = '{:} -> {:} | {:} | {:}'
fmt = '{0:2d} -> {1:8.2f} | {2:8.2f} | {3:8.2f}'
for payment in (np.arange(years * 12) + 1):
    index = payment - 1
    borrowed = borrowed + ppmt[index]
    print(fmt.format(payment, ppmt[index], ipmt[index], borrowed))


