'''
問題１８．入力した文字列に登場する文字の、出現頻度を
カウントするプログラムを作成してください。
'''

word = input('文字列を入力してください > ')

d = {}
for i in word:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)

