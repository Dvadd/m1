'''
У багатьох юрисдикціях до ємностей для напоїв додається невеликий депозит, 
щоб заохотити людей переробляти їх. В одній юрисдикції контейнери для напоїв 
місткістю один літр або менше мають заставу в розмірі 0,10 дол. США, а контейнери
для напоїв місткістю понад один літр мають Депозит 0,25 дол.
Напишіть програму, яка зчитує кількість контейнерів кожного розміру 
від користувача. Ваша програма має продовжити обчислення та відображення 
відшкодування, яке буде отримані за повернення цих контейнерів. Відформатуйте
вихідні дані так, щоб вони містили знак долара і дві цифри праворуч від коми.
'''
container1 = input("Яка у вас є кількість контейнерів \nмісткістю один літр або менше?")
container2 = input("Яка у вас є кількість контейнерів \nмісткістю більше одного літра?")
sum = int(container1)*0.10 + int(container2)*0.25
print(f"За повернення контейнерів ви отримаєте: ${round(sum, 3)}.")