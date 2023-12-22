# ID успешной посылки: 103603274
import sys

from typing import List


def instructions(cipher: str) -> str:
    """
    Программа, которая расшифровывает сжатые сообщения
    и возвращает строку с командами.
    """
    decoded: str = ''
    multiplier: str = ''
    remember: List[str] = []

    for symbol in cipher:
        if symbol.isdigit():
            multiplier += symbol
        elif symbol == '[':
            remember.append(decoded)
            remember.append(multiplier)
            multiplier, decoded = '', ''
        elif symbol == ']':
            decoded *= int(remember.pop())
            decoded = str(remember.pop()) + decoded
            multiplier = ''
        else:
            decoded += symbol

    return decoded


if __name__ == '__main__':
    cipher = sys.stdin.readline().rstrip()
    print(instructions(cipher))
