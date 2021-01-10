'''
問題３３．２つのリストで共通の値を出力するプログラムを作成してください。
'''

l1 = ['Python', 'Ruby', 'PHP', 'JavaScript']
l2 = ['Java', 'Ruby', 'Goland', 'Python', 'TypeScript']

l3 = []

for word1 in l1:
    for word2 in l2:
        if word1 == word2 and word1 not in l3:
            l3.append(word1)

print(f'共通する値を格納したリスト : {l3}')