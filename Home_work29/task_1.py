# Импортируем defaultdict для удобного хранения графа
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        """
        Инициализация графа.
        vertices: количество вершин в графе.
        """
        self.vertices = vertices  # количество вершин
        self.graph = defaultdict(list)  # словарь смежности

    def add_edge(self, u, v):
        """
        Добавление ребра в граф.
        u -> v: направление от вершины u к вершине v.
        """
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        """
        Поиск в глубину для записи порядка завершения вершин.
        v: текущая вершина.
        visited: список, отмечающий посещенные вершины.
        stack: стек для хранения порядка завершения.
        """
        visited[v] = True  # Отмечаем вершину как посещенную
        for neighbor in self.graph[v]:  # Проходим по всем соседям
            if not visited[neighbor]:  # Если сосед еще не посещен
                self.dfs(neighbor, visited, stack)  # Рекурсивно вызываем DFS
        stack.append(v)  # После обработки всех соседей добавляем вершину в стек

    def transpose(self):
        """
        Инвертирование графа (переворот всех ребер).
        """
        transposed_graph = Graph(self.vertices)  # Новый граф с тем же количеством вершин
        for vertex in self.graph:  # Проходим по каждой вершине
            for neighbor in self.graph[vertex]:  # Проходим по всем соседям
                transposed_graph.add_edge(neighbor, vertex)  # Меняем направление ребра
        return transposed_graph

    def find_sccs(self):
        """
        Нахождение сильно связанных компонент в графе.
        """
        stack = []  # Стек для хранения порядка завершения
        visited = [False] * self.vertices  # Список посещенных вершин

        # 1. Прямой обход графа для записи порядка завершения
        for i in range(self.vertices):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # 2. Инвертируем граф
        transposed_graph = self.transpose()

        # 3. Обход инвертированного графа для нахождения ССК
        visited = [False] * self.vertices  # Сброс списка посещенных вершин
        sccs = []  # Список для хранения всех ССК

        while stack:
            vertex = stack.pop()  # Берем вершину с вершины стека
            if not visited[vertex]:
                scc_stack = []  # Временный стек для одной ССК
                transposed_graph.dfs(vertex, visited, scc_stack)
                sccs.append(scc_stack)  # Добавляем ССК в общий список

        return sccs


# Пример использования
if __name__ == "__main__":
    g = Graph(5)  # Создаем граф с 5 вершинами
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(1, 0)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print("Сильно связанные компоненты:")
    sccs = g.find_sccs()
    for scc in sccs:
        print(scc)

"""
Объяснение
Инициализация графа:

Используем defaultdict для удобного хранения списков смежности.
Методы add_edge инициализируют граф.
Прямой обход графа (DFS):

Вершины добавляются в стек после завершения их обработки.
Инвертирование графа:

Меняем направление всех ребер графа, чтобы находить компоненты при обратном DFS.
Обратный обход графа:

Используем порядок из стека, чтобы обрабатывать каждую вершину.
Вывод ССК:

Каждая группа вершин, обработанная в одном DFS на инвертированном графе, является сильно связанной компонентой.
"""

"""
Полный разбор задачи -> G:\Мой диск\Обучение\Beetroot Academy\Информация

Важно!!!
Довольно не понятная тема.Требуется повторение!!!
"""