# factorial of a number 

def pp(num):
    fact = 1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
pp(5)