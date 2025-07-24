cart = {
    '사과': (2, 1000),
    '바나나': (3, 800),
    '오렌지': (1, 1500)
}

print("쇼핑 카트:")
total = 0
for item, (qty, price) in cart.items():
    item_total = qty * price
    total += item_total
    print(f"{item}: {qty}개 (개당 {price}원) = {item_total}원")

print("총 가격:", total, "원")