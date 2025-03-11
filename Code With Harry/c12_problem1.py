a= 89 # this is a global variable

def fun():
    global a # this will help to use the global variable inside the function
    # without the global keyword, this will create a new local variable a
    a = 8 # now the value of a will be 8
    print(a)
fun()
