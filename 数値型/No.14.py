'''
問題１４．整数aを入力したら、a + aaaを計算するプログラムを
作成してください。　例：a＝２の場合　2+222=224
'''

input_integer = int(input('整数を入力してください > '))

a = input_integer
b = str(input_integer) * 3

b_int = int(b)

result = a + b_int

print(f'計算結果 : {result}')


# a = input('整数を入力してください > ')
# x = int(a)
# y = int(a * 3)
#
# print(f'計算結果 : {x + y}')