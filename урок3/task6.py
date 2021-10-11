#def int_func(a):
#    b = a[0].lower() + a[1:]
#    return b
#print(int_func(input("Type a word: ")))
def upcase():
    while True:
        words = input('Enter list of words or * to exit: ').split(" ")
        output = []
        for i in words:
            try:
                if i == '*':
                    print(f'Output is ',' '.join(output), '.Exit')
                    return
                else:
                    capword = i[0].upper() + i[1:]
                    output.append(capword)
            except ValueError:
                print('Enter a word or *')
        print(f'Output is',' '.join(output))
print(upcase())