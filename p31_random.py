import random as r 

print("Random Float no between 0.0 to 1.0 is : ",r.random())
print("Uniform:random float between given min & max range is : ",r.uniform(6,99))
print("Random integer : between given range : ",r.randint(1,100))
print("Random ",r.randrange(1,100,5))

car=['bmw','mini cooper','range rover','Jaguar','Lamborghini','McLaren']
print(r.choice(car))
print(r.choices(car,k=2))

no=['1','2','3','4','5','6','7','8','9','10']
r.shuffle(no)
print(no)
print(r.sample(no,4))