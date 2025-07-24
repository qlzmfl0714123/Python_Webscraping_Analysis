list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print("리스트1:", list1)
print("리스트2:", list2)

merged = sorted(set(list1 + list2))
common = list(set(list1) & set(list2))

print("병합된 리스트:", merged)
print("공통 요소:", sorted(common))