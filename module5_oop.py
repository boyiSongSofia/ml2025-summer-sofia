
class NumberStore:
    """
    Simple OOP container to initialize, insert, and search numbers.
    Maintains insertion order. Search returns 1-based index or -1.
    """
    def __init__(self):
        self.data = []

    def insert(self, value: int) -> None:
        self.data.append(value)

    def search(self, target: int) -> int:
        for idx, val in enumerate(self.data, start=1):
            if val == target:
                return idx
        return -1


def read_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            n = int(raw)
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    store = NumberStore()

    n = read_positive_int("Enter N (positive integer): ")
    for i in range(1, n + 1):
        value = read_int(f"Enter number #{i}: ")
        store.insert(value)

    x = read_int("Enter X (integer to search): ")
    result = store.search(x)
    print(result)


if __name__ == "__main__":
    main()
