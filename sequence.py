#1 

n = int(input("Enter the length of the sequence: ")) # Do not change this line

counter = 0
number1 = 1
number2 = 2
number3 = 3

print (number1)
print (number2)
print (number3)

for n in range (n-3):
    sum = number1 +number2 +number3
    number1 = number2
    number2=number3
    number3=sum
    print(sum)