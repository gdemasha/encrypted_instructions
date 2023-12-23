# ID успешной посылки: 103675429
import sys


def instructions(cipher: str) -> str:
    """Принимает шифрованную строку, возвращает расшифрованную строку."""
    decoded: str = ''
    multiplier: str = ''
    remember: list[tuple[str, str]] = []

    for symbol in cipher:

        if symbol.isdigit():
            multiplier += symbol
        elif symbol == '[':
            remember.append((decoded, multiplier))
            decoded, multiplier = '', ''
        elif symbol == ']':
            symbol, multiplier = remember.pop()
            decoded *= int(multiplier)
            decoded = symbol + decoded
            multiplier = ''
        else:
            decoded += symbol

    return decoded


if __name__ == '__main__':
    print(instructions(sys.stdin.readline().rstrip()))
