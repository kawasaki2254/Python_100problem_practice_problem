'''
問題２２．２つの文字列を入力して、重複する部分だけ
出力するプログラムを作成してください。
'''

word1 = input('１つ目の文字列を入力してください > ')
word2 = input('２つ目の文字列を入力してください > ')

r = ''

for i in word1:
    if i in word2 and not i in r:
        r += i

print(f'重複する文字列 : {r}')

