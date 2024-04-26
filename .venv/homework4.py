immutable_var = (1, True, 'String')
print(type(immutable_var))
print(immutable_var)
#immutable_va[0]=20 не поддерживается обращения к элементам.
mutable_list = [1, True, 'String']
print(type(mutable_list))
mutable_list[0] = 2
print(mutable_list)