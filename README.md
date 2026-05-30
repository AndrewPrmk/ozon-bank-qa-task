Функция поиска самого высокого супергероя:

Функция `get_highest_hero(gender, has_work)` обращается к API (https://akabab.github.io/superhero-api/) и возвращает самого высокого супергероя по заданным критериям:
`gender` — пол героя ("Male" или "Female")
`has_work` — наличие работы (True или False)

Установка и запуск:
1. Установите зависимости:
pip install -r requirements.txt
2. Запустите тесты
pytest tests.py -v