'''
問題１５．整数aと整数bを入力したら、a - b を計算するプログラムを
作成してください。ただし、計算結果がマイナスの場合はプラスに変換しましょう。
'''

a = int(input('1つ目の整数を入力してください > '))
b = int(input('2つ目の整数を入力してください > '))

if a >= b:
    print(f'計算結果 : {a - b}')
else:
    print(f'計算結果 : {(a - b) * -1}')


# a = int(input('1つ目の整数を入力してください > '))
# b = int(input('2つ目の整数を入力してください > '))
#
# r = a - b
# r = -r if r < 0 else r
# print(f'計算結果 : {r}')
