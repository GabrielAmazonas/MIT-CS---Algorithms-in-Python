def fib_efficient(number, computations_dictionary):
    if number in computations_dictionary:
        return computations_dictionary[number]
    else:
        answer = fib_efficient(number-1, computations_dictionary) + fib_efficient(number-2, computations_dictionary)
        computations_dictionary[number] = answer
        return answer
#Fibonacci base cases
computations_dictionary = {1:1, 2:2}

#Usage example
print(fib_efficient(6,computations_dictionary))        
