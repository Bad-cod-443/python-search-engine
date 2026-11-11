from lru_cache import lru_cache_decorator
from collections import defaultdict
from models import Movie


class MovieIndex:
    def __init__(self):
        # Храним сами объекты фильмов по их ID для быстрого доступа
        self.movies_by_id: dict[int, Movie] = {}

        # Это и есть инвертированный индекс.
        # defaultdict(set) означает, что если жанра еще нет в словаре,
        # он автоматически создаст для него пустое множество (set).
        self.genre_index: dict[str, set[int]] = defaultdict(set)

    def add_movie(self, movie: Movie):
        """Добавляет фильм в базу и индексирует его по жанрам."""
        self.movies_by_id[movie.movie_id] = movie

        for genre in movie.genres:
            # Кладем ID фильма в "коробочку" нужного жанра
            self.genre_index[genre].add(movie.movie_id)

    @lru_cache_decorator(capacity=2)
    def search_by_genre(self, genre: str) -> list[Movie]:
        """Мгновенно находит все фильмы определенного жанра за O(1)."""
        if genre not in self.genre_index:
            return []

        # Получаем множество ID фильмов нужного жанра
        movie_ids = self.genre_index[genre]

        # Достаем сами объекты фильмов из базы по их ID
        result = [self.movies_by_id[m_id] for m_id in movie_ids]

        # Сортируем результат (по умолчанию сработает наш __lt__ из Movie, то есть по рейтингу)
        return sorted(result)


# --- Проверка работы индекса ---
if __name__ == "__main__":
    # ... твой текущий код вывода комедий ...

    from data_loader import load_movies

    # Инициализируем наш "движок"
    index = MovieIndex()

    # Читаем фильмы через генератор и добавляем в индекс
    print("Загрузка данных в индекс...")
    for movie in load_movies("movies.csv"):
        # Для наглядности добавим фейковый рейтинг, чтобы проверить сортировку
        # Пусть у первого фильма будет рейтинг 8.0, у второго 7.5, у третьего 9.0
        if movie.movie_id == 1:
            movie.rating = 8.0
        elif movie.movie_id == 2:
            movie.rating = 7.5
        elif movie.movie_id == 3:
            movie.rating = 9.0

        index.add_movie(movie)

    print("\nДанные загружены! Ищем все фильмы жанра 'Comedy'...")

    # Мгновенный поиск за O(1)
    comedies = index.search_by_genre("Comedy")

    for comedy in comedies:
        print(comedy)

    print("\n--- ТЕСТ КЭШИРОВАНИЯ ---")
    print("1. Второй поиск Comedy:")
    index.search_by_genre("Comedy")  # Должен взять из кэша!

    print("\n2. Поиск Action:")
    index.search_by_genre("Action")  # Должен пойти в базу (кэш теперь помнит Comedy и Action)

    print("\n3. Третий поиск Comedy:")
    index.search_by_genre("Comedy")  # Взял из кэша, Comedy стал самым свежим

    print("\n4. Поиск Sci-Fi (переполнение):")
    index.search_by_genre("Sci-Fi")  # Пойдет в базу. Кэш переполнен (размер 2).
    # Самым старым был Action, он удалится!

    print("\n5. Снова поиск Action:")
    index.search_by_genre("Action")  # Снова пойдет в базу, так как мы его удалили!