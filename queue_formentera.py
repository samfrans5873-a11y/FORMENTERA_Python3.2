# Assessment 3.2: Queue Program for FORMENTERA

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued '{item}' -> Current Queue: {self.items}")

    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            print(f"Dequeued '{item}' -> Current Queue: {self.items}")
            return item
        return None


def run_queue():
    letter_queue = Queue()
    last_name = "FORMENTERA"

    print("=== QUEUE INSERTION PHASE (ENQUEUE) ===")
    for char in last_name:
        letter_queue.enqueue(char)

    print("\n=== QUEUE DELETION PHASE (DEQUEUE) ===")
    while not letter_queue.is_empty():
        letter_queue.dequeue()

    print("\nQueue is now empty!")


if __name__ == "__main__":
    run_queue()