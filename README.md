rukya_web_dev

Учебный backend-проект на Django (интернет-магазин). В составе есть модули для каталога товаров, корзин, заказов и пользователей, шаблонов и статики.

Возможности

- Каталог товаров (просмотр списка и карточки с товарами)

- Корзина (добавление/удаление, изменение количества)

- Оформление заказа

- Базовая аутентификация/регистрация пользователей

- Админ-панель Django для управления данными

Технологии

- Питон 3.10+

- Django (и внешние пакеты из requirements.txt)

- PostgreSQL или SQLite 

- HTML/CSS (шаблоны в templates/, статика в static/)

- Гит

Структура проекта (основное)
app/                 # настройки Django-проекта
carts/               # корзина
goods/               # каталог товаров
orders/              # оформление и хранение заказов
users/               # пользователи и аутентификация
fixtures/goods/      # фикстуры (данные для загрузки)
templates/           # HTML-шаблоны
static/              # статические файлы
manage.py
requirements.txt

Быстрый старт (локально)

1) Клонируй репозиторий
git clone https://github.com/engineer-rukya/rukya_web_dev.git
cd rukya_web_dev

2) Создай и активируй виртуальное окружение
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

3) Установи в зависимости
pip install --upgrade pip
pip install -r requirements.txt

4) Настроить переменные окружения (по желанию)
Создай файл .envв корне (если используешь PostgreSQL или задаешь SECRET_KEY):
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/dbname

Если переменные не заданы, для старта можно оставить SQLite по умолчанию (см. settings.py).
5) Миграции и суперпользователь
python manage.py migrate
python manage.py createsuperuser

6) (Опционально) Загрузить тестовые данные
Если есть фикстуры в fixtures/goods/:
python manage.py loaddata fixtures/goods/*.json

7) Запуск сервера
python manage.py runserver
Открыть в браузере: http://127.0.0.1:8000/

Полезные команды
# Прогнать тесты (если настроены)
pytest
# или
python -m unittest

Конечные точки (общее представление)

Точные пути достижения от urls.py, но обычно есть:

/admin/— админ-панель

/<catolog>/...— страница каталога

/cart/— корзина

/orders/— оформление заказов

/users/— вход/регистрация

Автор

Гулиева Рукия
GitHub: https://github.com/engineer-rukya

