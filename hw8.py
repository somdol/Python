def buy(shopping_bag):
    item = input('[상품명?]')
    quantity = input('[수량은?]')
    shopping_bag[item] = quantity
    print(f'장바구니에 {item} {quantity}개 담겼습니다.')
    if item == '' :
        return False

def show(dic):
    print(dic)

def find(shopping_bag):
    item = input('장바구니에서 확인하고자 하는 상품은?')
    if item in shopping_bag :
        print(f'{item}은(는) {shopping_bag[item]} 개 담겨 있습니다.')
    else :
        print(f'장바구니에 {item}은(는) 없습니다.')
        
# 주 프로그램부

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)