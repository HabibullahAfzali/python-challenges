
#move all zeroes to the end of the array/ to the rigth
# [0,6,0,8,0,1]
def move_zeroes(data):
    fill_index =0;
    for num in data:
        if num !=0:
            data[fill_index]=num
            fill_index +=1
    for remaining_index in range(fill_index,len(data)):
        data[remaining_index] =0
        
        
data=[0,8,6,0,1]
move_zeroes(data)
print(data)

data=[0,0,6,8,1]
move_zeroes(data)
print(data)

data=[0,6,0,8,0,1]
move_zeroes(data)
print(data)