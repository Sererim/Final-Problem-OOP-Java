class Calculator:
    x: float
    y: float

    def __init__(self, x: float = None, y: float = None) -> None:
        if x is None and y is None:
            self.x = 0.0
            self.y = 0.0
        elif x is not None and y is None:
            self.x = x
            self.y = 0.0
        elif x is None and y is not None:
            self.x = 0.0
            self.y = y
        else:
            self.x = x
            self.y = y

    def __str__(self) -> str:
        foo: str = ""
        if self.y > 0:
            foo = f"{self.x} + i{self.y}"
        elif self.y < 0:
            foo = f"{self.x} - i{self.y}"
        else:
            foo = f"{self.x}"
        return foo


class Add:
    @staticmethod
    def add(z1: Calculator, z2: Calculator):
        pass


class Mod:
    @staticmethod
    def mod(z1: Calculator):
        pass


class Conjugate:
    @staticmethod
    def conjugate(z1: Calculator):
        pass


class Subtract:
    @staticmethod
    def sub(z1: Calculator):
        pass


class Multiply:
    @staticmethod
    def mulp(z1: Calculator):
        pass


class Divide:
    @staticmethod
    def div(z1: Calculator):
        pass


def main() -> None:
    calc = Calculator(0 , 5)
    print(calc)


if __name__ == "__main__":
    main()
