"""간단한 사칙연산 계산기."""

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(expression):
    """'10 + 5' 같은 문자열을 계산한다. 숫자와 연산자는 공백으로 구분."""
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("'숫자 연산자 숫자' 형식으로 입력하세요 (예: 10 + 5)")
    left, op, right = parts
    if op not in OPERATIONS:
        raise ValueError(f"지원하지 않는 연산자: {op} (+, -, *, / 만 가능)")
    a, b = _to_number(left), _to_number(right)
    result = OPERATIONS[op](a, b)
    if not math.isfinite(result):
        raise ValueError("결과가 너무 큽니다")
    return int(result) if result == int(result) else result


def _to_number(text):
    try:
        number = float(text)
    except ValueError:
        raise ValueError(f"숫자가 아닙니다: {text}") from None
    if not math.isfinite(number):
        raise ValueError(f"너무 크거나 유효하지 않은 숫자입니다: {text}")
    return number


def main():
    print("계산기 (예: 10 + 5, 끝내려면 q)")
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if line in ("q", "quit", "exit"):
            break
        if not line:
            continue
        try:
            print(calculate(line))
        except ValueError as e:
            print(f"오류: {e}")


if __name__ == "__main__":
    main()
