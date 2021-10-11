def my_func(x, y, z):
    list = [x, y, z]
    list.remove(min(x, y, z))
    return sum(list)
print(my_func(int(input("enter x ")), int(input("enter y ")), int(input("enter z "))))