from re import L
import secrets

from soupsieve import select

chars = 'qwertyuiopasdfghjklzxcvbnm1234567890`~!@#$%^&*()_+-=[]\;,./<>?:"{}|'

def create(number_of_passwords, password_length):
    for i in range(number_of_passwords):
        list = []
        for i in range(password_length):
            select = secrets.choice(chars)
            list.append(select)
        l = ''.join(list)
        print(l)
    return l

create(int(5),int(9))

input('press enter to exit')