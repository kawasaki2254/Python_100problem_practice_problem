'''
問題１３．以下のように時速（km/h）を入力したら、秒速（m/s）
が出力されるプログラムを作成してください。
'''

speed = float(input('時速（km/h）を入力してください > ')) / 3600 * 1000

print(f'秒速 = {speed} m/s')

# speed = float(input('時速(km/h)を入力してください > '))
# per_second = speed * 1000 / 60 ** 2
# print(f'秒速 = {per_second} m/s')