import os

# 確認、讀取檔案
def read_file():
    products = []
    filename = input('請輸入檔案名稱（包含副檔名）： ')
    if os.path.isfile(filename):
        print('已有之前的檔案')
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if '商品' in line:
                    continue
                s = line.strip().split(',')
                products.append(s)
        print(products)
        return products
    else:
        print('找不到檔案......')

# 使用者輸入
def input_products(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
        price = input('請輸入商品價格：')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

def print_products(products):
    for p in products:
        print(p[0],p[1])

# 儲存檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

products = read_file()
products = input_products(products)
print_products(products)
write_file('products.csv',products)