curl -X 'POST' \
  'http://127.0.0.1:8000/log/' \
  -H 'Content-Type: application/json' \
  -d '{
        "asctime": "2025-08-25",
        "levelno": 40,
        "message": "Hello, world"
    }'

