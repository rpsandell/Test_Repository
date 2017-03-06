# Added a comment here just to make a change.
def fizzbuzz(intList):
    newList = intList
    listcount = 0
    for i in newList:
        if i % 3 == 0:
            if i % 5 == 0:
                newList[listcount] = 'FizzBuzz'
            else:
                newList[listcount] = 'Fizz'
        elif i % 5 == 0:
            newList[listcount] = 'Buzz'
        listcount += 1
    return newList
