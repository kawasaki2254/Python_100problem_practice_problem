'''
問題２４．入力した英単語の中央に、@を差し込んで出力する
プログラムを作成してください。なお、入力した英単語の長さ
が奇数なら、真ん中のアルファベットを@に変換してください。
'''

word = input('英単語を入力してください > ')

word_count = 0

for i in word:
    word_count += 1

index = word_count // 2

if word_count % 2 == 0:
    word = word[:index] + '@' + word[index:]
else:
    word = word[:index] + '@' + word[index + 1:]

print(f'変換した英単語 : {word}')