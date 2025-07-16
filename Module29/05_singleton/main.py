from typing import Type, Any, Dict


def singleton(cls: Type) -> Type:
    """
    Декоратор, превращающий класс в синглтон.
    При повторной инициализации возвращается один и тот же экземпляр.
    """
    instances: Dict[Type, Any] = {}

    def get_instance(*args, **kwargs) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)