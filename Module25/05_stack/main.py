from typing import Any, Optional, Dict, List


class StekNode:
    """
    Узел (ячейка) стека.
    :param data: данные, которые хранятся в ячейке
    :param next: ссылка на следующую ячейку
    """
    def __init__(self, data: Any, next: Optional['StekNode'] = None) -> None:
        self.data: Any = data
        self.next: Optional[StekNode] = next


class Stek:
    """
    Класс Stek — реализация стека (LIFO).
    """
    def __init__(self) -> None:
        self.top: Optional[StekNode] = None  # Верхушка стека

    def put(self, value: Any) -> None:
        """
        Добавляет значение в стек.
        :param value: любые данные, помещаемые в стек
        """
        new_node: StekNode = StekNode(value, self.top)
        self.top = new_node

    def pop(self) -> Optional[Any]:
        """
        Удаляет и возвращает верхний элемент стека.
        :return: данные верхнего узла или None, если стек пуст
        """
        if self.top is None:
            return None
        value: Any = self.top.data
        self.top = self.top.next
        return value

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.
        :return: True, если стек пуст, иначе False
        """
        return self.top is None


class TaskManager:
    """
    Менеджер задач на основе стека.
    Каждая задача имеет имя и приоритет.
    """
    def __init__(self) -> None:
        self.node: Stek = Stek()

    def new_task(self, task: str, prio: int) -> None:
        """
        Добавляет новую задачу в стек.
        :param task: название задачи
        :type task: str
        :param prio: приоритет (чем меньше число, тем выше приоритет)
        :type prio: int
        """
        self.node.put((task, prio))

    def __str__(self) -> str:
        """
        Возвращает отсортированный по приоритету список задач.
        :return: строка с задачами в формате "приоритет задача1; задача2"
        """
        current: Optional[StekNode] = self.node.top
        prio_dict: Dict[int, List[str]] = {}

        # Сбор задач по приоритетам
        while current:
            task, prio = current.data
            if prio in prio_dict:
                prio_dict[prio].append(task)
            else:
                prio_dict[prio] = [task]
            current = current.next

        # Разворачиваем списки задач, чтобы сохранить порядок добавления
        for prio in prio_dict:
            prio_dict[prio] = prio_dict[prio][::-1]

        # Сортируем приоритеты по возрастанию
        sorted_prio: List[tuple[int, List[str]]] = sorted(prio_dict.items())
        return "\n".join(f"{prio} {'; '.join(tasks)}" for prio, tasks in sorted_prio)

    def remove_task(self, task_name: str) -> bool:
        """
        Удаляет ближайшую к вершине задачу с заданным именем.
        :param task_name: название задачи
        :type task_name: str
        :return: True, если задача найдена и удалена, иначе False
        """
        temp_stack: Stek = Stek()
        found: bool = False

        # Переносим задачи во временный стек, пока не найдём нужную
        while not found and not self.node.is_empty():
            task_prio = self.node.pop()
            if task_prio[0] == task_name:
                found = True
            else:
                temp_stack.put(task_prio)

        # Возвращаем оставшиеся задачи обратно
        while not temp_stack.is_empty():
            self.node.put(temp_stack.pop())

        return found

    def remove_all_tasks(self, task_name: str) -> None:
        """
        Удаляет все задачи с заданным именем.
        :param task_name: название задачи
        :type task_name: str
        """
        temp_stack: Stek = Stek()

        # Переносим все задачи, кроме совпадающих, во временный стек
        while not self.node.is_empty():
            task_prio = self.node.pop()
            if task_prio[0] != task_name:
                temp_stack.put(task_prio)

        # Возвращаем задачи обратно
        while not temp_stack.is_empty():
            self.node.put(temp_stack.pop())


# Пример использования
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

# Удаляем одну задачу
manager.remove_task("поесть")
print("\nПосле удаления 'поесть':")
print(manager)

# Удаляем все задачи с приоритетом 4
manager.remove_all_tasks("помыть посуду")
manager.remove_all_tasks("сделать уборку")
print("\nПосле удаления задач приоритета 4:")
print(manager)