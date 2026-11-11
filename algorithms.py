from models import Movie


def merge_sorted_movies(list_a: list[Movie], list_b: list[Movie]) -> list[Movie]:
    """
    Сливает два отсортированных по убыванию рейтинга списка фильмов в один.
    Алгоритм Two Pointers. Сложность O(N + M).
    """
    merged_list = []
    i = 0  # Указатель для первого списка
    j = 0  # Указатель для второго списка

    # Пока мы не дошли до конца хотя бы одного из списков
    while i < len(list_a) and j < len(list_b):
        # Если рейтинг в первом списке больше, берем его и двигаем первый указатель
        if list_a[i].rating >= list_b[j].rating:
            merged_list.append(list_a[i])
            i += 1
        # Иначе берем фильм из второго списка и двигаем второй указатель
        else:
            merged_list.append(list_b[j])
            j += 1

    # Если один из списков закончился, просто добавляем остатки другого списка в конец
    while i < len(list_a):
        merged_list.append(list_a[i])
        i += 1

    while j < len(list_b):
        merged_list.append(list_b[j])
        j += 1

    return merged_list


# --- Проверка работы алгоритма ---
if __name__ == "__main__":
    # Создаем два фейковых списка (они уже отсортированы по рейтингу)
    comedies = [
        Movie(1, "Comedy 1", ["Comedy"], 9.0),
        Movie(2, "Comedy 2", ["Comedy"], 8.0),
        Movie(3, "Comedy 3", ["Comedy"], 7.5)
    ]

    actions = [
        Movie(4, "Action 1", ["Action"], 8.8),
        Movie(5, "Action 2", ["Action"], 8.7),
        Movie(6, "Action 3", ["Action"], 7.0)
    ]

    print("Объединяем комедии и боевики...")
    result = merge_sorted_movies(comedies, actions)

    for movie in result:
        print(movie)