'''
問題１７．入力した文字列の、最初と最後の文字を出力する
プログラムを作成してください。
'''

word = []
word_input = input('文字を入力してください > ')

word = word_input

print(f'{word_input}の最初の文字 : {word[0]}')
print(f'{word_input}の最後の文字 : {word[-1]}')


# word = input('文字を入力してください > ')
#
# print(f'{word}の最初の文字 : {word[0]}')
# print(f'{word}の最後の文字 : {word[-1]}')
