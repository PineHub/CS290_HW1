def reverseString(inputString):


    if len(inputString) == 1:
        return inputString

    else:
        return inputString[len(inputString) - 1] + reverseString(inputString[0:(len(inputString)-1)])

print(reverseString("hello"))
