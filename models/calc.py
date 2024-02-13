"""
Author: Fabio Daros - 2024/02/12
"""
from random import randint


class Calc:
    def __init__(self: object, difficulty: int, /) -> None:  # constructor
        self.__difficulty: int = difficulty
        self.__value_1: int = self._generate_value
        self.__value_2: int = self._generate_value
        self.__operation: int = randint(1, 3)  # 1 = sum, 2 = decrease, 3 = multiply;
        self.__result: int = self._generate_result

        @property
        def difficulty(self: object) -> int:  # Property from .__difficulty.
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
            return (f'Value 1: {self.value_1} \nValue 2: {self.value_2} \nDifficulty: {self.difficulty}'
                    f'\nOperation: {self.operation}')

        @property
        def _generate_value(self: object) -> int:
            pass

        @property
        def _generate_result(self: object) -> int:
            pass

        def check_result(self: object, response: int) -> bool:
            pass

        def show_operation(self: object) -> None:
            pass
