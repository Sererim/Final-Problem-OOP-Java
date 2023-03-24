_filename: str = "database.csv"


class Person:

    def __init__(self, firstname: str, secondname: str, sex: str,
                 position: str, faculty: str) -> None:
        self.firstname = firstname
        self.secondname = secondname
        self.sex = sex
        self.position = position
        self.faculty = faculty

    def __str__(self) -> str:
        foo: str = f"{self.firstname};{self.secondname};" \
                   f"{self.sex};{self.faculty};{self.position};"
        return foo


class University:

    def __init__(self, p: Person) -> None:
        self.person = p
        foo: str = ReadData.read()
        self.datalist = foo.strip('\n').split(";")
        self.data = foo

    def __str__(self) -> str:
        return self.data


class SaveData:

    @staticmethod
    def save(u: University) -> None:
        with open(_filename, "a") as file:
            file.write(f"\n{GetID.id(u)};{u.person.__str__()}")


class ReadData:

    @staticmethod
    def read() -> str:
        foo: str = ""
        with open(_filename, 'r') as file:
            foo = file.read()
        return foo


class GetID:
    @staticmethod
    def id(u: University) -> int:
        foo: int = sum(1 for line in u.datalist)
        foo = int((foo - 1) / 6)
        return foo


class SearchInData:
    @staticmethod
    def search(word: str) -> None:
        foo: int = 0
        bar: str = ""
        with open(_filename) as file:
            lines = file.readlines()
        for k, line in enumerate(lines):
            if line.find(word) != -1:
                foo = k
                for i in range(foo + 1):
                    if (i - 1) % 6 == 0:
                        break
                    bar += f"{lines[i]};"
                for j in range(foo, len(lines)):
                    if (j - 1) % 6 == 0:
                        break
                    bar += f"{lines[j]};"
                print(bar)
                bar = ""


def main() -> None:
    hope = Person("Hope", "von Brawn", "Female", "Physics", "Professor")
    university = University(hope)
    print(ReadData.read())
    SaveData.save(university)
    SearchInData.search("Professor")

if __name__ == "__main__":
    main()
