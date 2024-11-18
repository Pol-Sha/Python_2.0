#Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42, 3, 3, 3, 13, 13]
new_list = []
for item in data:
    if item not in new_list and data.count(item) > 1:
        new_list.append(item)
print(new_list)