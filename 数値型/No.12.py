'''
問題１２．以下のように体重(kg)と身長(cm)を
自分で入力して、BMIを計算できるように「問題２」
のプログラムを書き換えてください。
'''

h = float(input('身長を入力してください(cm) > ')) / 100
w = float(input('体重を入力してください(kg) > '))

bmi = w / h ** 2

print(f'BMI = {bmi}')