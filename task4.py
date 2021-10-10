input_string = input("Введите строку из нескольких слов, разделённых пробелами: ")
a = input_string.split(' ')
for i, word in enumerate(a, 1):
    if len(word) > 10:
        el = word[0:10]
    print(f"{i}. {word}")