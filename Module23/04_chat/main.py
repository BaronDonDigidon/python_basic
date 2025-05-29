from typing import TextIO, Optional

def read_chat(chat_file: Optional[TextIO] = "chat_file.txt"):
    """

    :param chat_file:
    :return:
    """
    try:
        with open(chat_file, "a+", encoding="UTF-8") as file_chat:
            file_chat.seek(0)
            print(file_chat.read())
    except OSError as exc:
        print("Ошибка при работе с файлом {}".format(exc))

def send_messege(user_name, chat_file: Optional[TextIO] = "chat_file.txt"):
    """

    :param user_name:
    :param chat_file:
    :return:
    """
    message: str = input("Введите сообщение: ").strip()
    try:
        if len(message) > 0:
            with open(chat_file, "a", encoding="UTF-8") as file_chat:
                    file_chat.write(f"{user_name}: {message}\n")
        else:
            print("Пустое сообщение, сообщение не отправлено")
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
    except Exception as exc:
        print("Непредвиденная ошибка при отправке сообщения: {}".format(exc))




def menu(user_name):
    """

    :param user_name:
    :return:
    """
    while True:
        print("1. Посмотреть текущий текст чата.")
        print("2. Отправить сообщение (затем выводит сообщение)")
        choice: str = input("Ваш выбор: ").strip()
        try:
            if choice == "1":
                read_chat()
            elif choice == "2":
                send_messege(user_name)
            else:
                raise ValueError
        except ValueError:
            print("Введите 1 или 2")



def main():
    """

    :return:
    """
    user_name: str = input("Введите ваше имя: ").strip()
    print("{:-^30}".format("Чат"))
    print("Добро пожаловать в чат {}!".format(user_name))
    menu(user_name)


if __name__ == "__main__":
    main()