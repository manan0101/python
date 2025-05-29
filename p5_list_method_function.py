l1 =['abc',123,12.3,'pqr',True]
l2 =[123,'second-list']
print(l1);print(l2)
l1.append('python') # add element on end
print(l1)
l1.extend(l2) # add list on last
print(l1)
l1 =['abc',123,12.3,'pqr',True]
l2.extend(['l1',123])
print(l2)

del l1[2] # delete element which  index is passed
print(l1) # delete complete list if index is not passed

del l2
# print(l2)  # get error because l2 list is delete