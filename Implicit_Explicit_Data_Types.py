# Implict Type conversions
integer = 2 
decimal = 5.0
x = decimal + integer
print("Type after adding both values :")
print(type(x))


#Explict  type conversion

a = 2.5
b = "0101"
c= "0101"
print("After converting a to int with base 10 --> ", int(a))
print("After converting b to int with base 2 --> ", int(b, 2))

a = 'A'
print(ord(a))

a = 65
print(chr(a))


a = "McDreamy"
print(tuple(a))
b = [10,7,"It's a beautiful day to save lives",2.0]
print(tuple(b))


a = ((1,"Ross"),(2,"Rachel"),(3,"Friends"))
print(dict(a))
b = [[1,"Meredith"],[2,"Hayes"],[3,"Friends"]]
print(dict(b))

