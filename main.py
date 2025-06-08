import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import concurrent.futures  # Для многопоточного парсинга
import openpyxl

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
TIMEOUT = 15  # Увеличенное время ожидания
SLEEP_TIME = 0.5  # Задержка для предотвращения блокировки
MAX_THREADS = 10  # Количество потоков для обработки фильмов одновременно


def process_movie(entry):
    """Обрабатывает информацию о фильме из списка"""
    film_tag = entry.find('td', class_='td-film-details').find('a')
    if not film_tag:
        return None

    film_name = film_tag.text.strip()
    film_url = 'https://letterboxd.com' + film_tag['href']

    release_year_tag = entry.find('td', class_='td-released')
    release_year = release_year_tag.text.strip()[-4:] if release_year_tag else 'Неизвестно'

    rating_tag = entry.find('td', class_='td-rating')
    rating = rating_tag.text.strip() if rating_tag else 'Нет рейтинга'

    # Проверяем, является ли фильм понравившимся (есть ли класс 'has-like')
    like_tag = entry.find('td', class_='td-like center diary-like')
    liked = like_tag and like_tag.find('span',
                                       class_='has-icon icon-16 large-liked icon-liked hide-for-owner') is not None

    return {
        'film_name': film_name,
        'release_year': release_year,
        'rating': rating,
        'liked': liked
    }


def collect_user_rates(user_login):
    """Собирает все фильмы пользователя, проходя по всем страницам"""
    page_num = 1
    data = []

    while True:
        url = f'https://letterboxd.com/{user_login}/films/diary/page/{page_num}/'
        print(f"Парсим страницу {page_num}: {url}")

        try:
            response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            entries = soup.find_all('tr', class_='diary-entry-row')
            print(f"Найдено записей: {len(entries)}")

            if not entries:
                print("Записи закончились, завершаем парсинг.")
                break  # Если записей нет, останавливаемся

            # Многопоточная обработка фильмов
            with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                results = list(executor.map(process_movie, entries))

                # Добавляем только корректные данные
            data.extend([res for res in results if res])

            time.sleep(SLEEP_TIME)
            page_num += 1  # Переход на следующую страницу

        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса {url}: {e}")
            break  # Если ошибка, останавливаем парсинг

    return data


# Засекаем время выполнения
start_time = time.time()

# Собираем данные со всех страниц
user_rates = collect_user_rates(user_login='rfeldman9')
df = pd.DataFrame(user_rates)

# Разделяем понравившиеся и обычные фильмы
liked_movies = df[df['liked']].copy()
liked_movies = liked_movies.sort_values(by='rating', ascending=False)

disliked_movies = df[~df['liked']].copy()

# Сохранение в Excel с разделением на вкладки
file_path = 'user_rates.xlsx'
with pd.ExcelWriter(file_path) as writer:
    disliked_movies.drop(columns=['liked']).to_excel(writer, sheet_name='All Movies', index=False)
    liked_movies.drop(columns=['liked']).to_excel(writer, sheet_name='Liked Movies', index=False)

# Вывод времени выполнения
end_time = time.time()
print(f"Файл сохранен здесь: {file_path}")
print(f"Время выполнения: {round(end_time - start_time, 2)} секунд")