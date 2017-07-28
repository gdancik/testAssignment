# return the sum of two numbers
def add(x,y) :
    return x + y

# returns a list with each element of x squared
# if x is an int, you must convert it to a list
def square(x) :
    if type(x) == int :
        num = x
        x = list()
        x.append(num)
    return [i*i for i in x]
    #return [1,4]

