'''
問題１９．入力した英単語から、母音（a,i,u,e,o）を
取り除くプログラムを作成してください。
'''

vowels = ['a', 'i', 'u', 'e', 'o']

word = input('文字列を入力してください > ')

new_word = ''
for i in word:
    if i in vowels:
        continue
    new_word += i

print(f'作成した文字列 : {new_word}')