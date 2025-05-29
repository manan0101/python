name='abc'
print(name)
print(type(name)) #data type of variable
name1='pqr'

name = "Manan Maluka"
print(name)
print(name[::])
print(name[1]) # only single 
print(name[0:3]) # [start:end]
print(name[0:7:2]) # [start:end:Step]
# name[0]="M"  #get error because string is inmutable 
print(name[:6]) # start index is default 0
print(name[3:]) # end index take default length of string-1

print(name)
print(name*3)
print(name+" "+name)

# del name
# print(name) # get error not define