def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#print_params(a, b) Ошибка: name 'a' is not defined
#print_params(b, c) Ошибка: name 'a' is not defined
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [25, 'string', False]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['string', 23.65]
print_params(*values_list_2, 42)