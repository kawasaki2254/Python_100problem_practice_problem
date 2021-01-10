'''
問題３１．リストに格納されている文字列の中で、
一番短い単語を出力するプログラムを作成しましょう。
'''

l = ['Python', 'Ruby', 'PHP', 'JavaScript']

min_length_word, min_length = l[0], len(l[0])

for word in l:
    if len(word) < min_length:
        min_length_word = word
        # min_length = len(word)

print(f'一番短い単語 : {min_length_word}')