import re
import doctest


def is_right_password(password):
    """
    Эта функция проверяет может ли являться входная строка
    (целиком) корректным паролем.

    Args:
    password(str): Строка, что может быть паролем

    Returns:
        bool: True - если входная строка (целиком) может быть корректным паролем, False - если не может.

    >>> is_right_password('rtG3FG!Tr^e')
    True
    >>> is_right_password('aA1!*!1Aa')
    True
    >>> is_right_password('oF^a1D@y5e6')
    True
    >>> is_right_password('enroi#$rkdeR#$092uWedchf34tguv394h')
    True
    >>> is_right_password('пароль')
    False
    >>> is_right_password('password')
    False
    >>> is_right_password('qwerty')
    False
    >>> is_right_password('lOngPa$$$W0Rd')
    False
    """

    pattern = (
        # Состоит из не менее чем шести символов, среди
        # которых только латинские символы, цифры и
        # специальные символы ^$%@#&*!?
        r'^(?=[A-Za-z\d^$%@#&*!?]{6,}$)'
        # По крайней мере одна цифра
        r'(?=.*\d)'
        # По крайней мере два различных специальных символа
        r'(?=.*[!@#$%^&*?])'
        # По крайней мере два символа в верхнем регистре
        r'(?=.*[A-Z].*[A-Z])'
        # Не содержит трех одинаковых символов подряд
        r'(?!.*(.)\1\1)'
    )

    return bool(re.match(pattern, password))


doctest.testmod()
