

#due_balance_d1 = unpaid_balance_
def calculate_remaining_balance(balance, annualInterestRate, monthlyPaymentRate):
    monthsCount = 0
    remainingBalance = balance

    while(monthsCount < 12):
        print("Month: ", monthsCount)
        print("Remaining balance before payment: ", "%.2f"%remainingBalance)
        paid = remainingBalance * monthlyPaymentRate
        remainingBalance -= paid
        unpaid = remainingBalance 
        print("Remaining balance after payment: ", "%.2f"%remainingBalance)

        interest = (annualInterestRate / 12) * unpaid
        remainingBalance += interest
        monthsCount += 1

    print("Remaining balance: ", "%.2f"%remainingBalance)

calculate_remaining_balance(484, 0.2, 0.04)