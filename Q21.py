# Write a python program that counts the occurrences of a specific element
# in a list.

n = int(input("Enter the size of the list: "))
lst = []
for i in range(n):
    a = int(input("Enter the number to be inserted in the list: "))
    lst.append(a)
print("The list of given elements is: ", lst)
c = int(input("Enter the element of the list whose count you want to know: "))
if c in lst:
    b = lst.count(c)
    print(f"The element {c} has occurred in the list {b} times.")
else:
    print("The element is not present in the list.")


