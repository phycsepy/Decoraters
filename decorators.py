'''
r importing modual which is not accessble  
we need play with function recurssion is going to kill us 
 to save as decorators are used
 eg:
here we need to swap is a number is grater than other to avoid float
but without changing the code div ()???
''' 
def smart_div(func):
    def inner(a,b):
        if a < b:
            a,b = b,a#regular swap
        return func(a,b)
    return inner
@smart_div # it may or may not be nesssary it is just a practice
def div(a,b):
    print(a/b)
div = smart_div(div)
div(2,4)