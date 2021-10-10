number = int(input("Введите количество элементов списка "))
numbers_list = []
i = 0
el = 0
while i < number:
    numbers_list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(numbers_list)/2)):
        numbers_list[el], numbers_list[el + 1] = numbers_list [el + 1], numbers_list[el]
        el += 2
print(numbers_list)