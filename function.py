#print Hola based on the parameters passed to it. without the value loop iteration
def hi(times):
    for _ in range(times):
        print("Hola")

hi(5)
#------------- with value of loop iteration ---------------
def hi(times):
    for i in range(times):
        print(f"Hola {i+ 1}")

hi(5)


#Can you send a list to a function as an argument?
#Yes we can , but we  have to pass to it a list. not a single value
def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

print(list_sum([3,2,5]))

# can a list be the result of a function?
# Yes 
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))


