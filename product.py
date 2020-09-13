import os

products = []
# 確認檔案是否存在
if os.path.isfile('products.csv'):
    print('已有之前的檔案')
    # 讀取檔案
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品' in line:
                continue
            s = line.strip().split(',')
            products.append(s)
    print(products)
else:
    print('找不到檔案......')

# 使用者輸入
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    price = int(price)
    products.append([name, price])
print(products)

# 儲存檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')