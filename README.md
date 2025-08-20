(README.md)# rukya_web_dev

Учебный backend‑проект на **Django** (интернет‑магазин). В составе есть модули для каталога товаров, корзины, заказов и пользователей, шаблоны и статика.

## Возможности
- Каталог товаров (просмотр списка и карточки товара)  
- Корзина (добавление/удаление, изменение количества)  
- Оформление заказа  
- Базовая аутентификация/регистрация пользователей  
- Админ‑панель Django для управления данными

## Технологии
- **Python 3.10+**  
- **Django** (и зависимости из `requirements.txt`)  
- **PostgreSQL** или **SQLite** (по умолчанию SQLite)  
- **HTML/CSS** (шаблоны в `templates/`, статика в `static/`)  
- **Git**

## Структура проекта
```
app/                 # настройки Django-проекта
carts/               # корзина
goods/               # каталог товаров
orders/              # оформление и хранение заказов
users/               # пользователи и аутентификация
fixtures/goods/      # фикстуры (тестовые данные)
templates/           # HTML-шаблоны
static/              # статические файлы
manage.py
requirements.txt
```

## Быстрый старт (локально)

1. **Клонируй репозиторий**
    ```bash
    git clone https://github.com/engineer-rukya/rukya_web_dev.git
    cd rukya_web_dev
    ```

2. **Создай и активируй виртуальное окружение**
    ```bash
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # macOS / Linux:
    source .venv/bin/activate
    ```

3. **Установи зависимости**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. **(Опционально) Настрой переменные окружения**  
   Создай файл `.env` в корне (при необходимости, например, для PostgreSQL или SECRET_KEY):
    ```
    DJANGO_SECRET_KEY=your_secret_key
    DJANGO_DEBUG=True
    DATABASE_URL=postgres://user:password@localhost:5432/dbname
    ```

5. **Миграции и суперпользователь**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

6. **(Опционально) Загрузить фикстуры**
    ```bash
    python manage.py loaddata fixtures/goods/*.json
    ```

7. **Запуск сервера**
    ```bash
    python manage.py runserver
    ```
    Открой в браузере: `http://127.0.0.1:8000/`

## Полезные команды
```bash
# Прогнать тесты (если подключены)
pytest
# или
python -m unittest
```

## Эндпоинты (ориентировочно)
- `/admin/` — админ‑панель  
- `/goods/`, `/item/<id>/` — каталог и детальная страница  
- `/cart/` — корзина  
- `/orders/` — оформление заказов  
- `/users/` — логин/регистрация

(Пути могут отличаться в зависимости от `urls.py`.)

## Стиль и лучшие практики
- Следование PEP 8  
- Понятные коммиты и ветки (feature/fix)  
- Перед пушем запуск тестов и проверка на ошибки

## Дальнейшие идеи (Roadmap)
- Добавить DRF + JWT-аутентификацию (SimpleJWT)  
- API‑слой (Swagger/OpenAPI)  
- Докеризация (Dockerfile + docker-compose)  
- Пагинация, фильтр и поиск товаров  
- Покрытие тестами логики и API

## Автор
**Гулиева Рукия**  
GitHub: https://github.com/engineer-rukya
