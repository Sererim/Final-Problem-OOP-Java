class Person:

    def __init__(self, firstName: str, secondName: str, sex: str,
                 position: str, faculty: str) -> None:
        self.firstName = firstName
        self.secondName = secondName
        self.sex = sex
        self.position = position
        self.faculty = faculty

    def __str__(self) -> str:
        foo: str = f"{self.firstName};{self.secondName};" \
                   f"{self.sex};{self.faculty};{self.position};"
        return foo


class University:
    pass


class SaveData:
    pass


class ReadData:
    pass


class GetID:
    pass


class SearchInData:
    pass


class GetData:
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
