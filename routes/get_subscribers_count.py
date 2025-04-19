from random import randint


def get_subscribers_count(lat, lon, radius):
    '''
    Эмлулирует работу биллинговой системы. Выдает количество абонентов, подключенных к сети и находящихся в пределах радиуса точки
    :param lat: Широта точки
    :param lon: Долгота точки
    :param radius: Радиус
    :return:
    '''
    lat = float(lat)
    lon = float(lon)
    radius = float(radius)

    # Возвращаем эмуляцию работы с использованием псевдослучайных чисел
    return {
        'subscribers_count': randint(10*int(lat)*int(radius)+1, 100*int(lon)*int(radius)+1)
    }
