from typing import Any, Optional

class Node:
    """
    Класс Node.
    Описывает логику работы одного узла.
    """
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional[Node]= None


class LinkedList:
    """
    Класс LinkedList.
    Работает с узлом, добавляет удаляет или находит элемент по индексу.
    Attributes:
        __head (Any): экземпляр узла
    """
    def __init__(self) -> None:
        self.__head: Optional["Node"] = None


    def append(self, data) -> None:
        """
        Добавление элемента в конец списка.
        :param data: добавляемый элемент
        :type data: Any
        """
        new_node: "Node" = Node(data)
        if self.__head is None:
            self.__head = new_node
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = new_node


    def get(self, index: int) -> Any:
        """
        Получение значения по индексу.
        :param index: индекс
        :type index: int
        :return: значение по указанному индексу
        :rtype: int
        """
        current = self.__head
        current_index = 0
        while current is not None:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1


        raise IndexError("Индекс вне диапазона")


    def remove(self, index: int) -> None:
        """
        Удаление элемента по индексу.
        :param index: индекс удаляемого элемента
        :type index: int
        """
        if self.__head is None:
            raise IndexError("Список пуст")


        if index == 0:
            self.__head = self.__head.next
            return


        current = self.__head
        current_index = 0


        while current is not None and current_index < index - 1:
            current = current.next
            current_index += 1


        if current is None or current.next is None:
            raise IndexError("Индекс вне диапазона")


        current.next = current.next.next


    def __iter__(self):
        current: Optional["Node"] = self.__head
        while current:
            yield current.data
            current = current.next


    def __str__(self):
        return "[" + " ".join(str(item) for item in self) + "]"


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
