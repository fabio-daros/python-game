from models.calc import Calc


def main() -> None:
    points: int = 0
    play(points)


def play(points: int) -> None:

    difficulty: int = int(input('Enter the level of difficulty [1, 2, 3 or 4] to play: '))


    calc: Calc = Calc(difficulty)

    print('Enter the result to the following operation: ')
    calc.show_operation()

    result: int = int(input())

    if calc.check_result(result):
        points += 1
        print(f'Correct! You got {points} points.')

    continue_game: int = int(input('Continue in the game? [1 - Yes, 0 - No]: '))

    if continue_game:
        play(points)

    else:
        print(f'Ok, you finished with {points} points.')
        print('See you later!')


if __name__ == '__main__':
    main()
