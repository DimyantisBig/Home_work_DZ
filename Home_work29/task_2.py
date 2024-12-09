from collections import deque, defaultdict


def bfs_shortest_paths(graph, start):
    """
    Функция для поиска кратчайших путей от одной вершины до всех остальных.
    Используем поиск в ширину (BFS).

    :param graph: Список смежности графа (словарь).
    :param start: Стартовая вершина.
    :return: Словарь с кратчайшими расстояниями от start до каждой вершины.
    """
    # Создаем очередь для BFS
    queue = deque([start])  # Сначала добавляем начальную вершину
    # Храним расстояния от стартовой вершины
    distances = {start: 0}  # Расстояние до себя равно 0

    while queue:  # Пока очередь не пуста
        current = queue.popleft()  # Берем следующую вершину из очереди
        for neighbor in graph[current]:  # Перебираем всех соседей текущей вершины
            if neighbor not in distances:  # Если сосед еще не посещен
                distances[neighbor] = distances[current] + 1  # Считаем расстояние
                queue.append(neighbor)  # Добавляем соседа в очередь для дальнейшего поиска

    return distances


def all_pairs_shortest_paths(graph):
    """
    Функция для поиска кратчайших путей между всеми парами вершин.

    :param graph: Список смежности графа (словарь).
    :return: Матрица кратчайших расстояний.
    """
    # Инициализируем словарь для хранения всех кратчайших расстояний
    shortest_paths = {}

    # Запускаем BFS для каждой вершины графа
    for node in graph:
        # Используем BFS для нахождения кратчайших путей от текущей вершины
        shortest_paths[node] = bfs_shortest_paths(graph, node)

    return shortest_paths


# Пример графа (список смежности)
graph = {
    'A': ['B', 'C'],  # Вершина A соединена с B и C
    'B': ['A', 'D', 'E'],  # Вершина B соединена с A, D и E
    'C': ['A', 'F'],  # Вершина C соединена с A и F
    'D': ['B'],  # Вершина D соединена с B
    'E': ['B', 'F'],  # Вершина E соединена с B и F
    'F': ['C', 'E']  # Вершина F соединена с C и E
}

# Вызываем функцию для нахождения кратчайших путей
result = all_pairs_shortest_paths(graph)

# Выводим результат
for start, paths in result.items():
    print(f"От вершины {start}:")
    for end, distance in paths.items():
        print(f"  До вершины {end}: {distance}")

"""
Объяснение
Список смежности:

graph = {
    'A': ['B', 'C'],
    ...
}
Здесь вершина A соединена с B и C. Это удобно для представления графов.

Функция bfs_shortest_paths:

Использует очередь (deque) для обработки вершин.
Запоминает расстояния в словаре distances.
Функция all_pairs_shortest_paths:

Для каждой вершины запускает bfs_shortest_paths.
Собирает результаты для всех пар.
Вывод результата:

Каждая строка показывает кратчайшее расстояние от одной вершины до другой.
"""

"""
Полный разбор задачи -> G:\Мой диск\Обучение\Beetroot Academy\Информация
Важно!
Повторить ВСЮ тему!
"""