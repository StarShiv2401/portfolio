from waitress import serve
from dotenv import load_dotenv
import os

load_dotenv('.flaskenv')

from portfolio import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    host = os.environ.get('HOST', '0.0.0.0')

    print(f"Starting Waitress server on {host}:{port}")
    serve(app, host=host, port=port)