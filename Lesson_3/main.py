def int_input(message):
    while True:
        try:
            result = int(input(message))
        except ValueError:
            print('Вы ввели некорректное значение!')
        except Exception as error:
            print(f'Неизвестная ошибка: {type(error)} {error}!')
        else:
            return result


if __name__ == '__main__':
    a = int_input('Введите первое число: ')
    b = int_input('Введите второе число: ')
    c = int_input('Введите третье число: ')

    # a+b+c
    # a-b-c
    # a*b*c
    # a/b/c
