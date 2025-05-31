t1=('hello',123,11.2,'Manan',True,'Maluka')
t2=(435,'abc')
print(t1);print(t2)
print(t1[3]) 
print(t1[1:3])# return 2nd & 3rd element
print(t1[:3])
print(t1[2:4]) # [start_index : end_index] #value of last_index didn't print
t3=print(t1+t2)
print(t2*3) 
print(t1[-1]) # return last element of tuple
print(t1[-2]) # return second last element of tuple
print(t1[-5:]) # return from last 5th element to last element
print(t1[:5])  # return first five element
#del t1[2] # get error because single element is not possible