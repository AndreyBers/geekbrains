name = input('Please enter name ')
sname = input('Please enter surname ')
yob = int(input('Please enter year '))
city = input('Please enter city ')
email = input('Please enter email ')
phone = input('Please input telephone ')

def my_func (name, sname, yob, city, email, phone):
     return ' '.join([name, sname, yob, city, email, phone])