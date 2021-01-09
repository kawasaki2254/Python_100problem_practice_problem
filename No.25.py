'''
問題２５．入力した３つの英単語を。カンマ区切りでアルファベット
順になるように並び替えるプログラムを作成してください。
'''

word1 = input('１つ目の英単語を入力してください > ')
word2 = input('２つ目の英単語を入力してください > ')
word3 = input('３つ目の英単語を入力してください > ')

word_list = [word1, word2, word3]

word_list.sort()
word_sort_list = ', '.join(word_list)

print(f'並び替えた英単語 : {word_list}')