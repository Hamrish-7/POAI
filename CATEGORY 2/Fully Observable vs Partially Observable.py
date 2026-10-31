def fully_observable():
    rooms = {"A": "Dirty", "B": "Clean"}
    print("Fully Observable Environment")
    print("Environment:", rooms)
    for room, status in rooms.items():
        if status == "Dirty":
            print(room, "-> Clean")
        else:
            print(room, "-> No Action")

def partially_observable():
    rooms = {"A": "Dirty", "B": "Clean"}
    print("\nPartially Observable Environment")
    for room in rooms:
        percept = rooms[room] if room == "A" else "Unknown"
        print("Room:", room, "Percept:", percept)
        if percept == "Dirty":
            print("Action: Clean")
        else:
            print("Action: Move")

fully_observable()
partially_observable()
