import re
import doctest


def is_valid_color(color):
    # т.к в примере корректных цветов присутствует такой вот вариант: rgb(255, 255,255),
    # я решил, что функция (а значит и регулярные выражения) будут игнорировать отсутвие
    # (или наличие лишнего) пробела после запятой. Тесты на работоспособность этого
    # отмечены комментарием "запятая-пробел тест"

    """
        Эта функция проверяет может ли являться входная строка
        (целиком) корректной записью цвета в одном из трёх web форматов.

        Args:
        color(str): Строка, что может быть корректной записью цвета

        Returns:
            bool: True - если входная строка (целиком) может быть корректной
            записью цвета в одном из трёх web форматов, False - если не может.

        >>> is_valid_color("#21f48D")
        True
        >>> is_valid_color("#888")
        True
        >>> is_valid_color("rgb(255, 255, 255)")
        True
        >>> is_valid_color("rgb(255, 255,255)") #"запятая-пробел тест"
        True
        >>> is_valid_color("rgb(255,255, 255)") #"запятая-пробел тест"
        True
        >>> is_valid_color("rgb(255,255,255)") #"запятая-пробел тест"
        True
        >>> is_valid_color("rgb(10%, 20%, 0%)")
        True
        >>> is_valid_color("rgb(10%,20%, 0%)") #"запятая-пробел тест"
        True
        >>> is_valid_color("rgb(10%, 20%,0%)") #"запятая-пробел тест"
        True
        >>> is_valid_color("rgb(10%,20%,0%)") #"запятая-пробел тест"
        True
        >>> is_valid_color("hsl(200, 100%, 50%)")
        True
        >>> is_valid_color("hsl(200,100%, 50%)") #"запятая-пробел тест"
        True
        >>> is_valid_color("hsl(200, 100%,50%)") #"запятая-пробел тест"
        True
        >>> is_valid_color("hsl(200,100%,50%)") #"запятая-пробел тест"
        True
        >>> is_valid_color("hsl(0, 0%, 0%)")
        True
        >>> is_valid_color("#2345")
        False
        >>> is_valid_color("ffffff")
        False
        >>> is_valid_color("rgb(257, 50, 10)")
        False
        >>> is_valid_color("hsl(20, 10, 0.5)")
        False
        >>> is_valid_color("hsl(34%, 20%, 50%)")
        False
        """

    pattern_rgb = (
        r'^rgb\((\d{1,2}%?|1\d{0,2}%?|2[0-4]\d%?|25[0-5]%?),\s*(\d{1,2}%?|1\d{0,2}%?|2[0-4]\d%?|25[0-5]%?),'
        r'\s*(\d{1,2}%?|1\d{0,2}%?|2[0-4]\d%?|25[0-5]%?)\)$'
    )

    pattern_hex = (
        r'^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$'
    )

    pattern_hsl = (
        r'^hsl\((\d{1,3}|[1-9]\d?|[12]\d{2}|3[0-5]\d),\s*(100%|[1-9]\d?%|0%),\s*(100%|[1-9]\d?%|0%)\)$'
    )

    return bool(re.match(pattern_rgb, color) or re.match(pattern_hex, color) or re.match(pattern_hsl, color))


doctest.testmod()
