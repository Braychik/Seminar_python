# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12

list = {1:"АВЕИНОРСТ",
        2:"ДКЛМПУ",
        3:"БГЁЬЯ",
        4:"ЙЫ",
        5:"ЖЗХЦЧ",
        8:"ШЭЮ",
        10:"ФЩЪ"}

word = input("Введите слово: ").upper()
summ = 0
for i in word:
    for k, v in list.items():
        if i in v:
            summ += k
print(f"Стоимость слова: {summ}")