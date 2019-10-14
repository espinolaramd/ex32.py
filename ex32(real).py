#Diego Espinola
#10.13.19
#Loops and Lists

the_count= [1,2,3,4,5]
fruits= ['apples','oranges','pears','apricots']
change= [1,'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is  count {number}")

#same as above
for fruit in change:
    print(f"A fruit of type: {fruit}")

#also we can go through mixed lists too
#notice we have to use{} since we dont know what's in it
for i in change:
    print(f"I got {i}")

#we can also build lists, firts start with an empty one
elements = []

for i in range (0,6):
 print(f"Adding {i} to the list ")
 elements.append(i)

for i in elements:
    print(f"Element was: {i}")
