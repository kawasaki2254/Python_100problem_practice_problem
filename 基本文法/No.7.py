'''
問題７．問題４で３の倍数のとき'fizz'、５の倍数
のとき'buzz'、１５の倍数のとき'fizzbuzz'、
その他の場合は数字を出力するプログラムを作成しましょう。
'''

for i in range(1, 31):
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
