tup = (1,2,3,4)
tup= tup[1:-1]
tup = tup[0]
print(tup)

#---------2--
# def fun(x):
#     if x % 2==0:
#         return 1
#     else:
#         return
# print(fun(fun(2))+1)
#------- 3 --

dictionary = {'one':'two', 'three':'one','two':'three'}
v = dictionary['one']
for k in range(len(dictionary)):
    v = dictionary[v]
    
print(v)

# try:
#    value = input("engresa a valor: ")
#    print(value/value)
# except ValueError:
#     print("entrada incorrecta")
# except ZeroDivisionError:
#     print("entrada erronea...")
# except TypeError:
#     print("entrada muy erronea...")
# except:
#     print("Buuu!")
#----- 8 --------

def any():
    print(var + 1, end='')
    
var =1
any()
print(var)



def f(x):
    if x==0:
        return x
    return x + f(x-1)

print(f(3))

# my_list = ['mary', 'had', 'a', 'little','lamb']

# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'
    
# print(my_list(my_list))

def fun(x):
    global y
    y = x * x
    return y

fun(2)
print(y)

def fun_1(a):
    return a ** a

def fun_2(a):
    return fun_1(a) * fun_1(a)


print(fun_2(2))
#------- error for missing required argument b
# def fun(a,b):
#     return a ** a

# print(fun(2))

# ------ 
def fun(x):
    
    x +=1
    return x

x = 2
x = fun(x+1)

print(x)


def fun(x,y,z):
    
    return x + 2 * y + z *3

print(fun(0,z=1,y=3))
