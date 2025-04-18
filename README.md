# Billing System Emulator

To start:
```bash
  uvicorn main:app --reload
```

Requirements:
``
uvicorn, fastapi
``

## API
Request:
``http://{host}?lat=44&lon=1&rad=2``

Reponse:
```
{
    "subscribers_count": 471
}
```
