_filename: str = "book.csv"


class Phonebook:
    def __init__(self, file: str, what: int, sep: str) -> None:
        self.namefile = file
        self.what = what
        self.separator = sep


class ExportPhonebookToFile:

    @staticmethod
    def export(p: Phonebook) -> bool:
        foo: str = ""
        bar: list[str]
        if p.what < 0:
            with open(_filename, 'r') as file:
                foo = file.read()
            bar = foo.split(";")

            with open(p.namefile, 'a') as file:
                for x in range(len(bar) - 1):
                    file.write(bar[x] + p.separator)
        else:
            return False
        return True


class ImportPhonebookIntoFile:

    @staticmethod
    def send(p: Phonebook) -> bool:
        foo: str = ""
        bar: list[str]
        if p.what > 0:
            with open(p.namefile, 'r') as file:
                foo = file.read()
            bar = foo.split(p.separator)

            with open(_filename, 'a') as file:
                for x in range(len(bar) - 1):
                    file.write(bar[x] + p.separator)
        else:
            return False
        return True


def main() -> None:
    ph1 = Phonebook("db.txt", -10, ",")
    ExportPhonebookToFile.export(ph1)
    ph2 = Phonebook("db1.txt", 10, ",")
    ImportPhonebookIntoFile.send(ph2)


if __name__ == "__main__":
    main()
