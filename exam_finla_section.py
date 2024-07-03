# x = 1// 5+ 1 / 5

# print(x)
# --------- 
# x =1
# y =2
# x,y,z = x,x,y
# z,y,z = x,y,z
# print(x,y,z) 
# print ("hola")


# x  = int(input())
# y = int(input())

# x =x % y
# x = x % y
# y = y % x
# print(y)

# def fun(x,y):
#     if x ==y:
#         return x
#     else:
#         return fun(x,y-1)
    
# print(fun(0,3))
# # ----------- dictionary -------

# dd = {"1":"0", "0":"1"}

# for x in dd.vals():
#     print(x,end="")


# --------- dict ---
# dict = {}
# dict['1']= (1,2)
# dict['2'] = (2,1)

# for x in dict.keys():
#     print(dict[x][1], end="")

# --------- a ^ 0 ---

# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a,b)

# -------- b ** 2 ------

# def fun(a,b):
#     return b ** a
# print(fun(b=2, 2))

# ----------- try and except -------

# try:
#    value = input("engresa a valor: ")
#    print(int(value)/len(value))
# except ValueError:
#     print("entrada incorrecta")
# except ZeroDivisionError:
#     print("entrada erronea...")
# except TypeError:
#     print("entrada muy erronea...")
# except:
#     print("Buuu!")
    
#     # ------------ 4 ** 1/5 -------
# print(4**0.5)
# ----------- infinite loop --------
# i = 0
# while i < i +2:
#     i  += 1
#     print("*")
# else:
#     print("*")
# def fun(x):
#     if x % 2 ==0:
#         return 1
#     else:
#         return 2
    
# print(fun(fun(2)))
# --------- res: 2 -----------

# nums = [1,2,3]
# vals = nums;
# del vals[:]

# print(len(vals))  -----> equal in size/ length
# print(len(nums))


# ------------ x value ? --------

# z= 0
# y = 10

# x = y<z and z >y or y> z and z <y
# print(x)  ---> True

# --------------- a, b , c , sep="sep" ------------

# print("a","b","c",sep="sep") --------  asepbsepc

# ------------  multiple except ---------
# except (TypeError,ValueError,ZeroDivisionError):


# my_list = [x * x for x in range(5)]

# def fun(lst):
#     del lst[lst[2]]
#     return lst
# print(fun(my_list)) ----->[0,1,4,9]


# my_list= [1,2]
# for v in range(2):
#     my_list.insert(-1, my_list[v])
    
# print(my_list) ------> [1,1,1,2]

# tup  = (1,2,4,8)
# tup  = tup[-2:-1]
# tup = tup[-1]
# print(tup)  ------> 4 

# lst = [i for i in range(-1,-2)]

# print(len(lst))  ---> 0
# ---------- how many '#' will print the following peice of code---
# lst = [[x for x in range(3)] for y in range(3) ]
# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 !=0:
#             print("#") 
#         answer    -----> '###'




def fun_1(a):
    return None

def fun_2(a):
    return fun_1(a) * fun_1(a)


print(fun_2(2))