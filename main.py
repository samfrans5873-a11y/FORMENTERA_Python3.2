# Assessment 3.2: Main Runner Program for FORMENTERA
from array_formentera import run_array
from linked_list_formentera import run_linked_list
from stack_formentera import run_stack
from queue_formentera import run_queue

if __name__ == "__main__":
    print("==================================================")
    print("  LINEAR DATA STRUCTURES DEMONSTRATION           ")
    print("  Last Name: FORMENTERA                          ")
    print("==================================================")

    print("\n[1] RUNNING ARRAY PROGRAM:")
    run_array()

    print("\n" + "=" * 50 + "\n")

    print("[2] RUNNING LINKED LIST PROGRAM:")
    run_linked_list()

    print("\n" + "=" * 50 + "\n")

    print("[3] RUNNING STACK PROGRAM:")
    run_stack()

    print("\n" + "=" * 50 + "\n")

    print("[4] RUNNING QUEUE PROGRAM:")
    run_queue()

    print("\n==================================================")
    print("  All data structures executed successfully!     ")
    print("==================================================")