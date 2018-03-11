def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    stringSize = len(aStr)
    
    if(stringSize == 0):
        return False
    elif(stringSize == 1):
        return char == aStr[0]
        
    middleCharacterIndex = (stringSize // 2) 
    if(char == aStr[middleCharacterIndex]):
        return True
    elif(char < aStr[middleCharacterIndex]):
        return isIn(char, aStr[:middleCharacterIndex])
    else:
        return isIn(char, aStr[middleCharacterIndex:])
