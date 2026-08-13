def func(num):
    #print(str(num)*3)  #we cannot add with the new variable
    return(num*3)   # we can add with the new variable
func(4)   #does not give the o/p, coz we are using return function not the print function

a=10
c=a+func(4)
print(c)