# модуль 8_2 "Сложные моменты и исключения в стеке вызовов функции"
# ====================================================================
def personal_sum(numbers):  # принимает коллекцию numbers.
    result = 0              # сумма чисел
    incorrect_data = 0      # кол-во некорректных данных
    for i in numbers: # Подсчитывает сумму чисел в numbers путём перебора
        try:
            result += i  # и увеличивать переменную result.
        except TypeError: # Если же при переборе встречается данное типа
               # отличного от числового, то обработать исключение TypeError,
            incorrect_data += 1  # увеличив счётчик incorrect_data на 1.
            print(f'Некорректный тип данных для подсчёта суммы: {i}')
    return (result, incorrect_data) # функция возвращает кортеж :
             # result - сумма чисел, incorrect_data - кол-во некорректных данных.
def calculate_average(numbers): # f принимает коллекцию numbers
    try:
        result_f1= personal_sum(numbers)   # вызываем итог personal_sum(numbers)
        summ_shisel = (len(numbers) - result_f1[1]) # кол-во чисел
        return result_f1[0] / summ_shisel  # среднее арифметическое всех чисел
    except ZeroDivisionError: # т.к.коллекция numbers может оказаться пустой,
                   # то обрабатываем исключение ZeroDivisionError при делении на 0
        return 0                       # и возвращаем 0.
    except TypeError:   # в numbers может быть записана не коллекция,
        # а другие типы данных, например числа. Поэтому обработаем исключение TypeError
                                            # В таком случае функция вернёт None.
        print('В numbers записан некорректный тип данных.')

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается,
                                                    # но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются
#                                                                     # только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

