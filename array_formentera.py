# Assessment 3.2: Array Program for FORMENTERA

class ArrayStructure:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item):
        self.items.append(item)
        print(f"Added '{item}' -> Current Array: {self.items}")

    def delete(self):
        if not self.is_empty():
            item = self.items.pop()
            print(f"Removed '{item}' -> Current Array: {self.items}")
            return item
        return None


def run_array():
    arr = ArrayStructure()
    last_name = "FORMENTERA"

    print("=== ARRAY INSERTION PHASE ===")
    for char in last_name:
        arr.insert(char)

    print("\n=== ARRAY DELETION PHASE ===")
    while not arr.is_empty():
        arr.delete()

    print("\nArray is now empty!")


if __name__ == "__main__":
    run_array()