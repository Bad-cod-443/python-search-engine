class Movie:
    def __init__(self, movie_id: int, title: str, genres: list[str], rating: float = 0.0):
        self.movie_id = movie_id
        self.title = title
        self.genres = set(genres)  # Множество для быстрого поиска жанра за O(1)
        self.rating = rating

    # 1. Метод для красивого вывода объекта при print()
    def __repr__(self) -> str:
        return f"Movie(id={self.movie_id}, title='{self.title}', rating={self.rating})"

    # 2. Магические методы для хэширования (чтобы использовать в dict и set)
    def __hash__(self) -> int:
        return hash(self.movie_id)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Movie):
            return False
        return self.movie_id == other.movie_id

    # 3. Магический метод для сравнения (сортировки) по умолчанию — по рейтингу (по убыванию)
    def __lt__(self, other: 'Movie') -> bool:
        # Если используем встроенную функцию sorted(), она по умолчанию сортирует по возрастанию.
        # Чтобы крутые фильмы были первыми, мы инвертируем логику:
        # фильм "меньше", если его рейтинг больше.
        return self.rating > other.rating


# --- Проверка работы ---
if __name__ == "__main__":
    m1 = Movie(1, "The Matrix", ["Action", "Sci-Fi"], 8.7)
    m2 = Movie(2, "Inception", ["Action", "Sci-Fi", "Thriller"], 8.8)
    m3 = Movie(1, "The Matrix", ["Action", "Sci-Fi"], 8.7)

    print("Проверка __repr__:", m1)
    print("Проверка __eq__ (одинаковый ли фильм):", m1 == m3)

    # Благодаря __lt__, мы можем просто сказать max() или sorted()
    movies = [m1, m2]
    print("Лучший фильм:", min(movies))  # min() использует __lt__, вернет Inception (8.8 > 8.7)


    class User:
        def __init__(self, user_id: int, name: str, favorite_genres: list[str]):
            self.user_id = user_id
            self.name = name
            # Используем set, чтобы потом быстро находить пересечения с жанрами фильмов
            self.favorite_genres = set(favorite_genres)

        def __repr__(self) -> str:
            return f"User(id={self.user_id}, name='{self.name}')"

        def __hash__(self) -> int:
            return hash(self.user_id)

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, User):
                return False
            return self.user_id == other.user_id

        # --- Конец класса User. Обрати внимание, что if пишется без отступов ---

    if __name__ == "__main__":
            # Твоя старая проверка фильмов
            m1 = Movie(1, "The Matrix", ["Action", "Sci-Fi"], 8.7)
            m2 = Movie(2, "Inception", ["Action", "Sci-Fi", "Thriller"], 8.8)
            m3 = Movie(1, "The Matrix", ["Action", "Sci-Fi"], 8.7)
            print("Проверка __repr__:", m1)
            print("Проверка __eq__ (одинаковый ли фильм):", m1 == m3)
            print("Лучший фильм:", min([m1, m2]))

            # Новая проверка пользователя (с отступом в 4 пробела, внутри if)
            u1 = User(101, "Audrey", ["Action", "Comedy"])
            u2 = User(101, "Audrey", ["Action", "Comedy"])
            print("Пользователь:", u1)
            print("Один и тот же пользователь?", u1 == u2)
