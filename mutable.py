  
#to show list and Dict are mutable or not

# list
Fruits = ["Apple","Banana","Mango","Strawberry","Watermelon"]
print(id(Fruits))
print(Fruits)

Vegetables = Fruits
Vegetables[1]='Orange'

print(id(Vegetables))
print(Vegetables)

#dictonary
Fruits = {1:"Apple",2:"Banana",3:"Mango",4:"Strawberry",5:"Watermelon"}
print(id(Fruits))
print(Fruits)

Vegetables = Fruits
Vegetables[1]='Orange'

print(id(Vegetables))
print(Vegetables)