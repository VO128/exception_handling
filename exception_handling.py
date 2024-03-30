def string_to_int(s):  # добавляем обработку ValueError
    try:
        return int(s)

    except ValueError:
        return f"Ошибка: Невозможно преобразовать '{s}' в целое число"


def read_file(filename):  # добавляем обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Ошибка: Файл '{filename}' не найден"
    except IOError:
        return f"Ошибка ввода/вывода приработе с файлом '{filename}'."


def divide_numbers(a, b):  # добавляем обработку ZeroDivisionError, TypeError return a/b
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    except TypeError:
        return "Ошибка: аргументы должны быть числами"


def access_list_element(lst, index):  # добавляем обработку IndexError, TypeError retun lst[index]
    try:
        return lst[index]
    except IndexError:
        return f"Ошибка: индекс {index} вне диапазона списка"
    except TypeError:
        return "Ошибка: индекс должен быть целым числом"
