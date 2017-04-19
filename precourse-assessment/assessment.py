'''
This is your precourse assesment. Below is a set of functions that you must complete.
Delete `pass` and write the contents of the function that will produce the desired outcome.

The docstrings under the functions will give you instructions on how to produce
the desired output.

Your code will be run against a unit test in file assessment_unittest.py
Open that file to see how basic unit tests are done. Pandas runs many 1000's of unit tests.

To test your code
----------------
At the command prompt run the following:
>>> python assessment_unittest.py

If any of the tests failed you will see `FAILED(failures=n)` 
where n is the number of tests failed.

If all your tests are correct you will see `OK`

Please commit the changes back to github

The first function has been done for you.

'''

def mult_dummy(x, y):
    '''
    Multiplies two numbers together

    Parameters
    ----------
    x: number
    y: number

    Returns
    -------
    The value when x and y are multiplied together
    '''
    return x * y

def add_divide_product(x, y):
    '''
    Divide the sum of two numbers by their product

    Parameters
    ----------
    x: positive number
    y: positive number

    Returns
    -------
    The value of the division of the sum of two numbers by their product

    '''
    return (x+y)/(x*y)

def count_letters(string, letter):
    '''
    Counts the occurrences of a single letter in a string

    Parameters
    ----------
    string: a string with characters
    letter: a single character that you will count in the string

    Return
    ------
    The number of times `letter` appears in `string`
    '''
    return string.count(letter)

def largest_smallest(some_list):
    '''
    Find the largest and smallest value in a list

    Parameters
    ----------
    some_list: a list of numbers

    Returns
    -------
    a tuple of the largest and smallest numbers in the list
    '''
    return max(some_list),min(some_list)

def greatest_divisble_7(some_list):
    '''
    Find the largest number in a list that is divisible by 7

    Parameters
    ----------
    some_list: a list of numbers

    Returns
    -------
    The largest number that is divisible by 7
    '''
    sorted_list = sorted(some_list, reverse=True)
    i=0
    found = False
    triedall = False
    while(not(found) and not(triedall)):
        if i >= len(sorted_list): 	
            triedall = True
        else:
            found = not(sorted_list[i] % 7)
        i+=1
    if found:
        return sorted_list[i-1]
		

def greatest_common_factor(x, y):
    '''
    Find the greatest common factor between x and y

    Parameters
    ----------
    x: a positive integer
    y: a positive integer

    Returns
    -------
    The largest integer divisible by x and y
    '''
    i = min(x,y)
    found = False
    while(i>0 and not(found)):
        if(not(x%i) and not(y%i)):
            found=True
        else:
            i-=1
    return(i)
	

def count_words(string):
    '''
    Count the words in the string

    Parameters
    ----------
    string: any string

    Returns
    -------
    An integer of the number of words in the string

    Hint
    ----
    look at the split method
    '''
    return(len(string.split()))
   

def count_substring_words(string, substring):
    '''
    Count the number of words that contain a certain word

    Parameters
    ----------
    string: any string
    substring : any string

    Returns
    -------
    The number of words in `string` that contain an exact match of `substring`
    '''
    total = 0
    for w in string.split():
        total += count_letters(w,substring)==True
    return total

def get_special_string_methods(end):
    '''
    Get a list of the first `end` string special methods

    Parameters
    ----------
    end: an integer

    Returns
    -------
    A list of the first `end` string special methods produced from the `dir` function
    '''
    return dir(str)[:end]

def longest_word(string):
    '''
    Get the longest word from a string

    Parameters
    ----------
    string: a string of words separated by spaces

    Returns
    -------
    The string with the most characters
    '''
    return(sorted(string.split(),key = len)[-1])

def double_letter_words(string):
    '''
    Get all the words that have two consecutive repeating letters

    Parameters
    ----------
    string: a string of words separated by spaces

    Returns
    -------
    a list of all words that contain at least one occurrence of 
    consecutive repeating letters
    '''
    words = string.split()
    repwords = []
    for w in words:
        foundrep = False
        lastletter = None
        for c in w:
            if c == lastletter:
                foundrep = True
            lastletter = c
        if(foundrep):
            repwords.append(w)
    return (repwords)	

def dict_of_powers(n):
    '''
    Create a dictionary with keys as integers 1 to n (inclusive) 
    and the values as a list of that integer raised to the 2nd, 3rd and 4th power

    Parameters
    ----------
    n: positive integer

    Returns
    -------
    a dictionary with keys as integers 1 to n (inclusive) 
    and the values as a list of that integer raised to the 2nd, 3rd and 4th power

    '''
    dictout = {}
    for i in range(n):
        dictout[i+1] = [(i+1)**2,(i+1)**3,(i+1)**4]
    return dictout
        

def last_2_list(some_list):
    '''
    Find the 4th to last and 2nd to last elements in a list

    Parameters
    ----------
    some_list: a list of elements

    Returns
    -------
    a list with the 4th and 2nd to last elements of `some_list`
    '''
    return ([some_list[-4],some_list[-2]])

def reorder_list(orig_list, order):
    '''
    Reorderd a list based on another list

    Parameters
    ----------
    orig_list: a list that will get reordered
    order: A list of integers that correspond to the new order of the list.
           Will contain all intgers between 0 and len(orig_list)-1

    Examples
    --------
    if orig_list is ['a', 'b', 'c'] and order is [2, 0, 1] then
    you would return ['c', 'a', 'b']

    '''
    return ([ orig_list[i] for i in order])

def prob_3_dice(num_dice, faces, total, num_simulations=10000):
    '''
    Finds the probability through simulation that the dice thrown will equal the total

    Parameters
    ----------
    num_dice: number of dice thrown
    faces: a list of the possible faces (integers)
    total: the sum of the faces that we want to find the probability of
    num_simulations: the number of times to simulate the dice throw. Default of 10000

    Returns
    -------
    the probability of sum of the dice equaling the total

    Hint
    ----
    Use the choice function in the random module to simulate dice throws

    '''
    from random import choice

    success = 0
    for sim in range(num_simulations):
        roll=0
        for num in range(num_dice):
            roll += choice(faces)
        success += roll == total
    return(success/num_simulations)

def simple_class(cls_var):
    '''
    Define a class (with any name you choose) with a class variable named `cls_var` with value `cls_var`.

    You class should have one instance variable called `name`

    Your class should have one method called `speak` which will return the exact string `my name is `name`'
    where `name` is whatever it was passed during initialization

    Parameters
    ----------
    cls_var: a string to be assigned to the class variable `cls_var`

    Returns
    -------
    return the class
    '''
		
    class Myclass(object):
        
        class_var = cls_var #class variable
        
        def __init__(self, name):	
            self.name = name
        
        def speak(self):
            return('my name is ' + self.name)
	
    return Myclass


