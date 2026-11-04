# Assessment 3.2: Linked List Program for FORMENTERA

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def get_as_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def insert(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Inserted '{item}' -> Current Linked List: {self.get_as_list()}")

    def delete(self):
        if not self.is_empty():
            removed_data = self.head.data
            self.head = self.head.next
            print(f"Deleted '{removed_data}' -> Current Linked List: {self.get_as_list()}")
            return removed_data
        return None


def run_linked_list():
    ll = LinkedList()
    last_name = "FORMENTERA"

    print("=== LINKED LIST INSERTION PHASE ===")
    for char in last_name:
        ll.insert(char)

    print("\n=== LINKED LIST DELETION PHASE ===")
    while not ll.is_empty():
        ll.delete()

    print("\nLinked List is now empty!")


if __name__ == "__main__":
    run_linked_list()