from request import Request
from shop import Shop
from store import Store

store = Store(items={'яблоко': 10, 'дыня': 20, 'слива': 10})
shop = Shop(items={'яблоко': 3, 'дыня': 3, 'слива': 1})


def main():
    print('Добро пожаловать.')
    while True:
        user_input = input('Введите команду в формате "Доставить 1 слива из store в shop"\n'
                           'Введите "стоп", если хотите закончить\n')

        if user_input in ['стоп', 'stop']:
            print('До свидания')
            break

        request = Request(user_input)
        request.move()


if __name__ == '__main__':
    main()
