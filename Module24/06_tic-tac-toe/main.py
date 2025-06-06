from typing import List


class Cell:
    def __init__(self, index: int) -> None:
        """
        Создаёт клетку с заданным индексом.
        По умолчанию клетка свободна (symbol = " ").
        """
        self.index: int = index
        self.symbol: str = " "  # Пустая клетка по умолчанию

    def is_taken(self) -> bool:
        """Проверяет, занята ли клетка (то есть, символ не пробел)."""
        return self.symbol != " "

    def __str__(self) -> str:
        """Возвращает символ, если клетка занята, иначе её номер."""
        return self.symbol if self.is_taken() else str(self.index)


class Board:
    def __init__(self) -> None:
        """Создаёт игровое поле из 9 ячеек."""
        self.cells: List[Cell] = [Cell(i) for i in range(1, 10)]

    def display(self) -> None:
        """Печатает текущее состояние игрового поля."""
        print("\n")
        for i in range(0, 9, 3):
            print(" | ".join(str(cell) for cell in self.cells[i:i+3]))
            if i < 6:
                print("-" * 9)

    def update_cell(self, index: int, symbol: str) -> bool:
        """
        Обновляет символ в клетке, если она свободна.
        Возвращает True, если ход сделан, иначе False.
        """
        if not self.cells[index - 1].is_taken():
            self.cells[index - 1].symbol = symbol
            return True
        return False

    def is_full(self) -> bool:
        """Возвращает True, если все клетки заняты."""
        return all(cell.is_taken() for cell in self.cells)

    def check_winner(self, symbol: str) -> bool:
        """Проверяет, есть ли победная комбинация для переданного символа."""
        win_combinations: List[tuple[int, int, int]] = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтали
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикали
            (0, 4, 8), (2, 4, 6)              # диагонали
        ]
        for combo in win_combinations:
            if all(self.cells[i].symbol == symbol for i in combo):
                return True
        return False

    def reset(self) -> None:
        """Сбрасывает поле до начального состояния."""
        for i in range(9):
            self.cells[i] = Cell(i + 1)


class Player:
    def __init__(self, name: str, symbol: str) -> None:
        """
        Создаёт игрока с именем, символом (X или O) и начальным счётом 0.
        """
        self.name: str = name
        self.symbol: str = symbol
        self.score: int = 0

    def make_move(self, board: Board) -> int:
        """
        Запрашивает у пользователя номер клетки и делает ход.
        Возвращает выбранный номер клетки.
        """
        while True:
            try:
                choice: int = int(input(f"{self.name} ({self.symbol}), выбери клетку (1-9): "))
                if 1 <= choice <= 9:
                    if board.update_cell(choice, self.symbol):
                        return choice
                    else:
                        print("Клетка уже занята.")
                else:
                    print("Номер клетки должен быть от 1 до 9.")
            except ValueError:
                print("Пожалуйста, введи корректное число.")


class Game:
    def __init__(self) -> None:
        """
        Создаёт игру, игровое поле и двух игроков.
        """
        self.board: Board = Board()
        self.players: List[Player] = [
            Player(input("Введите имя первого игрока: "), "X"),
            Player(input("Введите имя второго игрока: "), "O")
        ]
        self.current_player_index: int = 0

    def switch_player(self) -> None:
        """Меняет текущего игрока на следующего."""
        self.current_player_index = 1 - self.current_player_index

    def play_round(self) -> bool:
        """
        Запускает один раунд игры.
        Возвращает True, если есть победитель, иначе False.
        """
        self.board.reset()
        self.board.display()

        while True:
            current_player: Player = self.players[self.current_player_index]
            current_player.make_move(self.board)
            self.board.display()

            if self.board.check_winner(current_player.symbol):
                print(f"{current_player.name} победил!")
                current_player.score += 1
                return True

            if self.board.is_full():
                print("Ничья!")
                return False

            self.switch_player()

    def play(self) -> None:
        """Основной игровой цикл. Предлагает сыграть снова после каждого раунда."""
        while True:
            self.play_round()
            print("\nТекущий счёт:")
            for player in self.players:
                print(f"{player.name}: {player.score}")
            again: str = input("\nХотите сыграть ещё раз? (д/н): ").lower()
            if again != 'д':
                print("Спасибо за игру!")
                break


if __name__ == "__main__":
    game: Game = Game()
    game.play()
