#sum of the even-valued terms which are less than 4000000 in Fibonacci series

def summ():
    total=0
    x=1
    y=2
    while (x<=4000000):
        if x%2 == 0:
            total=x+total
        x,y = y,x+y
    return total
print(summ())
        
