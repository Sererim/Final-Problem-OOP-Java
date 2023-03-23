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


class Log:
    def __init__(self):
        log: list[str] = []
        i: int = 1
        self.log = log
        self.i = i

    def __str__(self) -> str:
        foo: str = ""
        for x in self.log:
            foo += f"{x}\n"
        return foo

    def add_to_log(self, entry: str) -> None:
        self.log.append(f"{self.i} ~ {entry}")
        self.i += 1


class Add:
    @staticmethod
    def add(z1: Calculator, z2: Calculator) -> Calculator:
        z = Calculator(z1.x + z2.x, z1.y + z2.y)
        return z


class Mod:
    @staticmethod
    def mod(z1: Calculator) -> float:
        return (z1.x * z1.x + z1.y * z1.y) ** 2


class Conjugate:
    @staticmethod
    def conjugate(z1: Calculator) -> Calculator:
        z = Calculator(z1.x - z1.y)
        return z


class Subtract:
    @staticmethod
    def sub(z1: Calculator, z2: Calculator) -> Calculator:
        z = Calculator(z1.x - z2.x, z1.y - z2.y)
        return z


class Multiply:
    @staticmethod
    def mulp(z1: Calculator, z2: Calculator) -> Calculator:
        x: float = z1.x * z2.x - z1.y * z2.y
        y: float = z1.x * z2.y + z1.y * z2.x
        z = Calculator(x, y)
        return z


class Divide:
    @staticmethod
    def div(z1: Calculator, z2: Calculator) -> Calculator:
        foo: Calculator = Multiply.mulp(z1, Conjugate.conjugate(z2))
        bar: float = Mod.mod(z1) * Mod.mod(z2)
        z = Calculator(foo.x / bar, foo.y / bar)
        return z


def main() -> None:
    z1 = Calculator(0, 5)
    z2 = Calculator(5, 5)
    z3 = Calculator(1, 1)
    lg = Log()

    print(f"{z1}\n{z2}\n{z3}")
    print(Mod.mod(z1))
    lg.add_to_log(f"|{z1.__str__()}| = {Mod.mod(z1)}")
    print(lg)
    print(Add.add(z1, z2))
    lg.add_to_log(f"{z1.__str__()} + {z2.__str__()} = {Add.add(z1, z2)}")
    print(lg)
    print(Divide.div(z2, z3))
    lg.add_to_log(f"{z2.__str__()} / {z3.__str__()} = {Divide.div(z2, z3).__str__()}")
    print(lg)
    print(Conjugate.conjugate(z3))
    print(Multiply.mulp(z3, z2))
    lg.add_to_log(f"{z3.__str__()} * {z2.__str__()} = {Multiply.mulp(z3, z2).__str__()}")
    print(Subtract.sub(z2, z3))
    lg.add_to_log(f"{z1.__str__()} - {z3.__str__()} = {Subtract.sub(z2, z3).__str__()}")
    print(lg)

if __name__ == "__main__":
    main()
