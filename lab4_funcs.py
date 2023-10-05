# --------------------------------------------------------------
# 1) Summing Evens
# --------------------------------------------------------------
def sumeven(n:int) -> int:
    
    '''
    This function should calculate and return the sum of the 
    first n even numbers, where n >= 0. Note that 0 is even.
    
    For example, if n is 6, then the sum would be:

    0 + 2 + 4 + 6 + 8 + 10 = 30

    FOOD FOR THOUGHT:
    There are about a dozen different (yet equally 'good') ways 
    you could accomplish this. Once you've solved the problem,
    try solving it again using a different loop style, or a
    different way of producing the first n even integers. Or, 
    just maybe, you can come up with a way to solve this 
    without writing a loop at all?
    
    '''
    sumEvenValue : int = 0
    for i in range(n):
        sumEvenValue += i * 2
    return sumEvenValue

# --------------------------------------------------------------
# 2) Summing Squares
# --------------------------------------------------------------
def sumsquares(n:int) -> int:
    
    '''
    This function should calculate and return the sum of the 
    first n squares, where n >= 0. Assume that 1 is the first 
    square.
    
    For example, if n is 5, then the sum would be:

    1 + 4 + 9 + 16 + 25 = 55
   
    FOOD FOR THOUGHT:
    How much code from your solution to the previous question
    can be reused? Work smart. It's not plagiarism if it's your
    own code you wrote previously!

    '''

    sumOfSquares : int = 0
    for i in range(1,n+1):
        sumOfSquares += i **2
    return sumOfSquares


# --------------------------------------------------------------
# 3) Summing Odd Digits
# --------------------------------------------------------------   
def odddigitsum(num : int) -> int:
    
    '''
    This function should calculate and return the sum of the 
    odd digits in the input integer num. The input can be any 
    integer, positive or negative.
    
    For example, if num is 482376, then the sum would be:
    
    3 + 7 = 10
    
    FOOD FOR THOUGHT:
    One thing that sets computer scientists apart from 
    mathematicians is our appreciation for the integer 
    division (//) and remainder (%) operations. Why do I 
    bring this up here of all places...? 
    
    '''
    oddSumValue : int = 0
    strNum = str(num)
    for c in strNum:
        if c == "-":
            continue
        if int(c) % 2 != 0:
            oddSumValue += int(c)
    return oddSumValue

    
    
    
    
# --------------------------------------------------------------
# 4) Listing Exponentials
# --------------------------------------------------------------
def listexponential(n: int, base: int) -> list:
    
    '''
    This function should calculate and return a list containing
    the first n exponentials, where 'base' is the base. Assume 
    that 0 is the first exponent.
    
    For example, if n is 6, and base is 2, then the list would be:
    
    [ 2**0, 2**1, 2**2, 2**3, 2**4, 2**5 ] = [ 1, 2, 4, 8, 16, 32]

    FOOD FOR THOUGHT:
    Use your solution to answer the age old thought experiment:
    Would you rather have $1,000,000 now, or $0.01 doubled
    every day for a month? 
   
    '''
    listOfExp = []
    for i in range(n):
        listOfExp.append(base**i)

    return listOfExp
    
    
# --------------------------------------------------------------
# 5) Concatenating Digits
# --------------------------------------------------------------      
def digitcat(s):
    
    '''
    This function accepts a string 's' as input, extracts the
    digit characters, and returns those digits as an integer.
    
    For example, if 's' is the string: 
    
    'I want 3 oranges, 24 bananas, and 101 dalmations'
    
    Then the function should return the integer 324101
    
    If there are no digits, return None.

    '''
    outputIntegerString : str = ""

    for c in s:
        try:
            int(c) #Will throw error if character can't be made a string
            outputIntegerString += c
        except:
            continue
        
    if outputIntegerString == "": return None
        
    return int(outputIntegerString)
    
    
# --------------------------------------------------------------
# 6) Parsing Floats
# --------------------------------------------------------------      
def stringtofloatlist(fltstr):
    
    '''
    Given an input string guaranteed to contain comma-separated
    floating point numbers, extract each float and place them
    in a list. Return the list.
    
    For example, if the input string is "1.23,2.4,3.123", then
    you should return the list [ 1.23, 2.4, 3.123 ]
    
    FOOD FOR THOUGHT:
    Don't reinvent the wheel. Familiarize yourself with the 
    Python documentation. Perhaps there are some built-in string 
    methods (*cough* split() *cough*) that could be of service?
    https://docs.python.org/3/library/stdtypes.html#string-methods
    Alternatively, DO reinvent the wheel, it's great practice
    either way!
    
    '''
    
    floatList : list = fltstr.split(",") 
    
    for i in range(len(floatList)): 
        floatList[i] = float(floatList[i])
    return floatList

    
# --------------------------------------------------------------
# 7) Maximum of Each Type
# --------------------------------------------------------------      
def maxbytype(items):
    
    '''
    Assume that parameter 'items' is a heterogeneous list that
    may contain integers, floats, strings, and any other type.
    
    You should return a 3-tuple, where the first element is the
    largest integer, the second element is the largest float, 
    and the third element is the largest string.
    
    If any of the types are not found in the list at all, there
    can logically be no maximum, and therefore you should use 
    the value None to represent this.
    
    Example #1) if the input list is:
    [ "hello", 1, 3.14, 99, "cat", "tac", 2.7, "bat" ]
    Then the tuple returned should be: (99, 3.14, "tac")
    
    Example #2) if the input list is: 
    [ "hello", 1, 99, "cat", "tac", "bat" ]
    Then the tuple returned should be: (99, None, "tac")
    
    You can check the type of any object in Python by using the
    type() function. For example, type(item) == float, will 
    return True if item is a float, False otherwise.
    
    FOOD FOR THOUGHT:
    Why might we use the special value 'None' when there is no
    instance of a particular type present in the list? Why not
    use some error value, eg. -1 for integers, or the empty
    string if there is no string?

    '''
    def findLargest(iterable, classinfo):
        """
        Finds the 'largest' item in an interable of type 'classinfo'

        """
        listOfItems = []
        for item in iterable:
            if isinstance(item, classinfo):
                listOfItems.append(item)
        
        if len(listOfItems) == 0: return None
        
        largest = listOfItems[0] #Starts with the first, to compare to others
        for item in listOfItems:
            if item > largest: largest = item
        return largest
    
    return (findLargest(items, int), findLargest(items, float), findLargest(items, str))

    

    
        
