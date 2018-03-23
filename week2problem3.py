
#SETUP: balance and annualInterestRate

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = (annualInterestRate / 12.0)

lowerBound = balance / 12

interestIncreaseRate = (1 + monthlyInterestRate) ** 12

upperBound =  balance *  interestIncreaseRate / 12.0

def checkValue(balance, lowerBound, upperBound):
    originalBalance = balance
    monthsCount = 0

    #setting up a new guess
    guess = (upperBound + lowerBound) / 2

    remainingBalance = balance
    #12 months interest count
    while(monthsCount < 12):
        remainingBalance -= guess
        unpaid = remainingBalance 
        interest = (annualInterestRate / 12) * unpaid
        remainingBalance += interest
        monthsCount += 1
    if(remainingBalance <= 0.1 and remainingBalance >= 0):
        print("Lowest Payment: ", "{0:.2f}".format(guess))
    elif(remainingBalance > 0.1):
        #Increase the guess
        checkValue(originalBalance, guess, upperBound)
    elif(remainingBalance < 0):
        #Decrease the guess
        checkValue(originalBalance, lowerBound, guess)
    
checkValue(balance, lowerBound, upperBound)
