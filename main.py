find = []
find = input("Введите искомое: ")
file = "text.txt"
count = 0
split_find = []
with open(file, "r", encoding="utf-8") as file1:
    for i in file1:
        if find in i:
            split_find.append(i)
            count += 1
        else:
            print("Строка не найдена")
print(f"Количество искомых строк: {count}")
print(f"Сортированые строки: {sorted(split_find)}")
