my_str = "привет"
my_float = 2.3434
my_list = ['e', '6']
my_tuple = ('y', '7')
my_int = 12

all_list = [my_float, my_str, my_list, my_tuple, my_int]
for element in all_list:
    print(f'{element} is {type(element)}')