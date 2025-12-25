from flask import Flask, render_template
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    """Главная страница с картой"""
    # Получаем API ключ из переменных окружения
    yandex_api_key = os.getenv('YANDEX_API')
    return render_template('index.html', yandex_api_key=yandex_api_key)

if __name__ == '__main__':
    print("Запуск веб-сайта с Яндекс Картой...")
    print("Откройте браузер и перейдите по адресу: http://127.0.0.1:5000")
    print("Для остановки нажмите Ctrl+C")
    app.run(debug=True)
