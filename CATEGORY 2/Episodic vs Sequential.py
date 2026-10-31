def episodic_environment():
    print("Episodic Environment")
    tasks = ["Clean", "Move", "Clean"]
    for task in tasks:
        print("Action:", task)
        print("Task Completed")

def sequential_environment():
    print("\nSequential Environment")
    position = 0
    while position < 3:
        position += 1
        print("Position:", position)
        print("Action: Move Forward")

episodic_environment()
sequential_environment()
