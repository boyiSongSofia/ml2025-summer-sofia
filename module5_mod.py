
class NumberStore:
    """
    A reusable class that supports data initialization (constructor),
    data insertion (insert), and data search (search).
    Search returns 1-based index of the first occurrence or -1.
    """
    def __init__(self, initial=None):
        self.data = []
        if initial is not None:
            for v in initial:
                self.insert(v)

    def insert(self, value: int) -> None:
        self.data.append(int(value))

    def search(self, target: int) -> int:
        target = int(target)
        for idx, val in enumerate(self.data, start=1):
            if val == target:
                return idx
        return -1
