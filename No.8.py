'''
問題８．問題６で出力していた数字（=3の倍数）を持つ「リスト」
を作成して、表示しましょう。
'''

l = []
for i in range(1, 31):
    if i % 3 == 0:
        l.append(i)
print(f'作成したリスト　：　{l}')