'''обмеження 13 рядків
Напишіть програму, яка просить користувача ввести ширину та довжину кімнати. 
Після того коли ці значення були прочитані, ваша програма повинна обчислити та 
відобразити площу кімната. Довжину та ширину буде введено як числа з 
плаваючою комою. Включати одиниці у вашому запиті та вихідному 
повідомленні; або фути, або метри, залежно від тої
одиниці, з якою вам зручніше працювати
'''
length = input("Вкажіть довжину кімнати: ")
width = input("Вкажіть ширину кімнати: ")
area = int(length) * int(width)
print(f"Площа кімнати дорівнює: {area} метрів квадратних.")
