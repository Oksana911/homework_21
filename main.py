from request import Request, store, shop


def main():
    print('\nДобро пожаловать.\n')
    while True:
        print(f'Сейчас на складе:\n{store}')
        print(f'Сейчас в магазине:\n{shop}')
        user_input = input('Введите команду в формате "Доставить 1 слива из склад в магазин"\n'
                           'Введите "стоп", если хотите закончить\n').lower()

        if user_input in ['стоп', 'stop']:
            print('До свидания')
            break

        try:
            request = Request(user_input)
            request.move()
        except Exception as e:
            print(f'Произошла ошибка: {e}')


if __name__ == '__main__':
    main()
