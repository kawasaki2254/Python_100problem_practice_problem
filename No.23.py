'''
問題２３．２つの文字列を入力して、重複する「英単語」
を出力するプログラムを作成してください。
'''

sentence1 = input('１つ目の英文を入力してください > ').split()
sentence2 = input('２つ目の英文を入力してください > ').split()

r = []

for i in sentence1:
    if i in sentence2 and not i in r:
        r.append(i)

print(f'重複する英単語 : {r}')

