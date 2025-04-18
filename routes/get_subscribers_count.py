from random import randint


def get_subscribers_count(lat, lon, radius):
    '''

    :param lat:
    :param lon:
    :param radius:
    :return:
    '''
    lat = float(lat)
    lon = float(lon)
    radius = float(radius)

    return randint(10*int(lat)*int(radius), 1000*int(lon)*int(radius))