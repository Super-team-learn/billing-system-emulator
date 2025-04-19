from fastapi import FastAPI, Response, status

# Пути
from routes.get_subscribers_count import get_subscribers_count

app = FastAPI()

@app.get("/subscribers-count")
async def get_subscribers_count_route(response: Response, lat=None, lon=None, radius=1):
    '''
    Запрос числа абонентов сети оператор в радиусе точки
    :param response: Объект ответа
    :param lat: Широта точки
    :param lon: Долгота точки
    :param radius: Радиус поиска абонентов
    :return: JSON-объект
    '''
    if (lat is None) or (lat == '') or (lon is None) or (lon == ''):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            'error': 'Latitude and longitude are required'
        }
    return get_subscribers_count(lat, lon, radius)

# Запуск сервера
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)