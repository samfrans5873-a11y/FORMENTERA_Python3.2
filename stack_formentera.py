# Assessment 3.2: Stack Program for FORMENTERA

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed '{item}' -> Current Stack: {self.items}")

    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            print(f"Popped '{item}' -> Current Stack: {self.items}")
            return item
        return None


def run_stack():
    letter_stack = Stack()
    last_name = "FORMENTERA"

    print("=== STACK INSERTION PHASE (PUSH) ===")
    for char in last_name:
        letter_stack.push(char)

    print("\n=== STACK DELETION PHASE (POP) ===")
    while not letter_stack.is_empty():
        letter_stack.pop()

    print("\nStack is now empty!")


if __name__ == "__main__":
    run_stack()