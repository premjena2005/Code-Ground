print(90)
print(1,4,3,"hello world")
print("hii \n bye")
print("my name is \"prem\"")
print(1,2,3,4,5,sep='-')


print("----------------- TYPE")


a=10
b=True
c="prem"
d=12.3
e=complex(2,5)
print(a)
print(d)
print(e)
print("the type of a is",type(a))
print("the type of b is",type(b))
print("the type of c is",type(c))
print("the type of d is",type(d))


print("--------------calculation")


print(4+5)
print(2-3)
print(2*3)
print(2**3)
print(11/2)
print(11//2)
print(10%2)


print("---------------LENGTH")


name="ranu jena"
print(name)
print(len(name))

print(name[0:4])
print(name[0:3])
print(name[0:2])
print(name[0:-5])
print(name[0:-1])
print(name[0:6])


print("----------------FOR LOOP ")

# name is use from the upper task
# lets use a for loop

for i in name:
    print(i)





print("----------------UPPER & LOWER")

str1="ABeufedu"
print(str1.upper())
str2="ABeufedu"
print(str2.lower())

  
print("-----------------IF ELSE CONDITION")

# CONDITIONAL OPERETOR
# < , > , <=, >= , == , !=

a1=int(input("enter your age \n"))
if(a1>=18):
    print("you can drive")

else:
    print("you cannot drive")


print("--------------")
