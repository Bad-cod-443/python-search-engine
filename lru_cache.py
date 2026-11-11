from collections import OrderedDict
from typing import Callable, Any


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # OrderedDict помнит порядок, в котором мы добавляем ключи
        self.cache: OrderedDict[str, Any] = OrderedDict()

    def get(self, key: str) -> Any:
        if key not in self.cache:
            return None

        # Если мы обратились к ключу, он становится "самым свежим".
        # Перемещаем его в конец словаря за O(1)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: str, value: Any):
        if key in self.cache:
            # Если ключ уже есть, просто обновляем его и делаем свежим
            self.cache.move_to_end(key)

        self.cache[key] = value

        # Если кэш переполнился, удаляем самый старый элемент (он находится в начале)
        if len(self.cache) > self.capacity:
            # popitem(last=False) удаляет первый (самый старый) элемент за O(1)
            oldest_key, _ = self.cache.popitem(last=False)
            print(f"[КЭШ] Удален самый старый запрос: '{oldest_key}'")


# Декоратор, который мы повесим на нашу функцию поиска
def lru_cache_decorator(capacity: int):
    cache = LRUCache(capacity)

    def decorator(func: Callable):
        def wrapper(self_instance, genre: str):
            # Проверяем, есть ли запрос в кэше
            cached_result = cache.get(genre)
            if cached_result is not None:
                print(f"[КЭШ] Результат для '{genre}' взят из кэша!")
                return cached_result

            # Если в кэше нет, вызываем реальную функцию поиска
            print(f"[ПОИСК] Ищем '{genre}' в базе данных...")
            result = func(self_instance, genre)

            # Сохраняем результат в кэш
            cache.put(genre, result)
            return result

        return wrapper

    return decorator