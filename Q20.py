# Write a python program that takes a list of numbers and returns their sum.
n = int(input("Enter the size of the list: "))
lst = []
sum = 0
for i in range(n):
    a = int(input("Enter the number to be inserted in the list: "))
    lst.append(a)
    sum = sum+a
print(f"The given list is {lst}")
print("The sum of the elements of the given list is: ",sum)
