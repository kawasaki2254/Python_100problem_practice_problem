'''
問題２１．入力した英単語の先頭１文字が、小文字だったら
大文字に変換、大文字だったら２回反復するプログラムを
作成してください。
'''

word = input('文字列を入力してください > ')

if word[0].islower():
    word = word[0].upper() + word[1:]
elif word[0].isupper():
    word = word * 2

print(f'変換後の文字列 : {word}')