def palindrop(s):
    return s == s[::-1]

s = input('Введите слово без пробелов: ')
print(palindrop(s))