'''
問題１６．入力した文字列と、その長さを出力する
プログラムを作成してください。
'''

word = input('文字を入力してください > ')
count = 0

for i in word:
    count += 1
print(f'{word}の文字数 : {count}')



# input_str = input('文字を入力してください > ')
#
# length = len(input_str)
#
# print(f'{input_str}の文字数 : {length}')