def read_lines(filename: str) -> list:
    with open(filename) as file:
        return file.readlines()