import csv
from typing import Generator
from models import Movie  # Импортируем наш класс фильма


def load_movies(filepath: str) -> Generator[Movie, None, None]:
    """
    Генератор, который читает CSV-файл построчно и возвращает объекты Movie.
    """
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Превращаем строку 'Action|Comedy' в список ['Action', 'Comedy']
            genres = row['genres'].split('|')

            # Для простоты пока ставим рейтинг 0.0, если его нет в этом файле
            movie = Movie(
                movie_id=int(row['movieId']),
                title=row['title'],
                genres=genres,
                rating=0.0
            )

            # Вместо return используем yield!
            # yield возвращает фильм и "ставит функцию на паузу", не загружая следующий
            yield movie


# --- Проверка работы генератора ---
if __name__ == "__main__":
    # Тебе понадобится создать фейковый файлик movies.csv рядом со скриптом,
    # чтобы проверить работу (смотри инструкцию ниже)

    # Мы не загружаем весь список! Мы запрашиваем фильмы по одному.
    generator = load_movies("movies.csv")

    print("Первый фильм:", next(generator))
    print("Второй фильм:", next(generator))
    print("Третий фильм:", next(generator))