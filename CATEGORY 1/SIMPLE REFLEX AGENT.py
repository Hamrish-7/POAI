def simple_reflex_agent(percept):
    if percept == "Dirty":
        return "Clean"
    elif percept == "Clean":
        return "Move"
    else:
        return "Invalid Percept"

location = input("Enter room status (Dirty/Clean): ")

action = simple_reflex_agent(location)

print("Action:", action)
