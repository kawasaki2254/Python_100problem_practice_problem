'''
問題３２．リストに格納されている文字列が短いものから
順番に並べるプログラムを作成してください。
'''

l = ['Python', 'Ruby', 'PHP', 'JavaScript']

sorted_l = sorted(l, key=len)

print(f'短い順に並び替えたリスト : {sorted_l}')