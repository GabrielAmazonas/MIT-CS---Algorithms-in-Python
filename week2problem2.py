
def calculate_lowest_payment(balance, annualInterestRate):
    #The answer must be a 10 multiple    
    monthlyPayment = 10
    def checkMonthlyPayment(monthlyPayment, balance, annualInterestRate):
        monthsCount = 0
        remainingBalance = balance
        while(monthsCount < 12):
            remainingBalance -= monthlyPayment
            unpaid = remainingBalance 
            interest = (annualInterestRate / 12) * unpaid
            remainingBalance += interest
            monthsCount += 1
        if(remainingBalance > 0):
            return checkMonthlyPayment(monthlyPayment + 10, balance, annualInterestRate)
        else:
            #Base case for recursive execution
            return monthlyPayment
    print("Lowest Payment: ", "%.2f"%checkMonthlyPayment(monthlyPayment, balance, annualInterestRate))

calculate_lowest_payment(4773, 0.2)