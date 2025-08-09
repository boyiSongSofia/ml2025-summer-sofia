
from module5_mod import NumberStore

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
