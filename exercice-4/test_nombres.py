import art


def number2anybase(num: int, base: int) -> tuple[int]:
    """convertit un nombre en une base quelconque"""
    digits = []
    while num:
        digits.append(num % base)
        num //= base
    return reversed(digits)


class NumberDisplay:
    """Cette classe affiche des nombres dans un alphabet donné sous la forme
    d'un afficheur numérique"""
    TYPE_NUMBERS = {
        "16": "0123456789ABCDEF",
        "10": "0123456789",
        "secret": "OIZELVG#Bq",
    }

    def __init__(self, display_len: int = 4, code: str = "10"):
        self.display_len = display_len
        self.encoding = code

    def show_number(self, number: str, number_source_base: int):
        our_encoding = self.TYPE_NUMBERS[self.encoding]
        our_base = len(our_encoding)
        to_show = "".join(
            our_encoding[a]
            for a in number2anybase(int(number, base=number_source_base), our_base)
        ).rjust(self.display_len, our_encoding[0])
        art.tprint(to_show)


def test_number2anybase():
    assert list(number2anybase(1023, 16)) == [3, 15, 15]  # 0x3ff
    assert list(number2anybase(15, 2)) == [1, 1, 1, 1]


def test_numberdisplay():
    n = NumberDisplay(4, "10")
    n.show_number("4", 10)
    n = NumberDisplay(4, "16")
    n.show_number("1023", 10)
    n = NumberDisplay(5, "secret")
    n.show_number("1337", 10)