from fastapi import FastAPI, Response, status

from routes.get_subscribers_count import get_subscribers_count

app = FastAPI()

@app.get("/")
async def get_subscribers_count_route(response: Response, lat=None, lon=None, radius=1):
    if (lat is None) or (lat == '') or (lon is None) or (lon == ''):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            'error': 'Latitude and longitude are required'
        }
    return get_subscribers_count(lat, lon, radius)