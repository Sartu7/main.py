import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student} {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Редактирование оценки ученика
        3. Удалить оценку ученику
        4. Добавить нового ученика
        5. Редактирование имени ученика
        6. Удалить ученика из журнала
        7. Добавление названия нового предмета
        8. Редактировать название предмета
        9. Удалить предмет
        10. Вывести средний балл по всем предметам по каждому ученику
        11. Вывести все оценки по всем ученикам 
        12. Вывод среднего бала по каждому предмету для определенного ученика
        13. Вывести все оценки для определенного ученика
        14. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
            #Список оценок по предмету
            print(f'\t{class_} - {students_marks[student][class_]}')
            for student in students:
                print(f'''{student} {students_marks[student]}''')
        # Если данные не верны
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
        print()
#2 КОМАНДА
    elif command == 2:
        print('2. Редактирование оценки ученика')
        #Считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку которую нужно изменить: '))
        new_mark = int(input('Введите новую оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            #Находим индекс оценки
            n = students_marks[student][class_].index(mark)
            # Редактируем оценку для ученика по предмету
            students_marks[student][class_][n] = new_mark
        print(f'Оценка ученика {student} по предмету {class_} изменена с {mark} на {new_mark}')
        #Выводим измененный журнал
        for student in students:
            print(f'''{student} {students_marks[student]}''')
        print()
#3 КОМАНДА
    elif command == 3:
        print('3. Удалить оценку ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
         # Редактируем оценку для ученика по предмету
            students_marks[student][class_].remove(mark)
            print(f'Для ученика {student} по предмету {class_} оценка {mark} удалена')
         # Выводим измененный журнал
            for student in students:
                print(f'''{student} {students_marks[student]}''')
        else:
            print('Ошибка: оценки или ученика нет в журнале')
        print()
#4 КОМАНДА
    elif command == 4:
        print('4. Добавить нового ученика')
        # считываем имя ученика
        student = input('Введите имя нового ученика: ')
        #Добавляем новое имя
        students.append(student)
        print(f'Добавлен новый ученик {student}')
        for student in students:  # 1 итерация: student = 'Александра'
            students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
            # цикл по предметам
            for class_ in classes:  # 1 итерация: class_ = 'Математика'
                marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
                students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
        # выводим получившийся словарь с оценками:
        for student in students:
            print(f'''{student} {students_marks[student]}''')
#5 КОМАНДА
    elif command == 5:
        print('5. Редактирование имени ученика')
        # Считываем имя ученика
        student = input('Введите имя ученика которое нужно изменить: ')
        #Считываем измененное имя
        new_student = input('Введите новое имя ученика: ')
        # если данные введены верно
        if student in students:
            n = students.index(student)
            #Меняем имя ученика
            students[n] = new_student
            print(f'Имя ученика {student} изменено на {new_student}')
            # Выводим полученный список
            for student in students:  # 1 итерация: student = 'Александра'
                students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
                # цикл по предметам
                for class_ in classes:  # 1 итерация: class_ = 'Математика'
                    marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
                    students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
            # выводим получившийся словарь с оценками:
            for student in students:
                print(f'''{student} {students_marks[student]}''')
        else:
            print('Ошибка: Имя введено с ошибкой или отсутвует в журнале')
#6 КОМАНДА
    elif command == 6:
        print('6. Удалить ученика из журнала')
        # считываем имя ученика
        student = (input('Введите имя ученика которого нужно удалить: '))
        # если данные введены верно
        if student in students:
            # Удаляем ученика
            students.remove(student)
            print(f'Ученик {student} удален из списка')
            #Выводим изменненый журнал
            for student in students:
                print(f'''{student} {students_marks[student]}''')
        else:
            print('Ошибка: введеное имя отсутвует в списке')
        print()
#7 КОМАНДА
    elif command == 7:
        print('7. Добавление названия нового предмета')
        # Cчитываем название нового предмета
        class_ = input('Введите название нового предмета: ')
        #Если данные введены верно
        if class_ not in classes:
            #Добавляем предмет
            classes.append(class_)
            #Выводим результат
            print(f'Новый предмет {class_} добален')
            #Выводим изменный журнал
            for student in students:  # 1 итерация: student = 'Александра'
                students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
                # цикл по предметам
                for class_ in classes:  # 1 итерация: class_ = 'Математика'
                    marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
                    students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
            # выводим получившийся словарь с оценками:
            for student in students:
                print(f'''{student} {students_marks[student]}''')
        else:
           print('Oшибка: введеный предмет уже есть журнале')
           print()
#8 КОМАНДА
    elif command == 8:
        print('8. Редактировать название предмета')
        class_ = input('Введите название предмета который хотите изменить: ')
        new_class_ = input('Введите новое название предмета: ')
        #Если данные верну
        if class_ in classes:
            #Находим индекс предмета и меняем название
            n = classes.index(class_)
            classes[n] = new_class_
            print(f'Название предмета {class_} изменено на {new_class_}')
            #Выводим измененный журнал
            for student in students:  # 1 итерация: student = 'Александра'
                students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
                # цикл по предметам
                for class_ in classes:  # 1 итерация: class_ = 'Математика'
                    marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
                    students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
            # выводим получившийся словарь с оценками:
            for student in students:
                print(f'''{student} {students_marks[student]}''')
        else:
           print('Ошибка: вааеденный предмет отсутсвует в журнале')
           print()
#9 КОМАНДА
    elif command == 9:
        print('9. Удалить предмет')
        #Cчитываем название предмета
        class_ = input('Введите название предмета который хотите удалить: ')
        #Если данные верны
        if class_ in classes:
        #Удаляем название предмета
            classes.remove(class_)
            print(f'Предмет {class_} удален')
        #Выводим изменненый журнал
            for student in students:  # 1 итерация: student = 'Александра'
                students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
            # цикл по предметам
                for class_ in classes:  # 1 итерация: class_ = 'Математика'
                    marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
                    students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
        # выводим получившийся словарь с оценками:
            for student in students:
                print(f'''{student} {students_marks[student]}''')
        else:
            print('Ошибка: предмет отсутсвует в журнале или введен с ошибкой')

#10 КОМАНДА
    elif command == 10:
        print('10. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
#11 КОМАНДА
    elif command == 11:
        print('11. Вывести все оценки по всем предметам ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
#12 КОМАНДА
    elif command == 12:
        print('12. Вывод среднего бала по каждому предмету для определенного ученика')
        student = input('Введите имя ученика: ')
        print(student)
        # цикл по предметам
        for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
        print()
#13 КОМАНДА
    elif command == 13:
        print('13. Вывести все оценки для определенного ученика')
        student = input('Введите имя ученика: ')
        print(student)
        #Цикл по предметам
        for class_ in classes:
               print(f'\t{class_} - {students_marks[student][class_]}')
        print()
#14 КОМАНДА
    elif command == 14:
        print('14. Выход из программы')
        break