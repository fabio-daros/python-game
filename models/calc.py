"""
Author: Fabio Daros - 2024/02/12
"""
from random import randint


class Calc:
    def __init__(self: object, difficulty: int, /) -> None:  # Constructor
        self.__difficulty: int = difficulty
        self.__value_1: int = self._generate_value
        self.__value_2: int = self._generate_value
        self.__operation: int = randint(1, 3)  # 1 = sum, 2 = decrease, 3 = multiply
        self.__result: int = self._generate_result

    @property
    def difficulty(self: object) -> int:
        # Property for .__difficulty
        return self.__difficulty

    @property
    def value_1(self: object) -> int:
        return self.__value_1

    @property
    def value_2(self: object) -> int:
        return self.__value_2

    @property
    def operation(self: object) -> int:
        return self.__operation

    @property
    def result(self: object) -> int:
        return self.__result

    def __str__(self: object) -> str:
        op: str = ''
        if self.operation == 1:
            op = 'Sum'
        elif self.operation == 2:
            op = 'Decrease'
        elif self.operation == 3:
            op = 'Multiply'
        else:
            op = 'Unknown operation'
        return (f'Value 1: {self.value_1}\nValue 2: {self.value_2}\nDifficulty: {self.difficulty}'
                f'\nOperation: {op}')

    @property
    def _generate_value(self: object) -> int:
        if self.difficulty == 1:
            return randint(0, 10)
        elif self.difficulty == 2:
            return randint(0, 100)
        elif self.difficulty == 3:
            return randint(0, 1000)
        elif self.difficulty == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _generate_result(self: object) -> int:
        if self.operation == 1:  # Sum
            return self.value_1 + self.value_2
        elif self.operation == 2:  # Decrease
            return self.value_1 - self.value_2
        else:  # Multiplication
            return self.value_1 * self.value_2

    @property
    def _op_symbol(self: object) -> str:
        if self.operation == 1:  # Sum
            return '+'
        elif self.operation == 2:  # Decrease
            return '-'
        else:  # Multiplication
            return 'x'

    def check_result(self: object, response: int) -> bool:
        correct: bool = False

        if self.result == response:
            print('Right Answer!')
            correct = True
        else:
            print('Wrong Answer!')
        print(f'{self.value_1} {self._op_symbol} {self.value_2} = {self.result}')
        return correct

    def show_operation(self: object) -> None:
        print(f'{self.__value_1} {self._op_symbol} {self.value_2} = ?')
