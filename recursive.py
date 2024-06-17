  # gues the output of this recursive function with  a =25, then try different value of a , in order to understand how it works
def fun(a):
    print("this is the initial  value of a:")
    if a > 30:
     return 3
    else:
     print(a)
     print(fun(a+3))
     
     return a + fun(a + 3)


print(fun(20))